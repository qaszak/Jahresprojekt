import Game

game = None

print("-- Welcome to Dame --\nCommands:\ns: start a new game\nm: move queen\nq: quit")

while True:
    user_input = input(": ")
    if user_input == "s":
        game = Game.Game(6)
        game.print_board()
    elif user_input == "m":
        current_row = int(input("\tcurrent_row: "))
        current_column = int(input("\tcurrent column: "))
        destination_row = int(input("\tdestination row: "))
        destination_column = int(input("\tdestination column: "))
        game.move_queen_to(current_row, current_column, destination_row, destination_column)
    elif user_input == "q":
        print("Bye.")
        break
    else:
        print("unknown command.\nCommands:\ns: start a new game\nm: move queen\nq: quit")

