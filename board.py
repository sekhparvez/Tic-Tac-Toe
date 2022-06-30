class Board:

    def __init__(self) -> None:
        print("Board object created")
        self.game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

    # Step 4: Write a function to show the board as we will show the
    # board multiple times to the users while they are playing.(done)
    def __str__(self) -> str:
        return f"""
        {self.game_board[1]} | {self.game_board[2]} | {self.game_board[3]}
        {self.game_board[4]} | {self.game_board[5]} | {self.game_board[6]}
        {self.game_board[7]} | {self.game_board[8]} | {self.game_board[9]}"""

    # Step 2: Write a function to check whether the board is filled or not.(done)
    # Iterate over the board and return false if the board contains an empty sign or else return true.
    def is_board_filled(self) -> bool:
        for index in range(1, len(self.game_board)):
            return True if self.game_board[index] != "-" else False

    def is_pos_empty(self, num):
        return True if self.game_board[num] == "-" else False
