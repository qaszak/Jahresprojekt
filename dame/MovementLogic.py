import Move

class MovementLogic:

    __board = None
    __ai_player = -1
    __human_player = -1

    def __init__(self, board, ai_player, human_player):
        self.__board = board
        self.__ai_player = ai_player
        self.__human_player = human_player


    #public methods
    def get_moves_for(self, queen, check_possible_in_turn = True):
        moves = []
        if not check_possible_in_turn:
            moves = self.__get_possible_moves_for(queen)
        elif self.__is_new_turn() or self.__is_already_moved_in_turn(queen):
            hitting_moves = self.__get_hitting_moves_for_player(queen)
            if self.__is_already_moved_in_turn(queen) or len(hitting_moves) > 0:
                moves = self.__select_hitting_moves_for_queen_from(hitting_moves, queen)
            else:
                moves = self.__get_possible_moves_for(queen)
        return moves


    def get_hit_queen(self, move):
        hit_queen = None
        distance_rows = self.__calculate_row_distance(move)
        distance_columns = self.__calculate_column_distance(move)
        if distance_rows in [-2, 2] and distance_columns in [-2, 2]:
            hit_row = (1 if distance_rows == 2 else - 1) + move.get_queen().get_row()
            hit_column = (1 if distance_columns == 2 else -1) + move.get_queen().get_column()
            hit_queen = self.__board.get_tile(hit_row, hit_column)
            if (hit_queen is None) or (hit_queen.get_player() == move.get_queen().get_player()):
                hit_queen = None
        return hit_queen


    # private methods
    def __is_already_moved_in_turn(self, queen):
        return self.__board.get_in_turn_previously_moved_queen() == queen


    def __is_new_turn(self):
        return self.__board.get_in_turn_previously_moved_queen() is None


    def __get_hitting_moves_for_player(self, queen):
        hitting_moves = []
        for queen in self.__board.get_queens_for(queen.get_player()):
            for move in self.__get_possible_moves_for(queen):
                if self.__is_hitting_move(move):
                    hitting_moves.append(move)
        return hitting_moves


    def __select_hitting_moves_for_queen_from(self, hitting_moves, queen):
        moves = []
        for move in hitting_moves:
            if move.get_queen() == queen:
                moves.append(move)
        return moves


    def __get_possible_moves_for(self, queen):
        moves = []
        for move in self.__get_potential_moves_for(queen):
            if self.__is_move_valid(move):
                moves.append(move)
        return moves


    def __get_potential_moves_for(self, queen):
        moves = []
        prefixes = [-1, 1]
        for prefix_1 in prefixes:
            for prefix_2 in prefixes:
                for step in [1, 2]:
                    move = Move.Move(queen, queen.get_row() + prefix_1 * step, queen.get_column() + prefix_2 * step)
                    moves.append(move)
        return moves


    def __is_move_valid(self, move):
        return self.__is_move_in_board(move) and \
               self.__is_row_direction_valid(move) and \
               not self.__is_move_blocked_by_queen(move) and \
               (self.__is_non_hitting_move(move) or self.__is_hitting_move(move))


    def __is_move_in_board(self, move):
        index_range = range(0, self.__board.get_size())
        valid_row_destination = move.get_row() in index_range
        valid_column_destination = move.get_column() in index_range
        return valid_row_destination and valid_column_destination


    def __is_row_direction_valid(self, move):
        player = move.get_queen().get_player()
        distance_rows = self.__calculate_row_distance(move)
        if player == self.__ai_player:
            return distance_rows in [1, 2]      # valid downward move?
        elif player == self.__human_player:
            return distance_rows in [-1, -2]    # valid upward move?


    def __is_move_blocked_by_queen(self, move):
        content_destination_tile = self.__board.get_tile(move.get_row(), move.get_column())
        return content_destination_tile is not None


    def __is_non_hitting_move(self, move):
        distance_columns = self.__calculate_column_distance(move)
        return distance_columns in [-1, 1]


    def __is_hitting_move(self, move):
        return self.get_hit_queen(move) is not None


    def __calculate_row_distance(self, move):
        return move.get_row() - move.get_queen().get_row()


    def __calculate_column_distance(self, move):
        return move.get_column() - move.get_queen().get_column()