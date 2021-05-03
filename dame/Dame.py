import DameLogic
import MoveWrapper
import AdapterPrint

class Dame:

    __logic = None
    __possible_moves = []
    __observer = []

    def __init__(self, difficulty):
        self.__logic = DameLogic.DameLogic(self, difficulty)
        self.__possible_moves = []
        self.__observer = []


    # public methods
    def add_observer(self, observer):
        self.__observer.append(observer)


    def send_external_board(self, external_board=None):
        if external_board is None:
            external_board = self.__logic.get_external_board()
        for observer in self.__observer:
            adapter = observer.get_format_adapter()
            formatted_board = adapter.format_board(external_board)
            observer.get_observer().draw_board(formatted_board)


    def send_possible_moves(self, row, column, moves):
        for observer in self.__observer:
            adapter = observer.get_format_adapter()
            formatted_moves = adapter.format_possible_moves(row, column, moves)
            observer.get_observer().show_possible_moves(formatted_moves)


    def get_possible_moves_for(self, row, column):
        self.__possible_moves = self.__logic.get_possible_moves_for(row, column)
        wrapped_moves = self.__wrap_moves(self.__possible_moves)
        self.send_possible_moves(row, column, wrapped_moves)


    def execute_move(self, row, column):
        execution = False
        selected_move = self.__get_selected_move(row, column)
        if selected_move is not None:
            self.__logic.process_human_move(selected_move)
            execution = True
        return execution


    def get_winner(self):
        winner = self.__logic.get_winner()
        return self.__logic.get_player_name(winner)


    # private methods
    def __wrap_moves(self, moves):
        output = []
        for move in moves:
            output.append(MoveWrapper.MoveWrapper(move))
        return output

    def __get_selected_move(self, row, column):
        output = None
        for move in self.__possible_moves:
            if move.get_row() == row and move.get_column() == column:
                output = move
                break
        return output
