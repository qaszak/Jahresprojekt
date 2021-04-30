import Queen
import Move
import ExternalDameBoard

class DameBoard:

    __board = [[]]
    __queens = []
    __score = 0
    __player_turn = -1

    def __init__(self, board, player_first_move):
        self.__board = board
        self.__player_turn = player_first_move
        self.__initialize_queen_collection()


    def __set_tile(self, row, column, value):
        self.__board[column][row] = value


    def __set_player_turn(self, player):
        self.__player_turn = player


    def increment_score_by(self, points):
        self.__score += points


    def get_tile(self, row, column):
        return self.__board[column][row]


    def get_size(self):
        return len(self.__board)


    def get_score(self):
        return self.__score


    def get_player_turn(self):
        return self.__player_turn


    def get_queens_for(self, player):
        output = []
        for queen in self.__queens:
            if queen.get_player() == player:
                output.append(queen)
        return output


    def get_board_representation(self, board, empty_tile_character):
        output = board
        for row in range(0, self.get_size()):
            for column in range(0, self.get_size()):
                queen = self.get_tile(row, column)
                content_representation = empty_tile_character if queen is None else queen.get_character()
                output[column][row] = content_representation
        return output


    def execute_move(self, move):
        queen = move.get_queen()
        self.__set_tile(queen.get_row(), queen.get_column(), None)
        self.__set_tile(move.get_row(), move.get_column(), queen)
        queen.set_position(move.get_row(), move.get_column())


    def remove_queen(self, queen):
        self.__set_tile(queen.get_row(), queen.get_column(), None)
        self.__queens.remove(queen)


    def __initialize_queen_collection(self):
        for row in range(0, self.get_size()):
            for column in range(0, self.get_size()):
                queen = self.get_tile(row, column)
                if queen is not None:
                    self.__queens.append(queen)
