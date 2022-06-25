import tic_tac_toe


def main() -> None:

    board = tic_tac_toe.Board()

    game_board = board.board

    game_board = board.create_board(game_board)

    board.print_board()


if __name__ == "__main__":
    main()
