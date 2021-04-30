import DameLogic
import MoveWrapper
import AdapterPrint

class Dame:

    __logic = None
    __possible_moves = []

    def __init__(self):
        self.__logic = DameLogic.DameLogic()


    # public methods
    def get_list_of_possible_moves(self, row, column):
        self.__possible_moves = self.__logic.get_possible_moves_for(row, column)
        return self.__get_wrapped_moves()


    def get_print_of_possible_moves(self, row, column):
        self.__possible_moves = self.__logic.get_possible_moves_for(row, column)
        print_adapter = AdapterPrint.AdapterPrint()
        return print_adapter.get_print_of_possible_moves(row, column, self.__possible_moves)


    def get_print_of_board(self):
        external_board = self.__logic.get_external_board()
        print_adapter = AdapterPrint.AdapterPrint()
        return print_adapter.get_print_of_board(external_board)


    def get_winner(self):
        return self.__logic.get_winner()


    def execute_player_move_for(self, row, column):
        move = self.__get_selected_move(row, column)
        if move is not None:
            self.__logic.execute_move(move)


    def execute_player_move(self, wrapped_move):
        move = self.__get_unwrapped_move(wrapped_move)
        self.__logic.execute_move(move)

    # ?
    def execute_ki_move(self):
        pass


    # private methods
    def __get_wrapped_moves(self):
        output = []
        for move in self.__possible_moves:
            output.append(MoveWrapper.MoveWrapper(move))
        return output


    def __get_unwrapped_move(self, wrapped_move):
        return self.__get_selected_move(wrapped_move.get_row(), wrapped_move.get_column())


    def __get_selected_move(self, row, column):
        for move in self.__possible_moves:
            if move.get_row() == row and move.get_column() == column:
                return move