import Dame

dame = None

print("-- Welcome to Dame --\nn: new game\nq: quit")

while True:
    command = input("(n) new game or (q) quit : ")
    if command == "n":
        dame = Dame.Dame()
        print(dame.get_print_of_board())

        while True:
            command_2 = input("(s) select queen, (p) print board or (q) quit game: ")
            if command_2 == "q":
                break
            elif command_2 == "p":
                print(dame.get_print_of_board())
            elif command_2 == "s":
                # Select Queen
                print("\n\tSelect a queen")
                queen_row = int(input("\t\trow: "))
                queen_column = int(input("\t\tcolumn: "))
                print(dame.get_print_of_possible_moves(queen_row, queen_column))
                while True:
                    command_3 = input("\n(m) move selected queen, (u) unselect queen: ")
                    if command_3 == "u":
                        break
                    elif command_3 == "m":
                        queen_row = int(input("\t\tmove to row: "))
                        queen_column = int(input("\t\tmove to column: "))
                        dame.execute_player_move_for(queen_row, queen_column)
                        break
                    else:
                        print("Unknown command")
            else:
                print("Unknown command")

            print(dame.get_print_of_board())
            winner = dame.get_winner()
            if winner != "":
                print(str(winner) + " wins")
                quit()

    elif command == "q":
        print("Bye.")
        break
    else:
        print("unknown command")
