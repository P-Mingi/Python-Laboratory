import os 
import csv
from abc import ABC, abstractmethod

os.system("clear")  # I use this to clear the screen

class Board(ABC):
    def __init__(self):
        self._box = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " % (self._box[1], self._box[2], self._box[3]))
        print("- - - - - -")
        print(" %s | %s | %s " % (self._box[4], self._box[5], self._box[6]))
        print("- - - - - -")
        print(" %s | %s | %s " % (self._box[7], self._box[8], self._box[9]))

    @abstractmethod
    def update_box(self, box_no, player):
        pass

    def is_winner(self, player):
        if self._box[1] == player and self._box[2] == player and self._box[3] == player:
            return True
        if self._box[4] == player and self._box[5] == player and self._box[6] == player:
            return True
        if self._box[7] == player and self._box[8] == player and self._box[9] == player:
            return True
        if self._box[1] == player and self._box[4] == player and self._box[7] == player:
            return True
        if self._box[2] == player and self._box[5] == player and self._box[8] == player:
            return True
        if self._box[3] == player and self._box[6] == player and self._box[9] == player:
            return True
        if self._box[1] == player and self._box[5] == player and self._box[9] == player:
            return True
        if self._box[3] == player and self._box[5] == player and self._box[7] == player:
            return True
        return False

    def is_equal(self):
        used_box = 0
        for box in self._box:
            if box != " ":
                used_box += 1
        return used_box == 9

    def reset(self):
        self._box = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

class ConcreteBoard(Board):
    def update_box(self, box_no, player):
        if self._box[box_no] == " ":
            self._box[box_no] = player

class Player(ABC):
    @abstractmethod
    def move(self):
        pass

class XPlayer(Player):
    def move(self):
        return int(input("X) Please choose 1 - 9 = "))

class OPlayer(Player):
    def move(self):
        return int(input("O) Please choose 1 - 9 = "))

class PlayerFactory(ABC):
    @abstractmethod
    def create_player(self):
        pass

class XPlayerFactory(PlayerFactory):
    def create_player(self):
        return PlayerMoveDecorator(XPlayer())

class OPlayerFactory(PlayerFactory):
    def create_player(self):
        return PlayerMoveDecorator(OPlayer())

class PlayerMoveDecorator(Player):
    def __init__(self, player):
        self.player = player

    def move(self):
        print(f"{self.player.__class__.__name__} is making a move.")
        return self.player.move()

def save_game_results(results, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Player', 'Wins']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for player, wins in results.items():
            writer.writerow({'Player': player, 'Wins': wins})

def load_game_results(filename):
    results = {}
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = row['Player']
            wins = int(row['Wins'])
            results[player] = wins
    return results

def print_title(game_results):
    print("Hi welcome to the game !")
    print("Current Score:")
    for player, wins in game_results.items():
        print(f"{player}: {wins} wins")
    print(" ")

def refresh_screen(board, game_results):
    os.system("clear")
    print_title(game_results)
    board.display()

def play_game():
    game_results = load_game_results("game_results.csv")
    board = ConcreteBoard()

    while True:     
        refresh_screen(board, game_results)

        x_factory = XPlayerFactory()
        o_factory = OPlayerFactory()

        o_player = o_factory.create_player()  # "O" player created first
        x_player = x_factory.create_player()

        o_choice = o_player.move()
        board.update_box(o_choice, "O")

        refresh_screen(board, game_results)

        if board.is_winner("O"):
            print("O won")
            game_results["O"] += 1
            save_game_results(game_results, "game_results.csv")
            break

        if board.is_equal():
            print("There isn't any winner")
            save_game_results(game_results, "game_results.csv")
            break

        x_choice = x_player.move()
        board.update_box(x_choice, "X")

        if board.is_winner("X"):
            print("X won")
            game_results["X"] += 1
            save_game_results(game_results, "game_results.csv")
            break

        if board.is_equal():
            print("There isn't any winner")
            save_game_results(game_results, "game_results.csv")
            break

while True:
    play_game()
    play_again = input("Do you want to play again ? (Yes or No) = ")
    if play_again.lower() != "yes":
        break
