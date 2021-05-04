from board.board import Board, Tk


class Play_bauernschach():
    def __init__(self, page, login, difficulty, id_player_stat):
        spiel = "bauernschach"
        self.master = page
        # self.master.pack_forget()
        Board(page, spiel,login, difficulty, id_player_stat)

#page = Tk()
#Play_bauernschach(page,"zak", "normal")
