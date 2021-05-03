import DameLogic
import MinimaxTreeNode

dame_logic = DameLogic.DameLogic("Test", 4)
board = dame_logic.get_board()
root = MinimaxTreeNode.MinimaxTreeNode(dame_logic, 1, board, None, 2, 4)
move = root.get_best_move()
print("Best move: (" + str(move.get_queen().get_row()) + "," + \
      str(move.get_queen().get_column()) + ") --> (" + str(move.get_row()) + "," + \
      str(move.get_column()) + ")")

