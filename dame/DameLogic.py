import InternalDameBoard
import ExternalDameBoard
import Queen
import MinimaxTreeNode
import BoardEvaluationLogic
import MovementLogic
import WinLogic
import Move
import time


class DameLogic:

    __dame = None
    __difficulty = -1
    __board = None
    __evaluation_logic = None
    __movement_logic = None
    __win_logic = None
    __BOARD_SIZE = 6
    __AI_PLAYER = 1
    __HUMAN_PLAYER = 2
    __PLAYER_FIRST_MOVE = 2
    # __PLAYER_FIRST_MOVE = 1
    __NAME_AI_PLAYER = "Computer"
    __NAME_HUMAN_PLAYER = "Player"
    __AI_QUEEN_CHARACTER = "B"
    __HUMAN_QUEEN_CHARACTER = "W"
    __EMPTY_TILE_CHARACTER = " "
    __DELAY_KI_REACTION_IN_SECONDS = 1
    __START_BOARD = [[__EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER],
                     [__AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER],
                     [__EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER],
                     [__EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER],
                     [__EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER],
                     [__HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER]]


    def __init__(self, dame, difficulty):
        self.__dame = dame
        self.__difficulty = difficulty
        self.__initialize_board(self.__START_BOARD)


    # TEMPORARY - DELETE LATER
    def get_board(self):
        return self.__board


    # public methods
    def get_possible_moves_for(self, row, column, board=None, check_possible_in_turn = True):
        moves = []
        if board is None:
            board = self.__board
        queen = board.get_tile(row, column)
        if queen is not None:
            if (not check_possible_in_turn) or (check_possible_in_turn and self.__is_players_turn(queen, board)):
                moves = self.__movement_logic.get_moves_for(board, queen, check_possible_in_turn)
        return moves


    def get_hitting_moves_for_player(self, board, player):
        return self.__movement_logic.get_hitting_moves_for_player(board, player)


    def evaluate_board(self, board, player):
        return self.__evaluation_logic.evaluate(board, player)


    def is_game_over(self, board=None):
        if board is None:
            board = self.__board
        return self.get_winner(board) != -1


    def get_winner(self, board=None):
        if board is None:
            board = self.__board
        return self.__win_logic.get_winner(board)


    def get_external_board(self, board=None):
        if board is None:
            board = self.__board
        board_representation = board.get_board_representation(self.__EMPTY_TILE_CHARACTER)
        score = board.get_score()
        name_player_turn = self.get_player_name(board.get_player_turn())
        character_player_turn = self.__get_player_character(board.get_player_turn())
        number_of_queens_ai = len(board.get_queens_for(self.__AI_PLAYER))
        number_of_queens_human = len(board.get_queens_for(self.__HUMAN_PLAYER))
        return ExternalDameBoard.ExternalDameBoard(board_representation, score, self.__NAME_AI_PLAYER, self.__NAME_HUMAN_PLAYER,
                                                   name_player_turn, character_player_turn, number_of_queens_ai,
                                                   number_of_queens_human, self.__AI_QUEEN_CHARACTER,
                                                   self.__HUMAN_QUEEN_CHARACTER, self.__EMPTY_TILE_CHARACTER)


    def process_human_move(self, move):
        self.execute_move(move)
        self.__dame.send_external_board(self.get_external_board())
        while self.__board.get_player_turn() == self.__AI_PLAYER:
            self.__execute_ki_move()
            time.sleep(self.__DELAY_KI_REACTION_IN_SECONDS)
            self.__dame.send_external_board(self.get_external_board())


    def execute_move(self, move, board=None):
        if board is None:
            board = self.__board
        hit_queen = self.__movement_logic.get_hit_queen(board, move)
        if hit_queen is None:
            board.execute_move(move)
            board.close_turn()
            self.__switch_player_turn(board)
        else:
            board.update_turn(move)
            board.execute_move(move)
            board.remove_queen(hit_queen)
            if self.__is_human_move(move):
                board.increment_score_by(10)
            if len(self.__movement_logic.get_moves_for(board, move.get_queen())) == 0:
                board.close_turn()
                self.__switch_player_turn(board)


    def __execute_ki_move(self):
        if self.__board.get_player_turn() == self.__AI_PLAYER:
            minimax = MinimaxTreeNode.MinimaxTreeNode(self, self.__AI_PLAYER, self.__board, None, self.__HUMAN_PLAYER, self.__difficulty)
            best_ki_move = minimax.get_best_move()
            best_ki_move = self.__cast_ki_move_to_board(best_ki_move)
            self.execute_move(best_ki_move)


    def get_opponent(self, player):
        return self.__HUMAN_PLAYER if player == self.__AI_PLAYER else self.__AI_PLAYER


    def get_opponents_baseline_index(self, board, player):
        return self.__win_logic.get_opponents_baseline_index(board, player)


    # private methods
    def __initialize_board(self, board):
        PARSE_BOARD = True
        IN_TURN_PREVIOUSLY_MOVED_QUEEN = None
        self.__board = InternalDameBoard.InternalDameBoard(board, PARSE_BOARD, IN_TURN_PREVIOUSLY_MOVED_QUEEN,
                                                           self.__PLAYER_FIRST_MOVE, self.__AI_PLAYER, self.__HUMAN_PLAYER,
                                                           self.__AI_QUEEN_CHARACTER, self.__HUMAN_QUEEN_CHARACTER,
                                                           self.__EMPTY_TILE_CHARACTER,)
        self.__evaluation_logic = BoardEvaluationLogic.BoardEvaluationLogic(self)
        self.__movement_logic = MovementLogic.MovementLogic(self.__AI_PLAYER, self.__HUMAN_PLAYER)
        self.__win_logic = WinLogic.WinLogic(self, self.__AI_PLAYER, self.__HUMAN_PLAYER)


    def __is_human_move(self, move):
        return move.get_queen().get_player() == self.__HUMAN_PLAYER


    def __get_player_character(self, player):
        return self.__AI_QUEEN_CHARACTER if player == self.__AI_PLAYER else self.__HUMAN_QUEEN_CHARACTER


    def get_player_name(self, player):
        output = ""
        if player == self.__AI_PLAYER:
            output = self.__NAME_AI_PLAYER
        elif player == self.__HUMAN_PLAYER:
            output = self.__NAME_HUMAN_PLAYER
        return output


    def __get_queen_at(self, row, column):
        return self.__board.get_tile(row, column)


    def __is_players_turn(self, queen, board=None):
        if board is None:
            board = self.__board
        return board.get_player_turn() == queen.get_player()


    def __switch_player_turn(self, board):
        if board.get_player_turn() == self.__AI_PLAYER:
            board.set_player_turn(self.__HUMAN_PLAYER)
        else:
            board.set_player_turn(self.__AI_PLAYER)


    def __cast_ki_move_to_board(self, move):
        queen_ki_board = move.get_queen()
        queen_original_board = self.__get_queen_at(queen_ki_board.get_row(), queen_ki_board.get_column())
        return Move.Move(queen_original_board, move.get_row(), move.get_column())



    ################### UNCOMMENT TO RUN TESTCASES.PY #######################
    
    """"
    
    def load_custom_board(self, board):
        self.__initialize_board(board)

    def get_win_logic(self):
        return self.__win_logic

    def get_movement_logic(self):
        return self.__movement_logic

    def get_ai_player(self):
        return self.__AI_PLAYER

    def get_human_player(self):
        return self.__HUMAN_PLAYER

    def get_ai_character(self):
        return self.__AI_QUEEN_CHARACTER

    def get_human_character(self):
        return self.__HUMAN_QUEEN_CHARACTER

    def get_empty_tile_character(self):
        return self.__EMPTY_TILE_CHARACTER

    def create_moves(self, move_collection):
        output = []
        for entry in move_collection:
            start_row = entry[0]
            start_column = entry[1]
            destination_row = entry[2]
            destination_column = entry[3]
            queen = self.__board.get_tile(start_row, start_column)
            output.append(Move.Move(queen, destination_row, destination_column))
        return output
        
    """
        

