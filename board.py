class Board:

    def __init__(self) -> None:
        print("Board object created")
        self.cells = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

    # Step 4: Write a function to show the board as we will show the
    # board multiple times to the users while they are playing.(done)
    def __str__(self) -> str:
        return f"""
        {self.cells[1]} | {self.cells[2]} | {self.cells[3]}
        {self.cells[4]} | {self.cells[5]} | {self.cells[6]}
        {self.cells[7]} | {self.cells[8]} | {self.cells[9]}"""

    # Step 2: Write a function to check whether the board is filled or not.(done)
    # Iterate over the board and return false if the board contains an empty sign or else return true.
    def is_board_filled(self) -> bool:
        for index in range(1, len(self.cells)):
            return True if self.cells[index] != "-" else False
