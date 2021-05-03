# uses an instance of ExternalDameBoard to format the board state into an output string

class AdapterPrint:


    def format_board(self, external_board):
        output = "\n" + str(external_board.get_name_human()) + "\t\t\t" + str(external_board.get_name_ai()) + \
                 "\nQueens: " + str(external_board.get_number_of_queens_human()) + \
                 "\t\tQueens: " + str(external_board.get_number_of_queens_ai()) + \
                 "\nScore: " + str(external_board.get_score()) + "\n\nCurrent Turn: " + \
                 str(external_board.get_name_player_turn()) + " (" + str(external_board.get_character_player_turn())  + \
                 ")\n\n" + str(self.__format_board(external_board.get_board()))
        return output


    def format_possible_moves(self, row, column, moves):
        position = "(" + str(row) + "," + str(column) + ")"
        if len(moves) == 0:
            output = "\n\tNo moves possible for " + position
        else:
            output = "\n\tPossible moves for queen " + position + ":\n\t\t"
            for move in moves:
                output += "(" + str(move.get_row()) + "," + str(move.get_column()) + ") "
        return output


    def __format_board(self, board):
        board_range = range(0, len(board))
        output = "-------------------------\n"
        for row in board_range:
            for column in board_range:
                output += ("| " + str(board[row][column]) + " ")
            output += "|\n-------------------------\n"
        return output
