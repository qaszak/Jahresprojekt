from board.board import Board, Tk


class Play_dame():
    def __init__(self, page, login, difficulty, id_player_stat):
        spiel = "dame"
        self.master = page
        # self.master.pack_forget()
        Board(page, spiel,login, difficulty, id_player_stat)


