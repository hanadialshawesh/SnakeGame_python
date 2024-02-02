import sys
import random
import socket
import threading
from CircularLinkedList import CircularLinkedList
from player import Player



class SnakeGame2:
    def __init__(self , HOST, PORT):
        self.players = CircularLinkedList()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST=HOST
        self.PORT=PORT
        self.isconnected=False
        
    def roll_dice(self):
        return random.randint(1, 6)

    def start_game(self):
        print("===========================================")
        print("The two players enter your name")
        A = input("Player(A) name: ")
        B = input("Player(B) name: ")
        print("===========================================")

        playerA = Player(A)
        playerB = Player(B)

        r = random.randint(1, 10)
        print("Who will start?, Let's see")

        if r % 2 == 0:  # first roll
            print(A + "! you start")
            self.players.add_first(playerA)
            self.players.add_last(playerB)
        else:
            print(B + "! you start")
            self.players.add_first(playerB)
            self.players.add_last(playerA)

        print("===========================================")

        while playerA.get_position() < 100 and playerB.get_position() < 100:
            print("===========================================")

            num = 0
            print(f"{self.players.first().get_player_name()} enter 'R' to roll the dice")

            roll = self.run_client()
            

            if roll.upper() == "R":
                num = self.roll_dice()
                print(f"Your roll dice {num}")
            else:
                print("Invalid input. Enter 'R' to roll the dice.")

            self.players.first().set_position(num)
            num=0

            
            if(self.players.first().get_position() == 1 ):
                self.players.first().set_position(37)
            if(self.players.first().get_position() == 4):
                self.players.first().set_position(10)
            if(self.players.first().get_position() == 8):
                self.players.first().set_position(22)
            if(self.players.first().get_position() == 21):
                self.players.first().set_position(21)
            if(self.players.first().get_position() == 28):
                self.players.first().set_position(48)
            if(self.players.first().get_position() == 50):
                self.players.first().set_position(17)
            if(self.players.first().get_position()== 80):
                self.players.first().set_position(19)
            if(self.players.first().get_position()==71):
                self.players.first().set_position(21)
            
            
            if(self.players.first().get_position()== 36):
                self.players.first().set_position(-30)
            if(self.players.first().get_position() == 62):
                self.players.first().set_position(-44)
            if(self.players.first().get_position() == 48):
                self.players.first().set_position(-22)
            if(self.players.first().get_position() == 32):
                self.players.first().set_position(-22)
            if(self.players.first().get_position() == 88):
                self.players.first().set_position(-64)
            if(self.players.first().get_position() == 95):
                self.players.first().set_position(-39)
            if(self.players.first().get_position() == 97):
                self.players.first().set_position(-19)
        

            if self.players.first().get_position() > 100:
                print(f"{self.players.first().get_player_name()} is in position 100 ")
            else:
                print(f"{self.players.first().get_player_name()} is in position {self.players.first().get_position()}")

            self.players.rotate()
        print("===========================================\n")

        if playerA.get_position() >= 100:
            print(f"||        The winner is .... player {playerA.get_player_name()}        ||\n")
        if playerB.get_position() >= 100:
            print(f"||        The winner is .... player {playerB.get_player_name()}        ||\n")
         

    def run_server(self):
        self.server_socket.bind((self.HOST,self.PORT))
        self.server_socket.listen()

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection established with {client_address}")
            
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        roll = client_socket.recv(1024).decode()
        print(f"Received roll: {roll}")

    def run_client(self):
        if not self.isconnected:
            self.client_socket.connect((self.HOST,self.PORT))
            self.isconnected=True
        roll = input("Enter 'R' to roll the dice: ")
        self.client_socket.send(roll.encode())
        return roll


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please enter Host and Port ")
        sys.exit(0)
    host, port = sys.argv[1], int(sys.argv[2])
    game = SnakeGame2(HOST=host,PORT=port)
    print("-- Welcome to our game, which is a snake and ladders game --\n")
    print("THE RULES OF THE GAME ARE:")
    print("Every player will take turns to roll the dice")
    print("The first player that reaches the highest space on the board, 100, wins")
    print("If you land on any snake head, you will go down to its tail")
    print("If you land at the beginning of a ladder, you will go up to the ladder's top")
    print("If you roll a six, then you get an extra turn\n")
    
    print("Snake symbol: (@)\nLadder symbol: (^)")
    print(
            "----------------------------------------------\n"
            + "100 99  98   @  96  @   94  93  92  91\n"
            + "81  82  83  84  85  86  87  @   89  90 \n"
            + "41  42  43  44  45  46  47  @   49  ^  \n"
            + "^   79  78  77  76  75  74  73  72  ^  \n"
            + "61  @   63  64  65  66  67  68  69  70 \n"
            + "60  59  58  57  56  55  54  53  52  51 \n"
            + "40  39  38  37  @   35  34  33  @   31 \n"
            + "^   22  23  24  25  26  27  ^   29  30 \n"
            + "20  19  18  17  16  15  14  13  12  11 \n"
            + "^   2   3   ^   5   6   7   ^   9   10\n"
            + "----------------------------------------------\n"
    )
    
    exit_game = True
    while exit_game:
        print("Please choose how you want to play:")
        print("1.with your friend\t3. exit")
    
        answer = int(input())
        
        #server
    
        if answer == 1:
            server_thread = threading.Thread(target=game.run_server)
            server_thread.start()

            game.start_game()
        elif answer == 3:
            exit_game = False
            print("Goodbye")
        else:
            print(f"{answer} is an invalid number. Please try again.")

    
