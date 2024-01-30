
# import random
# from CircularLinkedList import CircularLinkedList
# from player import Player

# import socket

# HOST = "127.0.0.1" # The server's hostname or IP address
# PORT = 65432  # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST,PORT))
#     s.sendall(b"Hello, Hanadi")
import socket

def start_client():
    host = "127.0.0.1"
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        try:
            user_input = input("Enter 'R' to roll the dice: ")
            if user_input.upper() == "R":
                # Send player input to the server
                client_socket.sendall(user_input.encode("utf-8"))

                # Receive and print the updated game state
                data = client_socket.recv(1024).decode("utf-8")
                print(data)

        except KeyboardInterrupt:
            print("Exiting the game.")
            client_socket.close()
            break

if __name__ == "__main__":
    start_client()
