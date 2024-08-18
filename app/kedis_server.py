import asyncio
import socket
from argparse import ArgumentParser
from k_parser import parse_resp
from TTLCache import TTLCache
from info import RedisReplicationInfo
# Create a CommandParse object
from constants import SLAVE


class CommandParser:
    @staticmethod
    def respSimpleString(message):
        return f"+{message}\r\n"

    @staticmethod
    def respBulkString(message):
        if message is None:
            return "$-1\r\n"
        return f"${len(message)}\r\n{message}\r\n"

    @staticmethod
    def respArray(elements:list) -> str:
        if elements is None:
            return "*-1\r\n"
        
        result = f"*{len(elements)}\r\n"
        
        for element in elements:
            if isinstance(element, str):
                result += CommandParser.respBulkString(element)
            elif isinstance(element, list):
                result += CommandParser.respArray(element)
            else:
                raise ValueError("Unsupported element type in array")
        
        return result
    

class RedisServer:
    def __init__(self):
        self.is_slave = False
        self.master_connection = None
        self.cache = TTLCache() 
        self.info = RedisReplicationInfo()

    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break  # Client disconnected

                command = parse_resp(data.decode().strip())
                cmd = command[0].lower()
                if cmd == "ping":
                    writer.write(b"+PONG\r\n")
                elif cmd == "echo":
                    msg = command[1] if len(command) > 4 else ""
                    writer.write(CommandParser.respBulkString(msg).encode())
                elif cmd == "set":
                    key = command[1] if len(command) > 4 else ""
                    value = command[2] if len(command) > 6 else ""
                    expiry = int(command[5]) if len(command) > 8 else None
                    if expiry:
                        # For demonstration, using cache without TTL
                        self.cache.add(key=key, value=value, ttl=expiry)
                    else:
                        self.cache.add(key=key, value=value)
                    writer.write(CommandParser.respSimpleString("OK").encode())
                elif cmd == "get":
                    key = command[2] if len(command) > 4 else ""
                    value = self.cache.get(key)
                    writer.write(CommandParser.respBulkString(value).encode())
                elif cmd == "info":
                    # Ensure RedisReplicationInfo has a meaningful __str__ method
                    info_string = str(self.info)
                    writer.write(CommandParser.respBulkString(info_string).encode())
                elif cmd == "replconf":
                    writer.write(CommandParser.respSimpleString("OK").encode())
                elif cmd =="psync":
                    if command[1]=="?":
                        if command[2] == "-1":
                            writer.write(CommandParser.respSimpleString(f"FULLRESYNC {self.info.get(RedisReplicationInfo.MASTER_REPLID)} 0").encode())
                else:
                    writer.write(b"-ERR Unknown command\r\n")

                await writer.drain()  # Ensure the response is sent
        finally:
            writer.close()
            await writer.wait_closed()

    async def connect_to_master(self, master_address):
        try:
            reader, writer = await asyncio.open_connection(*master_address)
            print(f"Connected to master at {master_address}")
            self.master_connection = (reader, writer)
        except Exception as e:
            print(f"Failed to connect to master: {e}")

    async def main(self):
        parser = ArgumentParser(
            description="A Redis-like server written in Python")
        parser.add_argument("--port", type=int, default=6379)
        parser.add_argument("--replicaof", type=str,
                            help="Address of the master server")
        args = parser.parse_args()

        if args.replicaof:
            self.is_slave = True
            master_address = tuple(args.replicaof.split(" "))
            await self.connect_to_master(master_address)

            # Wait for the connection to the master to be established
            if not self.master_connection:
                print("Failed to connect to master. Exiting.")
                return
            master_reader = self.master_connection[0]
            master_writer = self.master_connection[1]

            sending_array = [CommandParser.respArray(["PING"]).encode(),
                             CommandParser.respArray(["REPLCONF", "listening-port", str(args.port)]).encode(),
                             CommandParser.respArray(["REPLCONF", "capa", "psync2"]).encode()]

            reciving_array = ["PONG", "OK", "OK"]

            for i , j in zip(sending_array, reciving_array):
                master_writer.write(i)
                await master_writer.drain()
                data = await master_reader.read(1024)
                
                if parse_resp(data.decode().strip()) != j:
                    print("Failed to connect to master. Exiting.")
                    return

            master_writer.write(CommandParser.respArray(["PSYNC", "?", str(-1)]).encode())
            await master_writer.drain()
            data = await master_reader.read(1024)
            data = data.split(" ")
            self.info.update({RedisReplicationInfo.MASTER_REPLID:data[1]})        

        # Create and bind a non-blocking server socket
        server = socket.create_server(('localhost', args.port), reuse_port=False)
        server.setblocking(False)
        server.listen()
        print(f"Listening on port {args.port}")

        loop = asyncio.get_event_loop()
        while True:
            client_socket, _ = await loop.sock_accept(server)
            # Wrap the client socket with StreamReader and StreamWriter
            reader, writer = await asyncio.open_connection(sock=client_socket)
            loop.create_task(self.handle_client(reader, writer))


if __name__ == "__main__":
    redis_server = RedisServer()
    asyncio.run(redis_server.main())
