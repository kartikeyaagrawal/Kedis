import socket
import threading
from typing import Tuple

def to_resp(command: str) -> str:
    # Split the command into its parts
    parts = command.split()
    
    # Create the RESP representation
    # Start with the array size
    resp = f"*{len(parts)}\r\n"
    
    for part in parts:
        # Convert each part to a bulk string
        bulk_string = f"${len(part)}\r\n{part}\r\n"
        resp += bulk_string
    
    return resp

def send_ping(server_address: Tuple[str, int]) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(server_address)
        
        # Define the two commands
        commands = ["INFO Replication"]

        for command in commands:
            # Convert the command to RESP format
            resp_command = to_resp(command=command)
            print(f"Sending: {command}")
            client_socket.sendall(resp_command.encode())
            
            # Receive the response
            response = client_socket.recv(1024).decode()
            print(f"Received: {response.strip()}")
        
        # Close the connection after sending both commands
        client_socket.close()

def main():
    server_address = ("localhost", 6379)
    threads = []

    # Creating multiple threads to send concurrent requests
    for _ in range(1):  # You can adjust the number of concurrent clients
        thread = threading.Thread(target=send_ping, args=(server_address,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
