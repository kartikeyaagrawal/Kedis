import socket
import threading
from typing import Tuple

def send_ping(server_address: Tuple[str, int]) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(server_address)
        command = "*2\r\n$4\r\nECHO\r\n$3\r\nhey\r\n"
        print(f"Sending: {command}")
        client_socket.sendall(command.encode())

        # Receive the response
        response = client_socket.recv(1024).decode()
        print(f"Received: {response.strip()}")

def main():
    server_address = ("localhost", 6379)
    threads = []

    # Creating multiple threads to send concurrent PING requests
    for _ in range(1):  # You can adjust the number of concurrent clients
        thread = threading.Thread(target=send_ping, args=(server_address,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
