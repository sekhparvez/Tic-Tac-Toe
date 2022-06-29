from board import Board


def test_board():
    board = Board()
    for index, val in enumerate(board.cells):
        if index == 0:
            continue
        val = "X"
        board.cells[index] = val

    print(board)
    print(board.is_board_filled())


test_board()
