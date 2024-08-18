import socket
import threading
import asyncio
import time
from k_parser import parse_resp
from argparse import ArgumentParser
from TTLCache import TTLCache
from info import RedisReplicationInfo
# Create a CommandParse object
from constants import SLAVE

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
                if len(command) > 8:
                    expiry = command[10]
                    cache.add(key=key, value=value, ttl=expiry)
                else:
                    cache.add(key=key,value=value)
                await loop.sock_sendall(
                    client, CommandParser.respSimpleString("OK").encode()
                )
            case "get":
                key = command[4]
                value = cache.get(key)
                await loop.sock_sendall(
                    client, CommandParser.respBulkString(value).encode()
                )
            case "info":
                key = command[4]
                info_string = info.__str__()
                await loop.sock_sendall(
                    client, CommandParser.respBulkString(info_string).encode()
                )


async def async_main():
    parser = ArgumentParser("A Redis server written in Python")
    parser.add_argument("--port", type=int, default=6379)
    parser.add_argument("--replicaof", type=str)
    if  parser.parse_args().replicaof:
        print(parser.parse_args().replicaof)
        info.update(role=SLAVE)
    port = parser.parse_args().port
    server = socket.create_server(("localhost", port), reuse_port=False)
    server.setblocking(False)
    server.listen()
    print(f"Listening on port {port}")
    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))

cache = TTLCache()
info = RedisReplicationInfo()
my_master = None


if __name__ == "__main__":
    asyncio.run(async_main())
