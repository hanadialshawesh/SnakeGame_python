import socket
import random

def roll_dice():
    return random.randint(1, 6)

def process_player_input():
    # Process player input (e.g., roll dice)
    return roll_dice()

def send_game_state(client_socket, players):
    game_state = {"players": players}
    client_socket.sendall(str(game_state).encode("utf-8"))

def start_server():
    host = "127.0.0.1"
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server is listening on {host}:{port}")

    client_socket, client_address = server_socket.accept()
    print(f"New connection from {client_address}")

    players = [{"name": "Player 1", "position": 0}]  # You can have multiple players in a list

    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break

            if data.upper() == "R":
                # Process player input and update game state
                players[0]["position"] += process_player_input()

                # Send updated game state to the client
                send_game_state(client_socket, players)

        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
