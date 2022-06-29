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

    print(p1.__symbol)

    Player.set_symbol(p1, p2)

    for index, val in enumerate(board.cells):
        if index == 0:
            continue
        val = "X"
        board.cells[index] = val

    print(p1.__symbol)
    print(p2.__symbol)

    game = Game(board.cells, p1, p2)

    print(game.player1, game.player2, game, board)
    print(game.check_for_win(board))


if __name__ == "__main__":
    main()
