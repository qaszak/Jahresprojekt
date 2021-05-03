from board.board import Board, Tk


class Play_bauernschach():
    def __init__(self, page, login, difficulty,player_stats_id):
        spiel = "bauernschach"
        self.master = page
        # self.master.pack_forget()
        Board(page, login, spiel, difficulty,player_stats_id)


#page = Tk()
#Play_bauernschach(page,"zak", "normal")
