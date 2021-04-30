import Move

# wraps a Move-object to prevent the manipulation of the contained Queen-object
# by the caller of Dame.get_possible_moves_for(row, column)

class MoveWrapper:

    __move = None

    def __init__(self, move):
        self.__move = move

    def get_row(self):
        return self.__move.get_row()

    def get_column(self):
        return self.__move.get_column()