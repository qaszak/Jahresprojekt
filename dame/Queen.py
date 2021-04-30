class Queen:

    __row = -1
    __column = -1
    __player = -1
    __character = ""


    def __init__(self, row, column, player, character):
        self.set_position(row, column)
        self.__player = player
        self.__character = character


    def set_position(self, row, column):
        self.__row = row
        self.__column = column


    def get_row(self):
        return self.__row


    def get_column(self):
        return self.__column


    def get_player(self):
        return self.__player


    def get_character(self):
        return self.__character
