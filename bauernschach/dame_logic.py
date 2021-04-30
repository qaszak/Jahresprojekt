
class Dame():
    def __init__(self, can, B_W, B_S, rand):
        # the highlighted square
        self.highlighted_square = []
        # the last played move player
        self.played_move_player = [[-1, -1], [-1, -1]]
        # the last played move KI
        self.played_move_KI = [[-1, -1], [-1, -1]]
        # last selected pawn
        self.last_selected = [-1, -1]

        # last possible moves
        self.last_possible_moves = [[-1, -1]]

        self.can = can
        self.BOARD_WIDTH = B_W
        self.BOARD_SIZE = B_S
        self.rand = rand
        self.spiel = "dame"
        self.last_selected = [0, 0]
        size = 6
        # player and ki pawns position [column , line]
        # player_pawns_position = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]
        # KI_pawns_position = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
        self.player_pawns_position = []
        self.KI_pawns_position = []
        i = 0
        while i < 2:
            j = 0
            while j < size:
                self.player_pawns_position.append([j + i, size + i - 2])
                self.KI_pawns_position.append([i, j + i])
                j = j + 2
            i = i + 1

        ###################################################################################################################
        ################################ FILL THE BOARD WITH QUEENS #######################################################
        ###################################################################################################################
        def fill_board_queen(self):
            self.fill_board_KI_queen()
            self.fill_board_player_queen()

        def fill_board_KI_queen(self):
            ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.rand, self.BOARD_WIDTH / 5 \
                                                      + self.rand, self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.rand, \
                                                      self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.rand
            i = 0
            while i < 6:
                self.can.create_rectangle(self.x3, self.x4, self.y3, self.y4, fill='yellow')
                i, ite, self.x3, self.x4, self.y3, self.y4 = i + 1, ite + 2, self.x3 + self.BOARD_WIDTH * 2, \
                                                             self.x4, self.y3 + self.BOARD_WIDTH * 2, self.y4
                if ite == 6:
                    ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + self.rand, \
                                                              self.BOARD_WIDTH + self.BOARD_WIDTH / 5 + self.rand, \
                                                              self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + \
                                                              self.rand, \
                                                              self.BOARD_WIDTH * 2 - self.BOARD_WIDTH / 5 + self.rand

        def fill_board_player_queen(self):
            ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.rand, self.BOARD_WIDTH * (
                    self.BOARD_SIZE - 2) + self.BOARD_WIDTH / 5 + self.rand, self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + \
                                                      self.rand, self.BOARD_WIDTH * (
                                                              self.BOARD_SIZE - 1) - self.BOARD_WIDTH / 5 + self.rand
            i = 0
            while i < self.BOARD_SIZE:
                self.can.create_oval(self.x3, self.x4, self.y3, self.y4, fill='red')
                i, ite, self.x3, self.x4, self.y3, self.y4 = i + 1, ite + 2, self.x3 + self.BOARD_WIDTH * 2, \
                                                             self.x4, self.y3 + self.BOARD_WIDTH * 2, self.y4
                if ite == 6:
                    ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + \
                                                              self.rand, self.BOARD_WIDTH * (self.BOARD_SIZE - 2) + \
                                                              self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + self.rand, \
                                                              self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + \
                                                              self.rand, self.BOARD_WIDTH * self.BOARD_SIZE - \
                                                              self.BOARD_WIDTH / 5 + self.rand

    ###################################################################################################################
    ################################ FILL THE BOARD WITH QUEENS #######################################################
    ###################################################################################################################
    def fill_board_queen(self):
        self.fill_board_KI_queen()
        self.fill_board_player_queen()

    def fill_board_KI_queen(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.rand, self.BOARD_WIDTH / 5 \
                                                  + self.rand, self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.rand, \
                                                  self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.rand
        i = 0
        while i < 6:
            self.can.create_rectangle(self.x3, self.x4, self.y3, self.y4, fill='yellow')
            i, ite, self.x3, self.x4, self.y3, self.y4 = i + 1, ite + 2, self.x3 + self.BOARD_WIDTH * 2, \
                                                         self.x4, self.y3 + self.BOARD_WIDTH * 2, self.y4
            if ite == 6:
                ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + self.rand, \
                                                          self.BOARD_WIDTH + self.BOARD_WIDTH / 5 + self.rand, \
                                                          self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + \
                                                          self.rand, \
                                                          self.BOARD_WIDTH * 2 - self.BOARD_WIDTH / 5 + self.rand

    def fill_board_player_queen(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.rand, self.BOARD_WIDTH * (
                self.BOARD_SIZE - 2) + self.BOARD_WIDTH / 5 + self.rand, self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + \
                                                  self.rand, self.BOARD_WIDTH * (
                                                          self.BOARD_SIZE - 1) - self.BOARD_WIDTH / 5 + self.rand
        i = 0
        while i < self.BOARD_SIZE:
            self.can.create_oval(self.x3, self.x4, self.y3, self.y4, fill='red')
            i, ite, self.x3, self.x4, self.y3, self.y4 = i + 1, ite + 2, self.x3 + self.BOARD_WIDTH * 2, \
                                                         self.x4, self.y3 + self.BOARD_WIDTH * 2, self.y4
            if ite == 6:
                ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + \
                                                          self.rand, self.BOARD_WIDTH * (self.BOARD_SIZE - 2) + \
                                                          self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + self.rand, \
                                                          self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.BOARD_WIDTH + \
                                                          self.rand, self.BOARD_WIDTH * self.BOARD_SIZE - \
                                                          self.BOARD_WIDTH / 5 + self.rand
