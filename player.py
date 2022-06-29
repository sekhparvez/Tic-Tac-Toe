class Player:
    list_symbol = ['X', 'O']

    def __init__(self, name) -> None:
        assert len(name) > 1, f"Name {name} cannot be empty or have 1 character"

        self.__name = name
        self.__symbol = ""

    def __str__(self) -> str:
        return f"Player Name: {self.__name} \n Player Symbol: {self.__symbol}"

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 1:
            raise Exception("Name needs to have length of greater than one")
        self.__name = new_name

    @staticmethod
    def set_symbol(player1, player2) -> None:
        print("choose symbol")
        player1.__symbol = input("Please choose X or O \n")
        player2.__symbol = 'O' if player1.__symbol == 'X' else 'X'


if __name__ == "__main__":
    p1 = Player("par")
    p2 = Player("alvi")

    Player.set_symbol(p1, p2)

    print(p1.symbol)
    print(p2.symbol)
