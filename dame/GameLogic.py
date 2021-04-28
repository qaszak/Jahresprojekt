import DameBoard
import Queen
import Move

class GameLogic:
    # ToDos:
    # - implement as a singleton
    # - implement methods

    __board = None
    __move = None

    # public methods
    def set_move(self, board, move):
        self.__board = board
        self.__move = move

    def is_queen_selected(self):
        return not(self.__move.get_queen() is None)

    def is_players_turn(self, player):
        return self.__move.get_queen().get_player() == player

    def is_move_valid(self):
        pass


    def is_hitting_move(self):
        pass

    def is_game_won(self):
        pass

    # private methods
    def is_direction_valid(self):
        return self.is_row_direction_valid(self) and self.is_column_direction_valid(self)

    def is_row_direction_valid(self):
        player = self.__move.get_queen().get_player()
        if player == 1:
            return self.__move.get_row() - self.__move.get_queen().get_row() in [1, 2]
        elif player == 2:
            return self.__move.get_row() - self.__move.get_queen().get_row() in [-1, -2]
        else:
            return False

    def is_column_direction_valid(self):
        pass

    def is_move_blocked(self):
        return self.is_move_blocked_by_own_queen(self) and \
               self.is_move_blocked_by_opposing_queen(self) and \
               self.is_move_blocked_by_border(self)

    def is_move_blocked_by_own_queen(self):
        pass

    def is_move_blocked_by_border(self):
        pass

    def is_move_blocked_by_opposing_queen(self):
        pass


    # temporary method for testing purposes
    def print_logic_checks(self, player_turn):
        is_queen_selected = self.is_queen_selected()
        print("queen selected: " + str(is_queen_selected))
        if is_queen_selected:
            print("is players turn: " + str(self.is_players_turn(player_turn)))
            print("row direction is valid: " + str(self.is_row_direction_valid()))
