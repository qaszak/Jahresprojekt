import Game

game = Game.Game(6)
game.print_board()
print("\nB = Player 1\nW = Player 2\n\nTESTCASES FOR DAME\n")
logic = game.game_logic
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



# 1: GAME LOGIC



# 1.1 PIECE SELECTION

# Testcase 1.1.1: select a queen
game.move_queen_to(0, 1, 0, 0)
result = logic.is_queen_selected()
print_testcase("1.1.1 GameLogic.is_queen_selected -> correct selection [0,1]", result, True)

# Testcase 1.1.2: select an empty tile
game.move_queen_to(0, 0, 1, 0)
result = logic.is_queen_selected()
print_testcase("1.1.2 GameLogic.is_queen_selected -> incorrect selection [0,0]", result, False)



# 1.2 PLAYERS TURN

# Testcase 1.2.1: Player1(B) tries to make a move while it is his turn
game.move_queen_to(1, 0, 2, 0)
result = logic.is_players_turn(1)
print_testcase("1.2.1 GameLogic.is_players_turn -> correct player", result, True)

# Testcase 1.2.2: Player1(B) tries to make a move while it is Player2(W)´s turn
game.move_queen_to(1, 0, 2, 0)
result = logic.is_players_turn(2)
print_testcase("1.2.2 GameLogic.is_players_turn -> correct player", result, False)



# 1.3 MOVEMENT


#1.3.1 DESTINATION IS STILL IN BOARD

# Testcase 1.3.1.1: Queen tries to move to a tile on the board (allowed)
game.move_queen_to(1, 0, 2, 0)
result = logic.is_move_in_board()
print_testcase("1.3.1.1 GameLogic.is_move_in_board -> legal movement to a tile on the board", result, True)

# Testcase 1.3.1.2: Queen tries to move left outside of the board (forbidden)
game.move_queen_to(1, 0, 1, -3)
result = logic.is_move_in_board()
print_testcase("1.3.1.2 GameLogic.is_move_in_board -> illegal movement left outside of the board", result, False)

# Testcase 1.3.1.3: Queen tries to move right outside of the board (forbidden)
game.move_queen_to(0, 5, 0, 6)
result = logic.is_move_in_board()
print_testcase("1.3.1.3 GameLogic.is_move_in_board -> illegal movement right outside of the board", result, False)

# Testcase 1.3.1.4: Queen tries to move upwards outside of the board (forbidden)
game.move_queen_to(0, 5, -1, 5)
result = logic.is_move_in_board()
print_testcase("1.3.1.4 GameLogic.is_move_in_board -> illegal movement upwards outside of the board", result, False)

# Testcase 1.3.1.5: Queen tries to move downwards outside of the board (forbidden)
game.move_queen_to(5, 0, 6, 0)
result = logic.is_move_in_board()
print_testcase("1.3.1.5 GameLogic.is_move_in_board -> illegal movement downwards outside of the board", result, False)


# 1.3.2 VALIDATE VERTICAL MOVEMENT FOR PLAYERS

# Testcase 1.3.2.1: Player1(B) tries to move downwards one tile (allowed)
game.move_queen_to(0, 5, 1, 5)
result = logic.is_row_direction_valid()
print_testcase("1.3.2.1 GameLogic.is_row_direction_valid -> player1: legal movement one tile downward", result, True)

# Testcase 1.3.2.2: Player1(B) tries to move downwards two tiles (allowed)
game.move_queen_to(0, 5, 2, 5)
result = logic.is_row_direction_valid()
print_testcase("1.3.2.2 GameLogic.is_row_direction_valid -> player1: legal movement two tiles downward", result, True)

# Testcase 1.3.2.3: Player1(B) tries to move downwards three tiles (forbidden)
game.move_queen_to(0, 5, 3, 5)
result = logic.is_row_direction_valid()
print_testcase("1.3.2.3 GameLogic.is_row_direction_valid -> player1: illegal movement three tiles downward", result, False)

# Testcase 1.3.2.4: Player1(B) tries to move upwards one tile (forbidden)
game.move_queen_to(1, 4, 0, 4)
result = logic.is_row_direction_valid()
print_testcase("1.3.2.4 GameLogic.is_row_direction_valid -> player1: illegal movement upward", result, False)

# Testcase 1.3.2.5: Player2(W) tries to move upwards one tile (allowed)
game.move_queen_to(5, 0, 4, 0)
result = logic.is_row_direction_valid()
print_testcase("1.3.2.5 GameLogic.is_row_direction_valid -> player2: legal movement one tile upward", result, True)

# Testcase 1.3.2.6: Player2(W) tries to move upwards two tiles (allowed)
game.move_queen_to(5, 0, 3, 0)
result = logic.is_row_direction_valid()
print_testcase("1.3.2.6 GameLogic.is_row_direction_valid -> player2: legal movement two tiles upward", result, True)

# Testcase 1.3.2.7: Player2(W) tries to move upwards three tiles (forbidden)
game.move_queen_to(5, 0, 2, 0)
result = logic.is_row_direction_valid()
print_testcase("1.3.2.7 GameLogic.is_row_direction_valid -> player2: illegal movement three tiles upward", result, False)

# Testcase 1.3.2.8: Player2(W) tries to move downwards one tile (forbidden)
game.move_queen_to(4, 1, 5, 1)
result = logic.is_row_direction_valid()
print_testcase("1.3.2.8 GameLogic.is_row_direction_valid -> player2: illegal movement three tiles upward", result, False)



# 1.3.3 VALIDATE HORIZONTAL MOVEMENT

# Testcase 1.3.3.1: Queen tries to move one tile to the left (allowed)
game.move_queen_to(1, 2, 1, 1)
result = logic.is_column_direction_valid()
print_testcase("1.3.3.1 GameLogic.is_column_direction_valid -> legal movement one tile to the left: ", result, True)

# Testcase 1.3.3.2: Queen tries to move two tiles to the left (allowed)
game.move_queen_to(1, 2, 1, 0)
result = logic.is_column_direction_valid()
print_testcase("1.3.3.2 GameLogic.is_column_direction_valid -> legal movement two tiles to the left: ", result, True)

# Testcase 1.3.3.3: Queen tries to move three tiles to the left (forbidden)
game.move_queen_to(1, 4, 1, 1)
result = logic.is_column_direction_valid()
print_testcase("1.3.3.3 GameLogic.is_column_direction_valid -> illegal movement three tiles to the left: ", result, False)

# Testcase 1.3.3.4: Queen tries to move one tile to the right (allowed)
game.move_queen_to(1, 0, 1, 1)
result = logic.is_column_direction_valid()
print_testcase("1.3.3.4 GameLogic.is_column_direction_valid -> legal movement one tile to the right: ", result, True)

# Testcase 1.3.3.5: Queen tries to move two tiles to the right (allowed)
game.move_queen_to(1, 0, 1, 2)
result = logic.is_column_direction_valid()
print_testcase("1.3.3.5 GameLogic.is_column_direction_valid -> legal movement two tiles to the right: ", result, True)

# Testcase 1.3.3.6: Queen tries to move three tiles to the right (forbidden)
game.move_queen_to(1, 0, 1, 3)
result = logic.is_column_direction_valid()
print_testcase("1.3.3.6 GameLogic.is_column_direction_valid -> illegal movement three tiles to the right: ", result, False)



# 1.3.4 Destination tile is not occupied by another queen

# Testcase 1.3.4.1: Queen tries to move to a free tile (allowed)
game.move_queen_to(1, 0, 2, 0)
result = logic.is_move_blocked_by_queen()
print_testcase("1.3.4.1 GameLogic.is_move_blocked_by_queen -> legal movement to a free tile", result, False)

# Testcase 1.3.4.2: Queen tries to move to an already occupied tile (forbidden)
game.move_queen_to(1, 0, 5, 0)
result = logic.is_move_blocked_by_queen()
print_testcase("1.3.4.2 GameLogic.is_move_blocked_by_queen -> illegal movement to an already occupied tile", result, True)



# 1.3.5 CHECK FOR NON-HITTING MOVE

# Testcase 1.3.5.1: Queen moves only one tile to the left (non-hitting move)
game.move_queen_to(4, 1, 3, 0)
result = logic.is_standard_move()
print_testcase("1.3.5.1 GameLogic.is_standard_move -> move one tile to the left (non-hitting)", result, True)

# Testcase 1.3.5.2: Queen moves only one tile to the right (non-hitting move)
game.move_queen_to(4, 1, 3, 2)
result = logic.is_standard_move()
print_testcase("1.3.5.2 GameLogic.is_standard_move -> move one tile to the right (non-hitting)", result, True)

# Testcase 1.3.5.3: Queen moves more than one tile to the left (non-hitting move)
game.move_queen_to(4, 3, 2, 1)
result = logic.is_standard_move()
print_testcase("1.3.5.3 GameLogic.is_standard_move -> move more than one tile to the left (non-hitting)", result, False)

# Testcase 1.3.5.4: Queen moves more than one tile to the right (non-hitting move)
game.move_queen_to(4, 1, 2, 3)
result = logic.is_standard_move()
print_testcase("1.3.5.4 GameLogic.is_standard_move -> move more than one tile to the right (non-hitting)", result, False)

