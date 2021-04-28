import Queen


class DameBoard:
    __board = [[]]
    __queens = []

    def __init__(self, board_size):
        self.__initialize_empty_board(board_size)
        self.__place_queens_for_player(board_size, 1)
        self.__place_queens_for_player(board_size, 2)


    def set_tile(self, row, column, value):
        self.__board[column][row] = value


    def get_tile(self, row, column):
        return self.__board[column][row]


    def get_queens_for_player(self, player):
        output = []
        for queen in self.__queens:
            if queen.get_player() == player:
                output.append(queen)
        return output


    # Temporary method for testing purposes
    def print(self):
        for row in range(0, len(self.__board)):
            row_output = ""
            for column in range(0, len(self.__board)):
                current_tile = self.get_tile(row, column)
                row_output += ("X" if current_tile is None else ("B" if current_tile.get_player() == 1 else "W")) + "   "
            print(row_output)


    def __initialize_empty_board(self, board_size):
        self.__board = [[None for columns in range(board_size)] for rows in range(board_size)]


    def __place_queens_for_player(self, board_size, player):
        step = 2
        start_column = 1
        row_range = range(0, 2) if player == 1 else range(board_size - 2, board_size)
        for row in row_range:
            for column in range(start_column, board_size, step):
                queen = Queen.Queen(row, column, player)
                self.set_tile(row, column, queen)
                self.__queens.append(queen)
            start_column = 0
