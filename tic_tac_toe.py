# Steps to complete the Tic Tac Toe Project
# Step 1 : Create a board using a 2-dimensional array and initialize each element as empty.


class Board:

    def __init__(self) -> None:
        print("Board object created")
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self) -> None:
        print(f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]} ")
        print("----------")
        print(f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]} ")
        print("----------")
        print(f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]} ")


def print_header() -> None:
    print("Welcome to Tic-Tac-Toe \n")


# Step 2: Write a function to check whether the board is filled or not.
# Iterate over the board and return false if the board contains an empty sign or else return true.


# Step 3: Write a function to check whether a player has won or not.
# We have to check all the possibilities that we discussed in the previous section.
# Check for all the rows, columns, and two diagonals.
class Player:
    list_symbol = ['X', 'O']

    def __init__(self, name) -> None:
        self.name = name
        self.symbol = ""


def set_symbol(player1, player2):
    print("choose symbol")
    player1.symbol = input("Please choose X or O \n")

    if player1.symbol == 'X':
        player2.symbol = 'O'
    else:
        player2.symbol = 'X'


p1 = Player("par")
p2 = Player("alvi")

set_symbol(p1, p2)

print(p1.symbol)
print(p2.symbol)

# p2 = Player("alvi", 'O')
# p3 = Player("sazaat", 'X')



# Step 4: Write a function to show the board as we will show the board multiple times to the users while they are playing.

# Step 5: Write a function to start the game.
# * elect the first turn of the player randomly.
# * Write an infinite loop that breaks when the game is over (either win or draw).
# * Show the board to the user to select the spot for the next move.
# * Ask the user to enter the row and column number.
# * Update the spot with the respective player sign.
# * Check whether the current player won the game or not.
# * If the current player won the game, then print a winning message and break the infinite loop.
# * Next, check whether the board is filled or not.
# * If the board is filled, then print the draw message and break the infinite loop.
