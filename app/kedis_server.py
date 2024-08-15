import socket
import threading
import asyncio
import time
# Create a CommandParse object


class CommandParser:
    def respSimpleString(message):
        return f"+{message}\r\n"

    def respBulkString(message):
        if message == None:
            return f"$-1\r\n"
        return f"${len(message)}\r\n{message}\r\n"


pong = "+PONG\r\n"
store_dictionary = {}
expiry_dictionary = {}


def set_command_assingment(msg):
    return None


async def handle_client(client):

    loop = asyncio.get_event_loop()

    while req := await loop.sock_recv(client, 1024):
        command = req.decode().split("\r\n")
        print("Received request", req)
        match command[2].lower():
            case "ping":
                await loop.sock_sendall(client, pong.encode())
            case "echo":
                msg = command[4]
                await loop.sock_sendall(
                    client, CommandParser.respBulkString(msg).encode()
                )
            case "set":
                key = command[4]
                value = command[6]
                store_dictionary[key] = value
                if len(command) > 8:
                    expiry = command[10]
                    expiry_dictionary[key] = time.time() * 1000 + int(expiry)
                await loop.sock_sendall(
                    client, CommandParser.respSimpleString("OK").encode()
                )
            case "get":
                key = command[4]
                value = store_dictionary.get(key)
                # Check if the key has expired
                if key in expiry_dictionary:
                    if time.time() * 1000 - expiry_dictionary[key] > 0:
                        value = None
                await loop.sock_sendall(
                    client, CommandParser.respBulkString(value).encode()
                )


async def async_main():
    server = socket.create_server(("localhost", 6379), reuse_port=False)
    server.setblocking(False)
    server.listen()
    print("Listening on port 6379")
    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))
if __name__ == "__main__":
    asyncio.run(async_main())
