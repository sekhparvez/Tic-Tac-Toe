# Step 3: Write a function to check whether a player has won or not.
from board import Board
from player import Player


class Game:

    def __init__(self, board_cells: list, player1: Player, player2: Player) -> None:
        self.board = board_cells
        self.player1 = player1
        self.player2 = player2

    def check_for_win(self) -> str:
        if (self.__is_first_row(self.player1.symbol)
                or self.__is_second_row(self.player1.symbol)
                or self.__is_third_row(self.player1.symbol)
                or self.__is_first_col(self.player1.symbol)
                or self.__is_second_col(self.player1.symbol)
                or self.__is_third_col(self.player1.symbol)):
            return f"{self.player1.name} wins"
        elif (self.__is_first_row(self.player2.symbol)
                or self.__is_second_row(self.player1.symbol)
                or self.__is_third_row(self.player1.symbol)
                or self.__is_first_col(self.player1.symbol)
                or self.__is_second_col(self.player1.symbol)
                or self.__is_third_col(self.player1.symbol)):
            return f"{self.player2.name} wins"
        else:
            return "no matches found"

    def __is_first_row(self, symbol) -> bool:
        if self.board[1] == symbol and self.board[2] == symbol and self.board[3] == symbol:
            return True
        else:
            return False

    def __is_second_row(self, symbol) -> bool:
        if self.board[4] == symbol and self.board[5] == symbol and self.board[6] == symbol:
            return True
        else:
            return False

    def __is_third_row(self, symbol) -> bool:
        if self.board[7] == symbol and self.board[8] == symbol and self.board[9] == symbol:
            return True
        else:
            return False

    def __is_first_col(self, symbol):
        if self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol:
            return True
        else:
            return False

    def __is_second_col(self, symbol):
        if self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol:
            return True
        else:
            return False

    def __is_third_col(self, symbol):
        if self.board[3] == symbol and self.board[6] == symbol and self.board[9] == symbol:
            return True
        else:
            return False

    def __is_first_diagnoal(self, symbol):
        if self.board[1] == symbol and self.board[5] == symbol and self.board[9] == symbol:
            return True
        else:
            return False

    def __is_second_diagnoal(self, symbol):
        if self.board[3] == symbol and self.board[5] == symbol and self.board[7] == symbol:
            return True
        else:
            return False

        # We have to check all the possibilities that we discussed in the previous section.
