# Step 3: Write a function to check whether a player has won or not.
from board import Board
from player import Player


class Game:

    def __init__(self, board: Board, player1: Player, player2: Player) -> None:
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def check_for_win(self, board) -> str:
        for index, value in enumerate(board.cells):
            if (0 < index <= 3 and value == value) or (3 < index <= 6 and value == value) or (
                    6 < index <= 9 and value == value):
                return f"{self.player1.name} has won the game" if value == self.player1.symbol else f"{self.player2.name} has won the game"

        # We have to check all the possibilities that we discussed in the previous section.