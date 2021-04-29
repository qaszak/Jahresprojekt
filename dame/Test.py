import Game

game = None

print("-- Welcome to Dame --\nn: new game\nq: quit")

while True:
    command = input("(n) new game or (q) quit : ")
    if command == "n":
        game = Game.Game(6)
        game.print_board()
        print()

        while True:
            command_2 = input("(s) select queen, (p) print board or (q) quit game: ")
            if command_2 == "q":
                break
            elif command_2 == "p":
                print()
                game.print_board()
                print()
            elif command_2 == "s":
                # Select Queen
                print("\n\tSelect a queen")
                queen_row = int(input("\t\trow: "))
                queen_column = int(input("\t\tcolumn: "))
                game.get_moves_for_queen_at(queen_row, queen_column)
                game.print_possible_moves()
                while True:
                    command_3 = input("\n(m) move selected queen, (u) unselect queen: ")
                    if command_3 == "u":
                        break
                    elif command_3 == "m":
                        winner = game.get_winner()
                        if winner != -1:
                            print("Player " + str(winner) + " wins")
                            quit()
                        queen_row = int(input("\t\tmove to row: "))
                        queen_column = int(input("\t\tmove to column: "))
                        if game.execute_move(queen_row, queen_column):
                            print()
                            game.print_board()
                            print()
                        else:
                            print("\tinvalid move")
                        break
                    else:
                        print("Unknown command")
            else:
                print("Unknown command")
    elif command == "q":
        print("Bye.")
        break
    else:
        print("unknown command")
