class WinLogic:

    __dame_logic = None
    __ai_player = -1
    __human_player = -1

    def __init__(self, dame_logic, ai_player, human_player):
        self.__dame_logic = dame_logic
        self.__ai_player = ai_player
        self.__human_player = human_player


    # public method
    def get_winner(self, board):
        winner = -1
        if self.__is_player_on_opponents_baseline(board, self.__ai_player) or \
           self.__is_player_out_of_queens(board, self.__human_player) or \
           self.__is_player_out_of_moves(board, self.__human_player):
                winner = self.__ai_player
        elif self.__is_player_on_opponents_baseline(board, self.__human_player) or \
             self.__is_player_out_of_queens(board, self.__ai_player) or \
             self.__is_player_out_of_moves(board, self.__ai_player):
                winner = self.__human_player
        return winner


    # private methods
    def __is_player_on_opponents_baseline(self, board, player):
        result = False
        for queen in board.get_queens_for(player):
            if queen.get_row() == self.get_opponents_baseline_index(board, player):
                result = True
                break
        return result


    def get_opponents_baseline_index(self, board, player):
        return 0 if player == self.__human_player else board.get_size() - 1


    def __is_player_out_of_queens(self, board, player):
        return len(board.get_queens_for(player)) == 0


    def __is_player_out_of_moves(self, board, player):
        CHECK_FOR_PLAYER_TURN = False
        result = True
        for queen in board.get_queens_for(player):
            moves = self.__dame_logic.get_possible_moves_for(queen.get_row(), queen.get_column(), board, CHECK_FOR_PLAYER_TURN)
            if len(moves) > 0:
                result = False
                break
        return result



    ################### UNCOMMENT TO RUN TESTCASES.PY #######################

    """"
    
    
    def is_player_on_opponents_baseline(self, player):
        return self.__is_player_on_opponents_baseline(player)

    def is_player_out_of_queens(self, player):
        return self.__is_player_out_of_queens(player)

    def is_player_out_of_moves(self, player):
        return self.__is_player_out_of_moves(player)
        
        
    """
