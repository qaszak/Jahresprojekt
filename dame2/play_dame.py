from board.board import Board, Tk


class Test2():
    def __init__(self, master):
        spiel = "dame"
        Board(master, spiel,"easy")



page = Tk()
Test2(page)
