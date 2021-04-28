class Move:
    __player = -1
    __queen = None
    __to_row = -1
    __to_column = -1

    def __init__(self, player, queen, to_row, to_column):
        self.__player = player
        self.__queen = queen
        self.__to_row = to_row
        self.__to_column = to_column

    def get_player(self):
        return self.__player

    def get_queen(self):
        return self.__queen

    def get_row(self):
        return self.__to_row

    def get_column(self):
        return self.__to_column
