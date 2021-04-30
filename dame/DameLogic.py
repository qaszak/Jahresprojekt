import InternalDameBoard
import ExternalDameBoard
import Queen
import Move


class DameLogic:

    __board = None
    __BOARD_SIZE = 6
    __AI_PLAYER = 1
    __HUMAN_PLAYER = 2
    __PLAYER_FIRST_MOVE = 2
    __NAME_AI_PLAYER = "Computer"
    __NAME_HUMAN_PLAYER = "Player"
    __AI_QUEEN_CHARACTER = "B"
    __HUMAN_QUEEN_CHARACTER = "W"
    __EMPTY_TILE_CHARACTER = " "


    def __init__(self):
        board = self.__initialize_empty_board(self.__BOARD_SIZE)
        self.__place_queens_for_player(self.__AI_PLAYER, board)
        self.__place_queens_for_player(self.__HUMAN_PLAYER, board)
        self.__board = InternalDameBoard.InternalDameBoard(board, self.__PLAYER_FIRST_MOVE)


    # public methods

    def get_possible_moves_for(self, row, column):
        moves = []
        if self.__is_queen_at(row, column):
            queen = self.__get_queen_at(row, column)
            if self.__is_players_turn(queen):
                for move in self.__get_potential_moves_for(queen):
                    if self.__is_move_valid(move):
                        moves.append(move)
        return moves


    def execute_move(self, move):
        hit_queen = self.__get_hit_queen(move)
        if hit_queen is None:
            self.__switch_player_turn()
        else:
            self.__board.remove_queen(hit_queen)
            self.__board.increment_score_by(10)
        self.__board.execute_move(move)


    def get_winner(self):
        if self.__is_player_on_opponents_baseline(self.__AI_PLAYER) or \
                self.__is_player_out_of_queens(self.__HUMAN_PLAYER) or \
                self.__is_player_out_of_moves(self.__HUMAN_PLAYER):
            winner = self.__NAME_AI_PLAYER
        elif self.__is_player_on_opponents_baseline(self.__HUMAN_PLAYER) or \
                self.__is_player_out_of_queens(self.__AI_PLAYER) or \
                self.__is_player_out_of_moves(self.__AI_PLAYER):
            winner = self.__NAME_HUMAN_PLAYER
        else:
            winner = ""
        return winner


    def get_external_board(self):
        empty_board = self.__initialize_empty_board(self.__BOARD_SIZE)
        board = self.__board.get_board_representation(empty_board, self.__EMPTY_TILE_CHARACTER)
        score = self.__board.get_score()
        player_turn = self.__get_player_character(self.__board.get_player_turn())
        number_of_queens_ai = len(self.__board.get_queens_for(self.__AI_PLAYER))
        number_of_queens_human = len(self.__board.get_queens_for(self.__HUMAN_PLAYER))
        return ExternalDameBoard.ExternalDameBoard(board, score, self.__NAME_AI_PLAYER, self.__NAME_HUMAN_PLAYER,
                                                   player_turn, number_of_queens_ai, number_of_queens_human,
                                                   self.__AI_QUEEN_CHARACTER, self.__HUMAN_QUEEN_CHARACTER,
                                                   self.__EMPTY_TILE_CHARACTER)


    # private helpers for __init__
    def __initialize_empty_board(self, board_size):
        return [[None for columns in range(board_size)] for rows in range(board_size)]


    def __place_queens_for_player(self, player, board):
        step = 2
        start_column = 1
        player_character = self.__get_player_character(player)
        # Test: HUMAN_PLAYER -> AI_PLAYER
        row_range = range(0, 2) if player == self.__AI_PLAYER else range(self.__BOARD_SIZE - 2, self.__BOARD_SIZE)
        for row in row_range:
            for column in range(start_column, self.__BOARD_SIZE, step):
                board[column][row] = Queen.Queen(row, column, player, player_character)
            start_column = 0


    def __get_player_character(self, player):
        return self.__AI_QUEEN_CHARACTER if player == self.__AI_PLAYER else self.__HUMAN_QUEEN_CHARACTER


    # private helpers for get_possible_moves_for()
    def __is_queen_at(self, row, column):
        return self.__board.get_tile(row, column) is not None


    def __get_queen_at(self, row, column):
        return self.__board.get_tile(row, column)


    def __is_players_turn(self, queen):
        return self.__board.get_player_turn() == queen.get_player()


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
        if player == self.__AI_PLAYER:
            return distance_rows in [1, 2]      # valid downward move?
        elif player == self.__HUMAN_PLAYER:
            return distance_rows in [-1, -2]    # valid upward move?


    def __is_move_blocked_by_queen(self, move):
        content_destination_tile = self.__board.get_tile(move.get_row(), move.get_column())
        return content_destination_tile is not None


    def __is_non_hitting_move(self, move):
        distance_columns = self.__calculate_column_distance(move)
        return distance_columns in [-1, 1]


    def __is_hitting_move(self, move):
        return self.__get_hit_queen(move) is not None


    def __get_hit_queen(self, move):
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


    def __calculate_row_distance(self, move):
       return move.get_row() - move.get_queen().get_row()


    def __calculate_column_distance(self, move):
        return move.get_column() - move.get_queen().get_column()


    # private helpers for execute_move()
    def __switch_player_turn(self):
        if self.__board.get_player_turn() == self.__AI_PLAYER:
            self.__board.set_player_turn(self.__HUMAN_PLAYER)
        else:
            self.__board.set_player_turn(self.__AI_PLAYER)


    # private helpers for get_winner()
    def __is_player_on_opponents_baseline(self, player):
        result = False
        for queen in self.__board.get_queens_for(player):
            if queen.get_row() == self.__get_opponents_baseline_index(player):
                result = True
                break
        return result


    def __get_opponents_baseline_index(self, player):
        return 0 if player == self.__HUMAN_PLAYER else self.__board.get_size() - 1


    def __is_player_out_of_queens(self, player):
        return len(self.__board.get_queens_for(player)) == 0


    def __is_player_out_of_moves(self, player):
        moves = []
        for queen in self.__board.get_queens_for(player):
            moves += self.get_possible_moves_for(queen.get_row(), queen.get_column())
        return len(moves) == 0