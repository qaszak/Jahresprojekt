class BoardEvaluationLogic:

    __dame_logic = None

    def __init__(self, dame_logic):
        self.__dame_logic = dame_logic

    # public method
    def evaluate(self, board, player):
        score = 0
        if self.__is_game_won(board, player):
            score = 1000
        elif self.__is_game_lost(board, player):
            score = -1000
        else:
            score += self.__evaluate_queen_count_difference(board, player)
            score += self.__evaluate_possible_move_count_difference(board, player)
            score += self.__evaluate_possible_hitting_move_count_difference(board, player) * 2
            score += self.__evaluate_closest_distance_to_opponents_baseline_difference(board, player)
        return score


    # private methods
    def __is_game_won(self, board, player):
        return self.__dame_logic.get_winner(board) == player


    def __is_game_lost(self, board, player):
        return self.__dame_logic.get_winner(board) == self.__get_opponent(player)


    def __evaluate_queen_count_difference(self, board, player):
        player_queen_count = len(board.get_queens_for(player))
        opponent_queen_count = len(board.get_queens_for(self.__get_opponent(player)))
        return player_queen_count - opponent_queen_count


    def __evaluate_possible_move_count_difference(self, board, player):
        player_move_count = self.__calculate_possible_move_count_for(board, player)
        opponent_move_count = self.__calculate_possible_move_count_for(board, self.__get_opponent(player))
        return player_move_count - opponent_move_count


    def __evaluate_possible_hitting_move_count_difference(self, board, player):
        player_hitting_move_count = self.__calculate_possible_hitting_move_count_for(board, player)
        opponent_hitting_move_count = self.__calculate_possible_hitting_move_count_for(board, self.__get_opponent(player))
        return player_hitting_move_count - opponent_hitting_move_count


    def __evaluate_closest_distance_to_opponents_baseline_difference(self, board, player):
        player_closest_distance = self.__calculate_closest_distance_to_opponents_baseline_for(board, player)
        opponent_closest_distance = self.__calculate_closest_distance_to_opponents_baseline_for(board, self.__get_opponent(player))
        return opponent_closest_distance - player_closest_distance


    def __get_opponent(self, player):
        return self.__dame_logic.get_opponent(player)


    def __calculate_possible_move_count_for(self, board, player):
        CHECK_POSSIBLE_IN_TURN = False
        count = 0
        for queen in board.get_queens_for(player):
            moves = self.__dame_logic.get_possible_moves_for(queen.get_row(), queen.get_column(), board, CHECK_POSSIBLE_IN_TURN)
            count += len(moves)
        return count


    def __calculate_possible_hitting_move_count_for(self, board, player):
        count = 0
        for queen in board.get_queens_for(player):
            moves = self.__dame_logic.get_hitting_moves_for_player(board, player)
            count += len(moves)
        return count


    def __calculate_closest_distance_to_opponents_baseline_for(self, board, player):
        index_opponents_baseline = self.__dame_logic.get_opponents_baseline_index(board, player)
        min_distance = board.get_size() - 1
        for queen in board.get_queens_for(player):
            distance = abs(queen.get_row() - index_opponents_baseline)
            if distance < min_distance:
                min_distance = distance
        return min_distance


