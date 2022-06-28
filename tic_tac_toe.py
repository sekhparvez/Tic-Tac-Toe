# Steps to complete the Tic Tac Toe Project
# Step 1 : Create a board using a 2-dimensional array and initialize each element as empty.

def print_header() -> None:
    print("Welcome to Tic-Tac-Toe \n")


def set_symbol(player1, player2) -> None:
    print("choose symbol")
    player1.symbol = input("Please choose X or O \n")
    player2.symbol = 'O' if player1.symbol == 'X' else 'X'


class Board:

    def __init__(self) -> None:
        print("Board object created")
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Step 4: Write a function to show the board as we will show the board multiple times to the users while they are playing.(done)
    def __str__(self) -> str:
        return f"""
        {self.cells[1]} | {self.cells[2]} | {self.cells[3]}
        {self.cells[4]} | {self.cells[5]} | {self.cells[6]}
        {self.cells[7]} | {self.cells[8]} | {self.cells[9]}"""

    # Step 2: Write a function to check whether the board is filled or not.(done)
    # Iterate over the board and return false if the board contains an empty sign or else return true.
    def is_board_filled(self) -> bool:
        for val in self.cells:
            return True if val != " " and self.cells[0] == " " else True


# Step 3: Write a function to check whether a player has won or not.
class Game:

    def __init__(self, board, player1, player2) -> None:
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def check_for_win(self, board) -> str:
        for index, value in enumerate(board.cells):
            if (0 < index <= 3 and value == value) or (3 < index <= 6 and value == value) or (6 < index <= 9 and value == value):
                return f"{self.player1.name} has won the game" if value == self.player1.symbol else f"{self.player2.name} has won the game"

        # We have to check all the possibilities that we discussed in the previous section.


# Check for all the rows, columns, and two diagonals.
class Player:
    list_symbol = ['X', 'O']

    def __init__(self, name) -> None:
        self.name = name
        self.symbol = ""

    def __str__(self) -> str:
        return f"Player Name: {self.name} \n Player Symbol: {self.symbol}"


if __name__ == "__main__":
    p1 = Player("par")
    p2 = Player("alvi")

    set_symbol(p1, p2)

    print(p1.symbol)
    print(p2.symbol)

# p2 = Player("alvi", 'O')
# p3 = Player("sazaat", 'X')




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
