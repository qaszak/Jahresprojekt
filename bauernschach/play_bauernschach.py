from board.board import Board, Tk


class Play_bauernschach():
    def __init__(self, page, difficulty):
        spiel = "bauernschach"
        self.master = page
        # self.master.pack_forget()
        Board(page, spiel, difficulty)

#page = Tk()
#Play_bauernschach(page,"normal")
