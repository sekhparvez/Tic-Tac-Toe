import tic_tac_toe
from board import Board
from game import Game
from player import Player


def main() -> None:
    board = Board()
    print(board)
    tic_tac_toe.print_header()

    p1 = Player("par")

    p2 = Player("alvi")

    Player.set_symbol(p1, p2)

    # for index, val in enumerate(board.game_board):
    #     if index == 0:
    #         continue
    #
    #     if index % 2 == 0:
    #         board.game_board[index] = 'X'
    #
    #     else:
    #         board.game_board[index] = 'O'

    print(p1.symbol)
    print(p2.symbol)

    game = Game(board, p1, p2)

    print(game.player1, game.player2)
    print(game.check_for_win())
    game.make_move(1)
    # game.make_move(4)
    # game.make_move(2)
    # game.make_move(5)
    # game.make_move(3)
    print(game.check_for_win())


if __name__ == "__main__":
    main()
