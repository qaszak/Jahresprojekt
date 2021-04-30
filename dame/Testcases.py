import DameLogic

############## HOW TO RUN TESTCASES #####################
#      Uncomment the testcase functions in classes:     #
#           - DameLogic                                 #
#           - WinLogic                                  #
#           - MovementLogic                             #
#########################################################

result = None
testcase_counter = 0
error_collection = []

def print_testcase(name_testcase, result, expected_result):
    global testcase_counter, error_collection
    output = ""
    if result == expected_result:
        output = "OK : "
    else:
        output = "ERROR : "
        error_collection.append(name_testcase)
    testcase_counter += 1
    print(output + str(name_testcase))


dame_logic = DameLogic.DameLogic()
a = dame_logic.get_ai_character()
p = dame_logic.get_human_character()
_ = dame_logic.get_empty_tile_character()
ai = dame_logic.get_ai_player()
player = dame_logic.get_human_player()


"""
TEMPLATE FOR TEST CASES

# TESTCASE: 
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
"""

############################## WIN LOGIC ##############################


######## WINLOGIC.__IS_PLAYER_ON_OPPONENTS_BASELINE() ########

# TESTCASE: AI is at players baseline
test_board = [[_, _, _, _, _, _],
              [_, a, _, _, a, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, _, _, _, _],
              [_, a, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_on_opponents_baseline(): AI at players baseline -> Expected result: True",
               win_logic.is_player_on_opponents_baseline(ai), True)

# TESTCASE: Player is at AIs baseline
test_board = [[_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, p, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_on_opponents_baseline(): Player at AIs baseline -> Expected result: True",
               win_logic.is_player_on_opponents_baseline(player), True)

# TESTCASE: AI is not at players baseline
test_board = [[a, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, a, _],
              [_, _, _, _, _, _],
              [_, _, a, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_on_opponents_baseline(): AI not at players baseline -> Expected result: False",
               win_logic.is_player_on_opponents_baseline(ai), False)

# TESTCASE: Player is not at AIs baseline
test_board = [[_, _, _, _, _, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, p],
              [p, _, _, _, _, _],
              [_, _, p, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_on_opponents_baseline(): Player not at AIs baseline -> Expected result: False",
               win_logic.is_player_on_opponents_baseline(player), False)


######## WINLOGIC.__is_player_out_of_queens ########

# TESTCASE: AI is out of queens
test_board = [[_, _, _, _, _, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, p, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_queens(): AI is out of queens -> Expected result: True",
               win_logic.is_player_out_of_queens(ai), True)

# TESTCASE: Player is out of queens
test_board = [[_, _, _, _, _, _],
              [_, a, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, a, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_queens(): Player is out of queens -> Expected result: True",
               win_logic.is_player_out_of_queens(player), True)

# TESTCASE: AI is not out of queens
test_board = [[_, _, _, _, _, _],
              [_, p, _, _, _, _],
              [_, _, a, _, _, _],
              [_, _, _, _, p, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_queens(): AI is not out of queens -> Expected result: False",
               win_logic.is_player_out_of_queens(ai), False)

# TESTCASE: Player is not out of queens
test_board = [[_, _, _, _, _, _],
              [_, p, _, _, _, _],
              [_, _, a, _, _, _],
              [_, _, _, _, p, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_queens(): Player is not out of queens -> Expected result: False",
               win_logic.is_player_out_of_queens(player), False)


######## WINLOGIC.__is_player_out_of_moves() ########

# TESTCASE: AI is out of moves
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, a, _, a, _],
              [_, p, _, p, _, p],
              [p, _, p, _, p, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_moves(): AI is out of queens -> Expected result: True",
               win_logic.is_player_out_of_moves(ai), True)

# TESTCASE: Player is out of moves
test_board = [[a, a, _, _, a, a],
              [_, a, a, a, a, _],
              [_, _, p, p, _, _],
              [_, a, _, _, _, _],
              [p, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_moves(): Player is out of queens -> Expected result: True",
               win_logic.is_player_out_of_moves(player), True)

# TESTCASE: AI can make only non-hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_moves(): AI can make only non-hitting move -> Expected result: False",
               win_logic.is_player_out_of_moves(ai), False)

# TESTCASE: Player can make only non-hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_moves(): Player can make only non-hitting move -> Expected result: False",
               win_logic.is_player_out_of_moves(player), False)

# TESTCASE: AI can make only hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, p, _, p, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_moves(): AI can make only hitting move -> Expected result: False",
               win_logic.is_player_out_of_moves(ai), False)

# TESTCASE: Player can make only hitting move
test_board = [[_, _, _, _, _, _],
              [a, _, _, _, _, _],
              [_, a, _, a, _, _],
              [_, _, p, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_moves(): Player can make only hitting move -> Expected result: False",
               win_logic.is_player_out_of_moves(player), False)

# TESTCASE: AI can make a hitting or a non-hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, p, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_moves(): AI can make a hitting or a non-hitting move -> Expected result: False",
               win_logic.is_player_out_of_moves(ai), False)

# TESTCASE: Player can make a hitting or a non-hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, p, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.__is_player_out_of_moves(): Player can make a hitting or a non-hitting move -> Expected result: False",
               win_logic.is_player_out_of_moves(player), False)


######## WINLOGIC.get_winner() ########

# TESTCASE: AI is at players baseline
test_board = [[_, _, _, _, _, _],
              [_, a, _, _, a, _],
              [_, _, p, _, _, _],
              [_, _, _, a, _, _],
              [_, _, _, _, _, _],
              [_, a, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): AI at players baseline -> Expected result: 1 (AI)",
               win_logic.get_winner(), 1)

# TESTCASE: Player is at AIs baseline
test_board = [[_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, p, _],
              [_, p, _, a, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): Player at AIs baseline -> Expected result: 2 (Player)",
               win_logic.get_winner(), 2)

# TESTCASE: Neither AI nor Player is at opponents baseline
test_board = [[_, _, _, _, _, _],
              [_, a, _, _, _, _],
              [_, _, p, _, a, _],
              [_, _, _, _, _, _],
              [_, _, a, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): Neither AI nor Player is at opponents baseline -> Expected result: ''",
               win_logic.get_winner(), "")

# TESTCASE: AI is out of queens
test_board = [[_, _, _, _, _, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, p, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): AI is out of queens -> Expected result: 2 (Player)",
               win_logic.get_winner(), 2)

# TESTCASE: Player is out of queens
test_board = [[_, _, _, _, _, _],
              [_, a, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, a, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): Player is out of queens -> Expected result: 1 (AI)",
               win_logic.get_winner(), 1)

# TESTCASE: Neither AI nor Player is out of moves
test_board = [[_, _, _, _, _, _],
              [_, a, _, _, _, _],
              [_, _, p, _, _, _],
              [_, _, _, _, a, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): Neither AI nor Player is out of moves -> Expected result: ''",
               win_logic.get_winner(), "")

# TESTCASE: AI is out of moves
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, a, _, a, _],
              [_, p, _, p, _, p],
              [p, _, p, _, p, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): AI is out of queens -> Expected result: 2 (Player)",
               win_logic.get_winner(), 2)

# TESTCASE: Player is out of moves
test_board = [[a, a, _, _, a, a],
              [_, a, a, a, a, _],
              [_, _, p, p, _, _],
              [_, a, _, _, _, _],
              [p, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): Player is out of queens -> Expected result: 1 (AI)",
               win_logic.get_winner(), 1)

# TESTCASE: AI can make only non-hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): AI can make only non-hitting move -> Expected result: ''",
               win_logic.get_winner(), "")

# TESTCASE: Player can make only non-hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): Player can make only non-hitting move -> Expected result: ''",
               win_logic.get_winner(), "")

# TESTCASE: AI can make only hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, p, _, p, _],
              [_, p, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): AI can make only hitting move -> Expected result: ''",
               win_logic.get_winner(), "")

# TESTCASE: Player can make only hitting move
test_board = [[_, _, _, _, _, _],
              [a, _, _, _, _, _],
              [_, a, _, a, _, _],
              [_, _, p, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): Player can make only hitting move -> Expected result: ''",
               win_logic.get_winner(), "")

# TESTCASE: AI can make a hitting or a non-hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, p, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): AI can make a hitting or a non-hitting move -> Expected result: ''",
               win_logic.get_winner(), "")

# TESTCASE: Player can make a hitting or a non-hitting move
test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, p, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
win_logic = dame_logic.get_win_logic()
print_testcase("WinLogic.get_winner(): Player can make a hitting or a non-hitting move -> Expected result: ''",
               win_logic.get_winner(), "")


############################## MOVEMENT LOGIC ##############################

######## MOVEMENTLOGIC.__calculate_row_distance  ########
######## MOVEMENTLOGIC.__calculate_column_distance  ########

test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, p, _, _, _],
              [_, _, _, _, a, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
movement_logic = dame_logic.get_movement_logic()
moves = dame_logic.create_moves([[3, 2, 5, 5], [2, 3, 0, 2], [4, 4, 4, 4]])

# TESTCASE: Positive row distance
print_testcase("MovementLogic.__calculate_row_distance(): Positive row distance from 3 to 5 -> Expected result: 2",
               movement_logic.calculate_row_distance(moves[0]), 2)

# TESTCASE: Negative row distance
print_testcase("MovementLogic.__calculate_row_distance(): Negative row distance from 2 to 0 -> Expected result: -2",
               movement_logic.calculate_row_distance(moves[1]), -2)

# TESTCASE: zero row distance
print_testcase("MovementLogic.__calculate_row_distance(): Zero row distance from 4 to 4 -> Expected result: 0",
               movement_logic.calculate_row_distance(moves[2]), 0)

# TESTCASE: Positive column distance
print_testcase("MovementLogic.__calculate_column_distance(): Positive column distance from 2 to 5 -> Expected result: 3",
               movement_logic.calculate_column_distance(moves[0]), 3)

# TESTCASE: Negative column distance
print_testcase("MovementLogic.__calculate_column_distance(): Negative column distance from 3 to 2 -> Expected result: -1",
               movement_logic.calculate_column_distance(moves[1]), -1)

# TESTCASE: zero column distance
print_testcase("MovementLogic.__calculate_column_distance(): Zero column distance from 4 to 4 -> Expected result: 0",
               movement_logic.calculate_column_distance(moves[2]), 0)


######## MOVEMENTLOGIC.get_hit_queen ########
######## MOVEMENTLOGIC.__is_hitting_move ########

test_board = [[_, _, _, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, a, _, _],
              [_, _, p, _, _, a],
              [p, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
movement_logic = dame_logic.get_movement_logic()

# TESTCASE: AI Queen hits Player Queen
moves = dame_logic.create_moves([[2, 3, 4, 1], [3, 2, 0, 2]])
print_testcase("MovementLogic.__get_hit_queen(): AI Queen hits Player Queen -> Expected result: Queen (3,2)",
               movement_logic.get_hit_queen(moves[0]), moves[1].get_queen())

# TESTCASE: Player Queen hits AI Queen
moves = dame_logic.create_moves([[3, 2, 1, 4], [2, 3, 0, 2]])
print_testcase("MovementLogic.__get_hit_queen(): Player Queen hits AI Queen -> Expected result: Queen (2,3)",
               movement_logic.get_hit_queen(moves[0]), moves[1].get_queen())

# TESTCASE: AI Queen hits makes non-hitting move
moves = dame_logic.create_moves([[2, 3, 3, 4]])
print_testcase("MovementLogic.__get_hit_queen(): AI Queen hits makes non-hitting move -> Expected result: None",
               movement_logic.get_hit_queen(moves[0]), None)

# TESTCASE: Player Queen hits makes non-hitting move
moves = dame_logic.create_moves([[4, 0, 3, 1]])
print_testcase("MovementLogic.__get_hit_queen(): Player Queen hits makes non-hitting move -> Expected result: None",
               movement_logic.get_hit_queen(moves[0]), None)

# TESTCASE: AI Queen makes hitting move
moves = dame_logic.create_moves([[2, 3, 4, 1]])
print_testcase("MovementLogic.__is_hitting_move(): AI Queen hits Player Queen -> Expected result: True",
               movement_logic.is_hitting_move(moves[0]), True)

# TESTCASE: Player Queen makes hitting move
moves = dame_logic.create_moves([[3, 2, 1, 4]])
print_testcase("MovementLogic.__is_hitting_move(): Player Queen hits AI Queen -> Expected result: True",
               movement_logic.is_hitting_move(moves[0]), True)

# TESTCASE: AI Queen hits makes non-hitting move
moves = dame_logic.create_moves([[2, 3, 3, 4]])
print_testcase("MovementLogic.__is_hitting_move(): AI Queen hits makes non-hitting move -> Expected result: False",
               movement_logic.is_hitting_move(moves[0]), False)

# TESTCASE: Player Queen hits makes non-hitting move
moves = dame_logic.create_moves([[4, 0, 3, 1]])
print_testcase("MovementLogic.__is_hitting_move(): Player Queen hits makes non-hitting move -> Expected result: False",
               movement_logic.is_hitting_move(moves[0]), False)


######## MOVEMENTLOGIC.__is_non_hitting_move ########

# TESTCASE: AI Queen makes hitting move
moves = dame_logic.create_moves([[2, 3, 4, 1]])
print_testcase("MovementLogic.__is_non_hitting_move(): AI Queen hits Player Queen -> Expected result: False",
               movement_logic.is_non_hitting_move(moves[0]), False)

# TESTCASE: Player Queen makes hitting move
moves = dame_logic.create_moves([[3, 2, 1, 4]])
print_testcase("MovementLogic.__is_non_hitting_move(): Player Queen hits AI Queen -> Expected result: False",
               movement_logic.is_non_hitting_move(moves[0]), False)

# TESTCASE: AI Queen hits makes non-hitting move
moves = dame_logic.create_moves([[2, 3, 3, 4]])
print_testcase("MovementLogic.is_non_hitting_move(): AI Queen hits makes non-hitting move -> Expected result: True",
               movement_logic.is_non_hitting_move(moves[0]), True)

# TESTCASE: Player Queen hits makes non-hitting move
moves = dame_logic.create_moves([[4, 0, 3, 1]])
print_testcase("MovementLogic.__is_non_hitting_move(): Player Queen hits makes non-hitting move -> Expected result: True",
               movement_logic.is_non_hitting_move(moves[0]), True)


######## MOVEMENTLOGIC.__is_move_blocked_by_queen ########

# TESTCASE: Player Queen moves to a field occupied by other player queen
moves = dame_logic.create_moves([[3, 2, 4, 0]])
print_testcase("MovementLogic.__is_move_blocked_by_queen(): Player Queen moves to a field occupied by other player queen -> Expected result: True",
               movement_logic.is_move_blocked_by_queen(moves[0]), True)

# TESTCASE: Player Queen moves to a field occupied by AI queen
moves = dame_logic.create_moves([[3, 2, 2, 3]])
print_testcase("MovementLogic.__is_move_blocked_by_queen(): Player Queen moves to a field occupied by AI queen -> Expected result: True",
               movement_logic.is_move_blocked_by_queen(moves[0]), True)

# TESTCASE: AI Queen moves to a field occupied by other AI queen
moves = dame_logic.create_moves([[2, 3, 3, 5]])
print_testcase("MovementLogic.__is_move_blocked_by_queen(): AI Queen moves to a field occupied by other AI queen -> Expected result: True",
               movement_logic.is_move_blocked_by_queen(moves[0]), True)

# TESTCASE: AI Queen moves to a field occupied by player queen
moves = dame_logic.create_moves([[3, 5, 4, 0]])
print_testcase("MovementLogic.__is_move_blocked_by_queen(): AI Queen moves to a field occupied by player queen -> Expected result: True",
               movement_logic.is_move_blocked_by_queen(moves[0]), True)

# TESTCASE: AI Queen moves to a free field
moves = dame_logic.create_moves([[3, 5, 2, 4]])
print_testcase("MovementLogic.__is_move_blocked_by_queen(): AI Queen moves to a free field -> Expected result: False",
               movement_logic.is_move_blocked_by_queen(moves[0]), False)

# TESTCASE: Player Queen moves to a free field
moves = dame_logic.create_moves([[4, 0, 5, 1]])
print_testcase("MovementLogic.__is_move_blocked_by_queen(): Player Queen moves to a free field -> Expected result: False",
               movement_logic.is_move_blocked_by_queen(moves[0]), False)


######## MOVEMENTLOGIC.__is_row_direction_valid ########

# TESTCASE: Player Queen moves upward (allowed)
moves = dame_logic.create_moves([[3, 2, 2, 1]])
print_testcase("MovementLogic.__is_row_direction_valid(): Player Queen moves upward (allowed) -> Expected result: True",
               movement_logic.is_row_direction_valid(moves[0]), True)

# TESTCASE: Player Queen moves downward (forbidden)
moves = dame_logic.create_moves([[3, 2, 4, 1]])
print_testcase("MovementLogic.__is_row_direction_valid(): Player Queen moves downward (forbidden) -> Expected result: False",
               movement_logic.is_row_direction_valid(moves[0]), False)

# TESTCASE: AI Queen moves downward (allowed)
moves = dame_logic.create_moves([[2, 3, 3, 4]])
print_testcase("MovementLogic.__is_row_direction_valid(): AI Queen moves upward (allowed) -> Expected result: True",
               movement_logic.is_row_direction_valid(moves[0]), True)

# TESTCASE: AI Queen moves upward (forbidden)
moves = dame_logic.create_moves([[2, 3, 1, 2]])
print_testcase("MovementLogic.__is_row_direction_valid(): AI Queen moves downward (forbidden) -> Expected result: False",
               movement_logic.is_row_direction_valid(moves[0]), False)


######## MOVEMENTLOGIC.__is_move_in_board ########

# TESTCASE: Queen stays in the board(allowed)
moves = dame_logic.create_moves([[3, 2, 5, 3]])
print_testcase("MovementLogic.__is_move_in_board(): Queen stays in the board(allowed) -> Expected result: True",
               movement_logic.is_move_in_board(moves[0]), True)

# TESTCASE: Queen leaves the board(forbidden)
moves = dame_logic.create_moves([[4, 0, -2, 7]])
print_testcase("MovementLogic.__is_move_in_board(): Queen leaves the board(forbidden) -> Expected result: False",
               movement_logic.is_move_in_board(moves[0]), False)


######## MOVEMENTLOGIC.__is_move_valid ########

test_board = [[_, _, _, _, _, a],
              [_, _, a, _, _, _],
              [_, a, _, a, _, _],
              [p, _, p, _, _, _],
              [_, _, _, _, _, _],
              [_, _, _, _, _, _]]
dame_logic.load_custom_board(test_board)
movement_logic = dame_logic.get_movement_logic()


print("\n\n\n################ RESULT ################\n" + \
      "\tSuccessful Testcases: " + str(testcase_counter - len(error_collection)) + " of " + str(testcase_counter) + "\n" + \
      "\tErrors: " + str(len(error_collection)))
for error in range(0, len(error_collection)):
    print("\t\tError #" + str(error + 1) + "\t" + str(error_collection[error]))