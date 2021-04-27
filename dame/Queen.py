class Queen:
    __x = -1
    __y = -1
    __player = -1

    def __init__(self, x, y, player):
        self.set_position(x, y)
        self.__player = player

    def set_position(self, x, y):
        self.__x = x
        self.__y = y

    def get_y_direction(self):
        return -1 if self.__player == 1 else 1

    def get_player(self):
        return self.__player
