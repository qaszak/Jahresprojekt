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

    def __init__(self):
        board = self.__initialize_empty_board(self.__BOARD_SIZE)
        self.__place_queens_for_player(self.__AI_PLAYER, board)
        self.__place_queens_for_player(self.__HUMAN_PLAYER, board)
        self.__board = InternalDameBoard.InternalDameBoard(board, self.__PLAYER_FIRST_MOVE)
        self.__movement_logic = MovementLogic.MovementLogic(self.__board, self.__AI_PLAYER, self.__HUMAN_PLAYER)
        self.__win_logic = WinLogic.WinLogic(self.__board, self, self.__AI_PLAYER, self.__HUMAN_PLAYER)


    # public methods
    def get_possible_moves_for(self, row, column, check_possible_in_turn = True):
        moves = []
        if self.__is_queen_at(row, column):
            queen = self.__get_queen_at(row, column)
            if (not check_possible_in_turn) or (check_possible_in_turn and self.__is_players_turn(queen)):
                moves = self.__movement_logic.get_moves_for(queen, check_possible_in_turn)
        return moves


    def get_winner(self):
        winner = self.__win_logic.get_winner()
        return self.__get_player_name(winner)


    def get_external_board(self):
        empty_board = self.__initialize_empty_board(self.__BOARD_SIZE)
        board = self.__board.get_board_representation(empty_board, self.__EMPTY_TILE_CHARACTER)
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


    # private methods
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


    def __is_queen_at(self, row, column):
        return self.__board.get_tile(row, column) is not None


    def __is_players_turn(self, queen):
        return self.__board.get_player_turn() == queen.get_player()


    def __initialize_empty_board(self, board_size):
        return [[None for columns in range(board_size)] for rows in range(board_size)]


    def __place_queens_for_player(self, player, board):
        step = 2
        start_column = 1
        player_character = self.__get_player_character(player)
        row_range = range(0, 2) if player == self.__AI_PLAYER else range(self.__BOARD_SIZE - 2, self.__BOARD_SIZE)
        for row in row_range:
            for column in range(start_column, self.__BOARD_SIZE, step):
                board[column][row] = Queen.Queen(row, column, player, player_character)
            start_column = 0


    def __switch_player_turn(self):
        if self.__board.get_player_turn() == self.__AI_PLAYER:
            self.__board.set_player_turn(self.__HUMAN_PLAYER)
        else:
            self.__board.set_player_turn(self.__AI_PLAYER)


    ################### UNCOMMENT TO RUN TESTCASES.PY #######################

    def get_custom_board(self, board, player_first_move=2):
        size_board = len(board)
        custom_board = self.__initialize_empty_board(size_board)
        for row in size_board:
            for column in size_board
                element = board[column][row]
                read_element = None
                if element == self.__AI_QUEEN_CHARACTER:
                    read_element = Queen.Queen(row, column, self.__AI_PLAYER, element)
                elif element == self.__HUMAN_QUEEN_CHARACTER:
                    read_element = Queen.Queen(row, column, self.__HUMAN_PLAYER, element)
                custom_board[column][row] = read_element
        return InternalDameBoard.InternalDameBoard(custom_board, player_first_move)
