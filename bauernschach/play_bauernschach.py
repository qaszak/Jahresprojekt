from board.board import Board


class Play_bauernschach():
    def __init__(self, page):
        spiel = "bauernschach"
        self.master = page
        #self.master.pack_forget()
        Board(page, spiel)


#page = Tk()
#Play_bauernschach(page)
