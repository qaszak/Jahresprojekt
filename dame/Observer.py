# represents external observers of Dame.
# Observers must implement methods draw_board(board) and show_possible_moves(moves)

class Observer:
    __observer = None
    __format_adapter = None

    def __init__(self, observer, format_adapter):
        self.__observer = observer
        self.__format_adapter = format_adapter

    def get_observer(self):
        return self.__observer

    def get_format_adapter(self):
        return self.__format_adapter