# Step 3: Write a function to check whether a player has won or not.
import random

from board import Board
from player import Player


class Game:

    def __init__(self, board: Board, player1: Player, player2: Player) -> None:
        self.board = board
        self.game_board = self.board.game_board
        print(self.game_board)
        self.player1 = player1
        self.player2 = player2
        self.turn = ""

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
        if self.game_board[1] == symbol and self.game_board[2] == symbol and self.game_board[ 3] == symbol:
            return True
        else:
            return False

    def __is_second_row(self, symbol) -> bool:
        if self.game_board[4] == symbol and self.game_board[5] == symbol and self.game_board[6] == symbol:
            return True
        else:
            return False

    def __is_third_row(self, symbol) -> bool:
        if self.game_board[7] == symbol and self.game_board[8] == symbol and self.game_board[9] == symbol:
            return True
        else:
            return False

    def __is_first_col(self, symbol):
        if self.game_board[1] == symbol and self.game_board[4] == symbol and self.game_board[7] == symbol:
            return True
        else:
            return False

    def __is_second_col(self, symbol):
        if self.game_board[2] == symbol and self.game_board[5] == symbol and self.game_board[8] == symbol:
            return True
        else:
            return False

    def __is_third_col(self, symbol):
        if self.game_board[3] == symbol and self.game_board[6] == symbol and self.game_board[9] == symbol:
            return True
        else:
            return False

    def __is_first_diagnoal(self, symbol):
        if self.game_board[1] == symbol and self.game_board[5] == symbol and self.game_board[9] == symbol:
            return True
        else:
            return False

    def __is_second_diagnoal(self, symbol):
        if self.game_board[3] == symbol and self.game_board[5] == symbol and self.game_board[7] == symbol:
            return True
        else:
            return False

        # We have to check all the possibilities that we discussed in the previous section.

    def __first_turn(self) -> str:
        num = random.randint(1, 2)
        if num == 1:
            print(f"{self.player1.name} goes first")
            return self.player1.name
        else:
            print(f"{self.player2.name} goes first")
            return self.player2.name

    def start_game(self):
        pass

    def make_move(self, number) -> None:

        if self.turn == self.player1.name and self.board.is_pos_empty(number):
            self.game_board[number] = self.player1.symbol
            self.turn = self.player2.name

        elif self.turn == self.player2.name and self.board.is_pos_empty(number):
            self.game_board[number] = self.player2.symbol
            self.turn = self.player1.name

        elif self.turn == "" and self.board.is_pos_empty(number) and self.__first_turn() == self.player1.name:
            self.game_board[number] = self.player1.symbol
            self.turn = self.player2.name

        elif self.turn == "" and self.board.is_pos_empty(number):
            self.game_board[number] = self.player2.symbol
            self.turn = self.player1.name

        else:
            print("That space is occupied please choose again")

        print(self.board)


if __name__ == "__main__":
    pass


