class GameLogic:
    # ToDos:
    # - implement as a singleton
    # - implement methods

    __board = None
    __queen = None
    __x = -1
    __y = -1

    # public methods
    def is_move_valid(self, board, queen, x, y):
        self.__set_move(self, board, queen, x, y)
        pass

    def is_hitting_move(self):
        pass

    def is_game_won(self):
        pass

    # private methods
    def __set_move(self, board, queen, x, y):
        self.__board = board
        self.__queen = queen
        self.__x = x
        self.__y = y

    def __is_direction_valid(self):
        return self.__is_x_direction_valid(self) and self.__is_x_direction_valid(self)

    def __is_x_direction_valid(self):
        pass

    def __is_y_direction_valid(self):
        pass

    def __is_move_blocked(self):
        return self.__is_move_blocked_by_own_queen(self) and \
               self.__is_move_blocked_by_opposing_queen(self) and \
               self.__is_move_blocked_by_border(self)

    def __is_move_blocked_by_own_queen(self):
        pass

    def __is_move_blocked_by_border(self):
        pass

    def __is_move_blocked_by_opposing_queen(self):
        pass
