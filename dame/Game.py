import DameBoard
import GameLogic

class Game:
    __internal_board = None
    __selected_queen = None
    __game_logic = None
    __player_turn = -1

    def __init__(self, board_size):
        self.__internal_board = DameBoard.DameBoard(board_size)
        # self.__game_logic = ...
        self.__player_turn = 2


    def start(self, board_size):
        pass

    def select_queen(self):
        pass

    def move_selected_queen(self, x, y):
        pass

    def print_board(self):
        self.__internal_board.print()



