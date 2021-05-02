import Queen
import Move
import ExternalDameBoard

class InternalDameBoard:

    __board = [[]]
    __queens = []
    __score = 0
    __player_turn = -1
    __in_turn_previously_moved_queen = None

    def __init__(self, board, parse, in_turn_previously_moved_queen, player_first_move, ai_player="", human_player="",
                 ai_queen_character="", human_queen_character="", empty_tile_character=""):
        if parse:
            self.__parse_board(board, ai_player, human_player, ai_queen_character, human_queen_character, empty_tile_character)
        else:
            self.__board = board
        self.__initialize_queen_collection()
        self.__in_turn_previously_moved_queen = in_turn_previously_moved_queen
        self.__player_turn = player_first_move


    def clone(self):
        clone_in_turn_previously_moved_queen = None
        if self.__in_turn_previously_moved_queen is not None:
            clone_in_turn_previously_moved_queen = self.__in_turn_previously_moved_queen.clone()
        clone = InternalDameBoard(self.__get_clone_of_board(), False, clone_in_turn_previously_moved_queen, self.get_player_turn())
        clone.set_score(self.get_score())
        clone.set_player_turn(self.get_player_turn())
        return clone


    def set_player_turn(self, player):
        self.__player_turn = player


    def get_player_turn(self):
        return self.__player_turn


    def increment_score_by(self, points):
        self.__score += points


    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def get_tile(self, row, column):
        return self.__board[row][column]


    def get_size(self):
        return len(self.__board)


    def get_in_turn_previously_moved_queen(self):
        return self.__in_turn_previously_moved_queen


    def get_queens_for(self, player):
        output = []
        for queen in self.__queens:
            if queen.get_player() == player:
                output.append(queen)
        return output


    def get_board_representation(self, empty_tile_character):
        board_range = range(0, self.get_size())
        output_board = [[None for columns in board_range] for rows in board_range]
        for row in board_range:
            for column in board_range:
                queen = self.get_tile(row, column)
                content_representation = empty_tile_character if queen is None else queen.get_character()
                output_board[row][column] = content_representation
        return output_board


    def execute_move(self, move):
        queen = move.get_queen()
        self.__set_tile(queen.get_row(), queen.get_column(), None)
        self.__set_tile(move.get_row(), move.get_column(), queen)
        queen.set_position(move.get_row(), move.get_column())


    def update_turn(self, move):
        self.__in_turn_previously_moved_queen = move.get_queen()


    def close_turn(self):
        self.__in_turn_previously_moved_queen = None


    def remove_queen(self, queen):
        self.__set_tile(queen.get_row(), queen.get_column(), None)
        self.__queens.remove(queen)


    # private methods
    def __set_tile(self, row, column, value):
        self.__board[row][column] = value


    def __parse_board(self, board, ai_player, human_player, ai_queen_character, human_queen_character, empty_tile_character):
        board_range = range(0, len(board))
        output_board = [[None for columns in board_range] for rows in board_range]
        for row in board_range:
            for column in board_range:
                board_element = board[row][column]
                if board_element == ai_queen_character:
                    queen = Queen.Queen(row, column, ai_player, ai_queen_character)
                elif board_element == human_queen_character:
                    queen = Queen.Queen(row, column, human_player, human_queen_character)
                elif board_element == empty_tile_character:
                    queen = None
                else:
                    queen = None
                output_board[row][column] = queen
        self.__board = output_board


    def __initialize_queen_collection(self):
        self.__queens = []
        for row in range(0, self.get_size()):
            for column in range(0, self.get_size()):
                queen = self.get_tile(row, column)
                if queen is not None:
                    self.__queens.append(queen)


    def __get_clone_of_board(self):
        board_range = range(0, len(self.__board))
        clone = [[None for columns in board_range] for rows in board_range]
        for row in board_range:
            for column in board_range:
                queen = self.get_tile(row, column)
                if queen is not None:
                    clone[row][column] = queen.clone()
        return clone
