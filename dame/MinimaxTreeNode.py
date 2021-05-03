import AdapterPrint

class MinimaxTreeNode:
    __dame_logic = None
    __maximizing_player = -1
    __current_board = None
    __executed_move = None
    __subtree_score = 0
    __player_turn = -1
    __current_tree_depth = -1
    __max_tree_depth = -1
    __child_nodes = []

    # replace player argument with current_board.get_player()?
    def __init__(self, dame_logic, maximizing_player, board, move, player_turn, max_tree_depth, current_tree_depth=-1):
        self.__dame_logic = dame_logic
        self.__maximizing_player = maximizing_player
        self.__current_board = board.clone()
        self.__executed_move = move
        self.__player_turn = self.__dame_logic.get_opponent(player_turn)
        self.__current_tree_depth = current_tree_depth + 1
        self.__max_tree_depth = max_tree_depth
        self.__child_nodes = []
        if self.__current_tree_depth < self.__max_tree_depth:
            self.build_child_nodes()
        # print("Player turn: " + str(self.__current_board.get_player_turn()))
        # self.test_print()


    def get_subtree_score(self):
        return self.__subtree_score


    def get_executed_move(self):
        return self.__executed_move


    def build_child_nodes(self):
        if not self.__dame_logic.is_game_over(self.__current_board):
            for queen in self.__current_board.get_queens_for(self.__player_turn):
                for move in self.__dame_logic.get_possible_moves_for(queen.get_row(), queen.get_column(), self.__current_board):
                    board_clone = self.__current_board.clone()
                    move_clone = move.clone()
                    self.__dame_logic.execute_move(move_clone.clone(), board_clone)
                    child = MinimaxTreeNode(self.__dame_logic, self.__maximizing_player, board_clone, move_clone,
                                            self.__player_turn, self.__max_tree_depth, self.__current_tree_depth)
                    self.__child_nodes.append(child)


    def get_best_move(self):
        self.evaluate_tree()
        # self.test_print_scores()
        return self.get_child_max_score().get_executed_move()


    def evaluate_tree(self):
        if len(self.__child_nodes) == 0:
            self.__subtree_score = self.__dame_logic.evaluate_board(self.__current_board, self.__maximizing_player)
        else:
            for child in self.__child_nodes:
                child.evaluate_tree()
                self.__subtree_score = self.calculate_subtree_score()


    def calculate_subtree_score(self):
        max_min_score = None
        for child in self.__child_nodes:
            child_score = child.get_subtree_score()
            if max_min_score is None:
                max_min_score = child_score
            elif ((self.__player_turn == self.__maximizing_player) and (child_score > max_min_score)) or \
                 ((self.__player_turn != self.__maximizing_player) and (child_score < max_min_score)):
                    max_min_score = child_score
        return max_min_score


    def get_child_max_score(self):
        child_max_score = None
        for child in self.__child_nodes:
            if child_max_score is None:
                child_max_score = child
            elif child.get_subtree_score() > child_max_score.get_subtree_score():
                child_max_score = child
        return child_max_score


    # FOR TESTING
    def test_print(self):
        if (len(self.__child_nodes) == 0):
            external_board = self.__dame_logic.get_external_board(self.__current_board)
            formatted_board = AdapterPrint.AdapterPrint().get_print_of_board(external_board)
            print(formatted_board)
            score = self.__dame_logic.evaluate_board(self.__current_board, self.__maximizing_player)
            print("Score: " + str(score))


    def test_print_scores(self):
        print(str(self.__current_tree_depth) + ": " + str(self.__subtree_score))
        for child in self.__child_nodes:
            child.test_print_scores()