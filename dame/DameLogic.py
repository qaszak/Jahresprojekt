import InternalDameBoard
import ExternalDameBoard
import Queen
import MovementLogic
import WinLogic
import Move


class DameLogic:

    __board = None
    __movement_logic = None
    __win_logic = None

    __BOARD_SIZE = 6
    __AI_PLAYER = 1
    __HUMAN_PLAYER = 2
    __PLAYER_FIRST_MOVE = 2
    __NAME_AI_PLAYER = "Computer"
    __NAME_HUMAN_PLAYER = "Player"
    __AI_QUEEN_CHARACTER = "B"
    __HUMAN_QUEEN_CHARACTER = "W"
    __EMPTY_TILE_CHARACTER = " "
    __START_BOARD = [[__EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER],
                     [__AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __AI_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER],
                     [__EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER],
                     [__EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER, __EMPTY_TILE_CHARACTER],
                     [__EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER],
                     [__HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER, __HUMAN_QUEEN_CHARACTER, __EMPTY_TILE_CHARACTER]]


    def __init__(self):
        self.__initialize_board(self.__START_BOARD)


    # public methods
    def get_possible_moves_for(self, row, column, check_possible_in_turn = True):
        moves = []
        queen = self.__get_queen_at(row, column)
        if queen is not None:
            if (not check_possible_in_turn) or (check_possible_in_turn and self.__is_players_turn(queen)):
                moves = self.__movement_logic.get_moves_for(queen, check_possible_in_turn)
        return moves


    def get_winner(self):
        winner = self.__win_logic.get_winner()
        return self.__get_player_name(winner)


    def get_external_board(self):
        board = self.__board.get_board_representation(self.__EMPTY_TILE_CHARACTER)
        score = self.__board.get_score()
        name_player_turn = self.__get_player_name(self.__board.get_player_turn())
        character_player_turn = self.__get_player_character(self.__board.get_player_turn())
        number_of_queens_ai = len(self.__board.get_queens_for(self.__AI_PLAYER))
        number_of_queens_human = len(self.__board.get_queens_for(self.__HUMAN_PLAYER))
        return ExternalDameBoard.ExternalDameBoard(board, score, self.__NAME_AI_PLAYER, self.__NAME_HUMAN_PLAYER,
                                                   name_player_turn, character_player_turn, number_of_queens_ai,
                                                   number_of_queens_human, self.__AI_QUEEN_CHARACTER,
                                                   self.__HUMAN_QUEEN_CHARACTER, self.__EMPTY_TILE_CHARACTER)


    def execute_move(self, move):
        hit_queen = self.__movement_logic.get_hit_queen(move)
        if hit_queen is None:
            self.__board.execute_move(move)
            self.__board.close_turn()
            self.__switch_player_turn()
        else:
            self.__board.update_turn(move)
            self.__board.execute_move(move)
            self.__board.remove_queen(hit_queen)
            if self.__is_human_move(move):
                self.__board.increment_score_by(10)
            if len(self.__movement_logic.get_moves_for(move.get_queen())) == 0:
                self.__board.close_turn()
                self.__switch_player_turn()



    # private methods
    def __initialize_board(self, board):
        self.__board = InternalDameBoard.InternalDameBoard(board, self.__AI_PLAYER, self.__HUMAN_PLAYER,
                                                           self.__AI_QUEEN_CHARACTER, self.__HUMAN_QUEEN_CHARACTER,
                                                           self.__EMPTY_TILE_CHARACTER, self.__PLAYER_FIRST_MOVE)
        self.__movement_logic = MovementLogic.MovementLogic(self.__board, self.__AI_PLAYER, self.__HUMAN_PLAYER)
        self.__win_logic = WinLogic.WinLogic(self.__board, self, self.__AI_PLAYER, self.__HUMAN_PLAYER)


    def __is_human_move(self, move):
        return move.get_queen().get_player() == self.__HUMAN_PLAYER


    def __get_player_character(self, player):
        return self.__AI_QUEEN_CHARACTER if player == self.__AI_PLAYER else self.__HUMAN_QUEEN_CHARACTER


    def __get_player_name(self, player):
        output = ""
        if player == self.__AI_PLAYER:
            output = self.__NAME_AI_PLAYER
        elif player == self.__HUMAN_PLAYER:
            output = self.__NAME_HUMAN_PLAYER
        return output


    def __get_queen_at(self, row, column):
        return self.__board.get_tile(row, column)


    def __is_players_turn(self, queen):
        return self.__board.get_player_turn() == queen.get_player()


    def __switch_player_turn(self):
        if self.__board.get_player_turn() == self.__AI_PLAYER:
            self.__board.set_player_turn(self.__HUMAN_PLAYER)
        else:
            self.__board.set_player_turn(self.__AI_PLAYER)


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
        

