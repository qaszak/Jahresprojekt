# import BoardEvaluationLogic
import AdapterPrint

class MinimaxTreeNode:
    __dame_logic = None
    __current_board = None
    __executed_move = None
    __value_of_subtree = None
    __player_turn = None
    __current_tree_depth = -1
    __max_tree_depth = -1
    __child_nodes = []

    # replace player argument with current_board.get_player()?
    def __init__(self, dame_logic, board, move, player, current_tree_depth, max_tree_depth):
        self.__dame_logic = dame_logic
        self.__current_board = board.clone()
        self.__executed_move = move
        self.__player_turn = self.__dame_logic.get_opponent(player)
        self.__current_tree_depth = current_tree_depth + 1
        self.__max_tree_depth = max_tree_depth
        self.__child_nodes = []
        if self.__current_tree_depth < self.__max_tree_depth:
            self.build_child_nodes()
        # print(str(len(self.__child_nodes)))
        self.test_print()


    def build_child_nodes(self):
        if not self.__dame_logic.is_game_over(self.__current_board):
            moves = []
            for queen in self.__current_board.get_queens_for(self.__player_turn):
                for move in self.__dame_logic.get_possible_moves_for(queen.get_row(), queen.get_column(), self.__current_board):
                    board_clone = self.__current_board.clone()
                    move_clone = move.clone()
                    self.__dame_logic.execute_move(move_clone, board_clone)
                    child = MinimaxTreeNode(self.__dame_logic, board_clone, move_clone, self.__player_turn, self.__current_tree_depth, self.__max_tree_depth)
                    self.__child_nodes.append(child)


    def test_print(self):
        if (len(self.__child_nodes) == 0):
            external_board = self.__dame_logic.get_external_board(self.__current_board)
            formatted_board = AdapterPrint.AdapterPrint().get_print_of_board(external_board)
            print(formatted_board)





    def evaluate_board(self):
        pass
        # if children exist
        #   for all children:
        #       child.evaluate_board()
        #   if Maximizer:
        #        __value_of_subtree = max(children.__value_of_subtree)
        #   elif Minimizer:
        #       __value_of_subtree = min(children.__value_of_subtree)
        # else
        #   __value_of_subtree = BoardEvaluationLogic(__board)
