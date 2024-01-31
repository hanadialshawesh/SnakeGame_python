import random
from CircularLinkedList import CircularLinkedList
from player import Player

class SnakeGame2:
    def __init__(self):
        self.players = CircularLinkedList()
        

    def roll_dice(self):
        return random.randint(1, 6)

    def startgame(self):
        print("===========================================")
        print("The two players enter your name")
        A = "Teletubbies"
        B = input("Player (B) enter your name: ")
        print("===========================================")

        playerA = Player(A)
        playerB = Player(B)

        r = random.randint(1, 10)
        print("Who will start?, Let's see")

        if r % 2 == 0:  # first roll
            print(f"{A}! you start")
            self.players.add_first(playerA)#server
            self.players.add_last(playerB)#
        else:
            print(f"{B}! you start")
            self.players.add_first(playerB)
            self.players.add_last(playerA)

        print("===========================================")
        
        while playerA.get_position() < 100 and playerB.get_position() < 100:
            print("===========================================")
            num = 0
    
            print(f"{self.players.first().get_player_name()} enter 'R' to roll the dice")

            roll = input()
            
            if roll.upper() == "R":
                num += self.roll_dice()
                if num == 6:
                    roll2 = input("You got 6, roll the dice again, enter 'R' to roll the dice: ")
                    if roll2.upper() == "R":
                        num += self.roll_dice()
                        print(f"You got {num}")
                else:
                    print(f"You got {num}")

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
