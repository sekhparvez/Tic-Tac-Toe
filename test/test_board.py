from board import Board


def test_board():
    board = Board()
    for index, val in enumerate(board.cells):

        if index == 0:
            continue

        if index % 2 == 0:
            board.cells[index] = 'X'

        else:
            board.cells[index] = 'O'

    print(board)
    print(board.is_board_filled())


test_board()
