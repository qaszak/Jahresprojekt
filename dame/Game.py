import Queen, GameLogic


class Game:

    __board = [[]]
    __queens = []
    __selected_queen = None
    __game_logic = None
    __turn = -1
    __number_of_queens = -1

    def __init__(self, board_size):
        self.__board = [["Test" for columns in range(board_size)] for rows in range(board_size)]
        print(self.__board)

    def start(self, board_size):
        pass

    def select_queen():
        pass

    def move_selected_queen(self, x, y):
        pass

    ########## TESTING #################



