from board import Board


def test_board():
    board = Board()
    for index, val in enumerate(board.game_board):

        if index == 0:
            continue

        if index % 2 == 0:
            board.game_board[index] = 'X'

        else:
            board.game_board[index] = 'O'

    print(board)
    print(board.is_board_filled())


test_board()
