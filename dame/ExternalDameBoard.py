# for external communication of the board state

class ExternalDameBoard:

    __board = [[]]
    __score = -1
    __name_ai = ""
    __name_human = ""
    __name_player_turn = ""
    __character_player_turn = ""
    __number_of_queens_ai = -1
    __number_of_queens_human = -1
    __ai_queen_character = ""
    __human_queen_character = ""
    __empty_tile_character = ""

    def __init__(self, board, score, name_ai, name_human, name_player_turn, character_player_turn, number_of_queens_ai, number_of_queens_human,
                 ai_queen_character, human_queen_character, empty_tile_character):
        self.__board = board
        self.__score = score
        self.__name_ai = name_ai
        self.__name_human = name_human
        self.__name_player_turn = name_player_turn
        self.__character_player_turn = character_player_turn
        self.__number_of_queens_ai = number_of_queens_ai
        self.__number_of_queens_human = number_of_queens_human
        self.__ai_queen_character = ai_queen_character
        self.__human_queen_character = human_queen_character
        self.__empty_tile_character = empty_tile_character



    def get_board(self):
        return self.__board


    def get_score(self):
        return self.__score


    def get_name_ai(self):
        return self.__name_ai


    def get_name_human(self):
        return self.__name_human


    def get_name_player_turn(self):
        return self.__name_player_turn


    def get_character_player_turn(self):
        return self.__character_player_turn


    def get_number_of_queens_ai(self):
        return self.__number_of_queens_ai


    def get_number_of_queens_human(self):
        return self.__number_of_queens_human


    def get_ai_queen_character(self):
        return self.__ai_queen_character


    def get_human_queen_character(self):
        return self.__human_queen_character


    def get_empty_tile_character(self):
        return self.__empty_tile_character