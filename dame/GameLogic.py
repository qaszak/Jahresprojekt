import DameBoard
import Queen
import Move

class GameLogic:
    # ToDos:
    # - implement as a singleton
    # - implement methods

    __board = None
    __move = None

    # public methods
    def set_move(self, board, move):
        self.__board = board
        self.__move = move


    def is_queen_at(self, board, row, column):
        return board.get_tile(row, column) is not None


    def is_players_turn(self, player):
        return self.__move.get_queen().get_player() == player


    # new
    def get_possible_moves_for(self, player, queen, board):
        moves = []
        for move in self.__get_potential_moves_for(queen):
            self.set_move(board, move)
            if self.__is_move_valid(player):
                moves.append(move)
        return moves

    # new
    def __get_potential_moves_for(self, queen):
        moves = []
        prefixes = [-1, 1]
        for prefix_1 in prefixes:
            for prefix_2 in prefixes:
                for step in [1, 2]:
                    move = Move.Move(queen, queen.get_row() + prefix_1 * step, queen.get_column() + prefix_2 * step)
                    moves.append(move)
        return moves

    # new
    def __is_move_valid(self, player):
        return self.is_players_turn(player) and \
               self.__is_move_in_board() and \
               self.__is_direction_valid() and \
               not self.__is_move_blocked_by_queen() and \
               (self.__is_standard_move() or self.is_hitting_move())


    def __is_move_in_board(self):
        index_range = range(0, self.__board.get_size())
        valid_row_destination = self.__move.get_row() in index_range
        valid_column_destination = self.__move.get_column() in index_range
        return valid_row_destination and valid_column_destination


    def __is_direction_valid(self):
        return self.__is_row_direction_valid() and self.__is_column_direction_valid()


    def __is_row_direction_valid(self):
        player = self.__move.get_queen().get_player()
        distance_rows = self.__move.get_row() - self.__move.get_queen().get_row()
        if player == 1:
            return distance_rows in [1, 2]      # valid downward move?
        elif player == 2:
            return distance_rows in [-1, -2]    # valid upward move?


    def __is_column_direction_valid(self):
        distance_columns = self.__move.get_column() - self.__move.get_queen().get_column()
        valid_left_move = distance_columns in [-1, -2]
        valid_right_move = distance_columns in [1, 2]
        return valid_left_move or valid_right_move


    def __is_move_blocked_by_queen(self):
        content_destination_tile = self.__board.get_tile(self.__move.get_row(), self.__move.get_column())
        return content_destination_tile is not None

    # new
    def __is_standard_move(self):
        distance_columns = self.__move.get_column() - self.__move.get_queen().get_column()
        return distance_columns in [-1, 1]

    # new
    def is_hitting_move(self):
        return self.get_hit_queen() is not None

    # new
    def get_hit_queen(self):
        hit_queen = None
        distance_rows = self.__move.get_row() - self.__move.get_queen().get_row()
        distance_columns = self.__move.get_column() - self.__move.get_queen().get_column()
        if distance_rows in [-2, 2] and distance_columns in [-2, 2]:
            hit_row = (1 if distance_rows == 2 else - 1) + self.__move.get_queen().get_row()
            hit_column = (1 if distance_columns == 2 else -1) + self.__move.get_queen().get_column()
            hit_queen = self.__board.get_tile(hit_row, hit_column)
            if (hit_queen is None) or (hit_queen.get_player() == self.__move.get_queen().get_player()):
                hit_queen = None
        return hit_queen


###################### FUNCTIONS FOR TESTCASES.PY (UNCOMMENT TO RUN TESTCASES) ####################################

    """
    def get_potential_moves_for(self, queen):
        return self.__get_potential_moves_for(queen)

    def is_move_valid(self):
        return self.__is_move_valid()
    
    def is_move_in_board(self):
        return self.__is_move_in_board()

    def is_direction_valid(self):
        return self.__is_direction_valid()

    def is_row_direction_valid(self):
        return self.__is_row_direction_valid()

    def is_column_direction_valid(self):
        return self.__is_column_direction_valid()

    def is_move_blocked_by_queen(self):
        return self.__is_move_blocked_by_queen()

    def is_standard_move(self):
        return self.__is_standard_move()

    """