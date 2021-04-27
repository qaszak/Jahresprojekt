import Queen
import GameLogic

# ToDo: think about refactoring: extract board methods in seperate class, rework method __initialize_queens

class Game:
    __board = [[]]
    __queens = []
    __selected_queen = None
    __game_logic = None
    __turn = -1
    __number_of_queens = -1

    def __init__(self, board_size):
        self.__initialize_empty_board(board_size)
        self.__initialize_queens(board_size)

    def start(self, board_size):
        pass

    def select_queen(self):
        pass

    def move_selected_queen(self, x, y):
        pass

    def __initialize_empty_board(self, board_size):
        self.__board = [[None for columns in range(board_size)] for rows in range(board_size)]

    def __initialize_queens(self, board_size):
        step = 2

        # add queens for player 1 (first two rows)
        player = 1
        start_column = 1
        for row in range(0, 2):
            for x in range(start_column, board_size, step):
                self.__add_queen(x, row, player)
            start_column = 0

        # add queens for player 2 (last two rows)
        player = 2
        start_column = 1
        for row in range(board_size - 2, board_size):
            for x in range(start_column, board_size, step):
                self.__add_queen(x, row, player)
            start_column = 0

    def __add_queen(self, x, y, player):
        queen = Queen.Queen(x, y, player)
        self.set_board_tile(x, y, queen)
        self.__queens.append(queen)

    def set_board_tile(self, x, y, value):
        self.__board[y][x] = value

    def get_board_tile(self, x, y):
        return self.__board[y][x]

    ####### TESTING (TEMPORARY)#######
    def print_board(self):
        for row in range(0, len(self.__board)):
            row_output = ""
            for column in range(0, len(self.__board)):
                current_tile = self.get_board_tile(column, row)
                row_output += ("X" if current_tile is None else ("B" if current_tile.get_player() == 1 else "W")) + "   "
            print(row_output)
