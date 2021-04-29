import DameBoard
import DameLogic
import Move

class Dame:
    __internal_board = None
    game_logic = None
    __player_turn = -1
    __current_moves = []

    def __init__(self, board_size):
        self.__internal_board = DameBoard.DameBoard(board_size)
        self.game_logic = DameLogic.DameLogic()
        self.__player_turn = 2

################################# NEW ##################################

    def get_moves_for_queen_at(self, row, column):
        self.__current_moves = []
        if self.game_logic.is_queen_at(self.__internal_board, row, column):
            queen = self.__internal_board.get_tile(row, column)
            self.__current_moves = self.game_logic.get_possible_moves_for(self.__player_turn, queen, self.__internal_board)
        return self.__current_moves

    #  TEMPORARY FOR TESTING PURPOSES
    def print_possible_moves(self):
        output = "\tPossible moves: "
        for move in self.__current_moves:
            output += "(" + str(move.get_row()) + "," + str(move.get_column()) + "), "
        print(output)



    def execute_move(self, destination_row, destination_column):
        execution = False
        move = self.__get_selected_move(destination_row, destination_column)
        if move is not None:
            queen = move.get_queen()
            self.game_logic.set_move(self.__internal_board, move)
            hit_queen = self.game_logic.get_hit_queen()

            # Position queen on board
            self.__internal_board.set_tile(queen.get_row(), queen.get_column(), None)
            self.__internal_board.set_tile(move.get_row(), move.get_column(), queen)
            queen.set_position(move.get_row(), move.get_column())

            # Delete hit queen
            if hit_queen is not None:
                self.__internal_board.remove_queen(hit_queen)

            if self.__player_turn == 1:
                self.__player_turn = 2
            else:
                self.__player_turn = 1

            execution = True
        return execution

    def get_winner(self):
        return self.game_logic.get_winner()



    def __get_selected_move(self, destination_row, destination_column):
        for move in self.__current_moves:
            if (move.get_row() == destination_row) and (move.get_column() == destination_column):
                return move
        return None









################################# OLD ###################################
    def start(self, board_size):
        print()

    def move_queen_to(self, current_row, current_column, destination_row, destination_column):
        move = self.__create_move_object(current_row, current_column, destination_row, destination_column)
        self.game_logic.set_move(self.__internal_board, move)
        # self.__game_logic.print_logic_checks(self.__player_turn)

    def print_board(self):
        print("Turn: Player " + str(self.__player_turn))
        self.__internal_board.print()

    # private methods
    def __create_move_object(self, current_row, current_column, destination_row, destination_column):
        queen = self.__internal_board.get_tile(current_row, current_column)
        return Move.Move(queen, destination_row, destination_column)



