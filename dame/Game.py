import DameBoard
import GameLogic
import Move

class Game:
    __internal_board = None
    game_logic = None
    __player_turn = -1

    def __init__(self, board_size):
        self.__internal_board = DameBoard.DameBoard(board_size)
        self.game_logic = GameLogic.GameLogic()
        self.__player_turn = 2

    def start(self, board_size):
        print()

    def move_queen_to(self, current_row, current_column, destination_row, destination_column):
        move = self.__create_move_object(current_row, current_column, destination_row, destination_column)
        self.game_logic.set_move(self.__internal_board, move)
        # self.__game_logic.print_logic_checks(self.__player_turn)

    def print_board(self):
        self.__internal_board.print()

    # private methods
    def __create_move_object(self, current_row, current_column, destination_row, destination_column):
        queen = self.__internal_board.get_tile(current_row, current_column)
        return Move.Move(queen, destination_row, destination_column)



