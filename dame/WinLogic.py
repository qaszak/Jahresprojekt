class WinLogic:

    __board = None
    __dame_logic = None
    __ai_player = -1
    __human_player = -1

    def __init__(self, board, dame_logic, ai_player, human_player):
        self.__board = board
        self.__dame_logic = dame_logic
        self.__ai_player = ai_player
        self.__human_player = human_player


    # public method
    def get_winner(self):
        winner = ""
        if self.__is_player_on_opponents_baseline(self.__ai_player) or \
           self.__is_player_out_of_queens(self.__human_player) or \
           self.__is_player_out_of_moves(self.__human_player):
            winner = self.__ai_player

        if self.__is_player_on_opponents_baseline(self.__human_player) or \
           self.__is_player_out_of_queens(self.__ai_player) or \
           self.__is_player_out_of_moves(self.__ai_player):
            winner = self.__human_player

        return winner


    # private methods
    def __is_player_on_opponents_baseline(self, player):
        result = False
        for queen in self.__board.get_queens_for(player):
            if queen.get_row() == self.__get_opponents_baseline_index(player):
                result = True
                break
        return result


    def __get_opponents_baseline_index(self, player):
        return 0 if player == self.__human_player else self.__board.get_size() - 1


    def __is_player_out_of_queens(self, player):
        return len(self.__board.get_queens_for(player)) == 0


    def __is_player_out_of_moves(self, player):
        CHECK_FOR_PLAYER_TURN = False
        result = True
        for queen in self.__board.get_queens_for(player):
            moves = self.__dame_logic.get_possible_moves_for(queen.get_row(), queen.get_column(), CHECK_FOR_PLAYER_TURN)
            if len(moves) > 0:
                result = False
                break
        return result