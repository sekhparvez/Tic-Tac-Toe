import tic_tac_toe


def main() -> None:
    board = tic_tac_toe.Board()
    print(board)
    tic_tac_toe.print_header()

    p1 = tic_tac_toe.Player("par")

    p2 = tic_tac_toe.Player("alvi")

    tic_tac_toe.set_symbol(p1, p2)

    for index, val in enumerate(board.cells):
        if index == 0:
            continue
        val = "X"
        board.cells[index] = val

    print(p1.symbol)
    print(p2.symbol)

    game = tic_tac_toe.Game(board.cells, p1, p2)

    print(game.player1, game.player2, game, board)
    print(game.check_for_win(board))


if __name__ == "__main__":
    main()
