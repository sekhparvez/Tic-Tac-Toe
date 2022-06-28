import tic_tac_toe


def test_board():
    board = tic_tac_toe.Board()
    for index, val in enumerate(board.cells):
        if index == 0:
            continue
        val = "X"
        board.cells[index] = val

    board.display()
    print(board.is_board_filled())


test_board()
