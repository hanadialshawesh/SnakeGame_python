import random
from CircularLinkedList import CircularLinkedList
from player import Player
class SnakeGame1:
    def __init__(self):
        self.players = CircularLinkedList()

    def roll_dice(self):
        return random.randint(1, 6)

    def startgame(self):
        print("===========================================")
        print("I am Teletubbies and I will be player (A)")
        A = "Teletubbies"
        B = input("Player (B) enter your name: ")
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
            if self.players.first().get_player_name() == B:
                roll = input(f"{B} enter 'R' to roll the dice: ")
                if roll.upper() == "R":
                    num = self.roll_dice()
                    print(f"Your roll dice {num}")
                else:
                    print("Invalid input. Enter 'R' to roll the dice.")
            else:
                num = self.roll_dice()
                print(f"{A} your roll dice {num}")

            if num == 6:
                roll2 = input("You got 6, roll the dice again, enter 'R' to roll the dice: ")
                if roll2.upper() == "R":
                    num += self.roll_dice()
                    print(f"You got {num}")
            else:
                print(f"You got {num}")

            self.players.first().set_position(num)

            if self.players.first().get_position() == 1:
                self.players.first().set_position(37)
            if self.players.first().get_position() == 4:
                self.players.first().set_position(10)
            # ... (add other position rules)

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
