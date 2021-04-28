##############                    #################
#######      JAHRESPROJEKT GROUP 4       ##########
##############                    #################
from tkinter import *


class Board:

    def __init__(self, master, spiel, player_pawns_position, KI_pawns_position):
        # the last played move
        self.played_move = [[-1, -1], [-1, -1]]
        # last selected pawn
        self.last_selected = [-1, -1]

        # last possible moves
        self.last_possible_moves = [[-1, -1]]

        # player and ki pawns position [column , line]
        self.player_pawns_position = player_pawns_position
        self.KI_pawns_position = KI_pawns_position
        ###  CHANGE SIZE OF THE BOARD AND THE WIDTH OF THE CASES HERE ###
        ###################
        self.spiel = spiel  ### which game bauernschach,dame, tic-tac-toe?
        self.BOARD_SIZE = 6  #
        self.BOARD_WIDTH = 80  #
        self.PAGE_WIDTH = 500  #
        self.PAGE_HEIGHT = 500  #
        self.COLOR1 = 'grey'  #
        self.COLOR2 = 'white'  #
        ###################
        self.x1, self.y1, self.x2, self.y2 = 0, 0, self.BOARD_WIDTH, self.BOARD_WIDTH
        self.color = self.COLOR1
        self.can = Canvas(master, width=self.PAGE_WIDTH, heigh=self.PAGE_HEIGHT, bg='ivory')
        b1 = Button(master, text='Create Game', command=self.board)
        if self.spiel == "bauernschach":
            b2 = Button(master, text='start Bauernschach ', command=self.fill_board_pawns)
            b2.pack(side=RIGHT, padx=3, pady=3)
        if self.spiel == "dame":
            b3 = Button(master, text='start dame ', command=self.fill_board_queen)
            b3.pack(side=RIGHT, padx=3, pady=3)
        self.can.pack(side=TOP, padx=5, pady=5)
        b1.pack(side=LEFT, padx=3, pady=3)
        master.mainloop()

    # create an empty board
    def board(self):
        ite, i = 0, 1

        while self.x1 < self.BOARD_WIDTH * self.BOARD_SIZE and self.y1 < self.BOARD_WIDTH * self.BOARD_SIZE:
            self.can.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)
            i, ite, self.x1, self.x2 = i + 1, ite + 1, self.x1 + self.BOARD_WIDTH, self.x2 + self.BOARD_WIDTH
            if ite == self.BOARD_SIZE:
                self.y1, self.y2 = self.y1 + self.BOARD_WIDTH, self.y2 + self.BOARD_WIDTH
                i, ite, self.x1, self.x2 = i + 1, 0, 0, self.BOARD_WIDTH
            if i % 2 == 0:
                self.color = self.COLOR2
            else:
                self.color = self.COLOR1

    # draw the pawns on the KI side
    def fill_board_KI_pawns(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5, self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5
        while ite < self.BOARD_SIZE:
            self.can.create_rectangle(self.x3, self.x4, self.y3, self.y4, fill='yellow')
            ite, self.x3, self.x4, self.y3, self.y4 = ite + 1, self.x3 + self.BOARD_WIDTH, self.x4, self.y3 + self.BOARD_WIDTH, self.y4

    # draw the pawns on the player side
    def fill_board_player_pawns(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5, self.BOARD_WIDTH * (
                self.BOARD_SIZE - 1) + self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5, self.BOARD_WIDTH * self.BOARD_SIZE - self.BOARD_WIDTH / 5

        while ite < self.BOARD_SIZE:
            obj1 = self.can.create_oval(self.x3, self.x4, self.y3, self.y4, fill='red')
            if self.spiel == "bauernschach":
                self.can.tag_bind(obj1, "<Button-1>", self.show_possible_moves)
            ite, self.x3, self.x4, self.y3, self.y4 = ite + 1, self.x3 + self.BOARD_WIDTH, self.x4, self.y3 + self.BOARD_WIDTH, self.y4

    # fill the board with both KI and player pawns
    def fill_board_pawns(self):
        self.fill_board_player_pawns()
        self.fill_board_KI_pawns()

    def fill_board_queen(self):
        self.fill_board_KI_queen()
        self.fill_board_player_queen()

    def fill_board_KI_queen(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5, self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5
        i = 0
        while i < 6:
            self.can.create_rectangle(self.x3, self.x4, self.y3, self.y4, fill='yellow')
            i, ite, self.x3, self.x4, self.y3, self.y4 = i + 1, ite + 2, self.x3 + self.BOARD_WIDTH * 2, self.x4, self.y3 + self.BOARD_WIDTH * 2, self.y4
            if ite == 6:
                ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.BOARD_WIDTH, self.BOARD_WIDTH + self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.BOARD_WIDTH, \
                                                          self.BOARD_WIDTH * 2 - self.BOARD_WIDTH / 5

    def fill_board_player_queen(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5, self.BOARD_WIDTH * (
                self.BOARD_SIZE - 2) + self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5, self.BOARD_WIDTH * (
                                                          self.BOARD_SIZE - 1) - self.BOARD_WIDTH / 5
        i = 0
        while i < self.BOARD_SIZE:
            self.can.create_oval(self.x3, self.x4, self.y3, self.y4, fill='red')
            i, ite, self.x3, self.x4, self.y3, self.y4 = i + 1, ite + 2, self.x3 + self.BOARD_WIDTH * 2, self.x4, self.y3 + self.BOARD_WIDTH * 2, self.y4
            if ite == 6:
                ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.BOARD_WIDTH, self.BOARD_WIDTH * (
                        self.BOARD_SIZE - 2) + self.BOARD_WIDTH / 5 + self.BOARD_WIDTH \
                    , self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.BOARD_WIDTH, self.BOARD_WIDTH * self.BOARD_SIZE - self.BOARD_WIDTH / 5

    def removeSelectionFromOthers(self):
        i = self.last_selected[0]
        j = self.last_selected[1]
        if i == -1: return
        print(" i   j  ", i, j)
        self.can.create_rectangle(i * self.BOARD_WIDTH, j * self.BOARD_WIDTH, (i + 1) * self.BOARD_WIDTH,
                                  (j + 1) * self.BOARD_WIDTH, outline='black')
        col = self.last_possible_moves[0][0]
        line = self.last_possible_moves[0][1]

        if (col + line) % 2 == 0:
            c = 'grey'
        else:
            c = 'white'
        print("last possible moves col   line  ", col, line, c)
        self.can.create_rectangle(col * self.BOARD_WIDTH, line * self.BOARD_WIDTH, (col + 1) * self.BOARD_WIDTH,
                                  (line + 1) * self.BOARD_WIDTH, fill=c)

    def selected_square(self, x, y):
        col = int(x / self.BOARD_WIDTH)
        line = int(y / self.BOARD_WIDTH)
        self.removeSelectionFromOthers()
        self.last_selected = [col, line]
        print("selected square ", col, line)
        self.can.create_rectangle(col * self.BOARD_WIDTH, line * self.BOARD_WIDTH, (col + 1) * self.BOARD_WIDTH,
                                  (line + 1) * self.BOARD_WIDTH,
                                  outline='red')
        self.possible_moves()

    def possible_moves(self):
        col = self.last_selected[0]
        line = self.last_selected[1] - 1
        self.last_possible_moves = [[col, line]]
        print("last possible moves 1 col   line  ", col, line)
        obj1 = self.can.create_rectangle(col * self.BOARD_WIDTH, line * self.BOARD_WIDTH, (col + 1) * self.BOARD_WIDTH,
                                         (line + 1) * self.BOARD_WIDTH, fill='green')
        self.can.tag_bind(obj1, "<Button-1>", self.play_move)

    def show_possible_moves(self, event):
        # print('Clicked', event.x, event.y, event.widget, )
        # print(event.widget.find_closest(event.x, event.y))
        self.selected_square(event.x, event.y)

    def play_move(self, event):
        print('Clicked', event.x, event.y, event.widget, )
        print(event.widget.find_closest(event.x, event.y))
        col = int(event.x / self.BOARD_WIDTH)
        line = int(event.y / self.BOARD_WIDTH)
        self.played_move = [[self.last_selected[0], self.last_selected[1]], [col, line]]

        if (self.last_selected[0] + self.last_selected[1]) % 2 == 0:
            c_rectangle = 'grey'
        else:
            c_rectangle = 'white'

        if (col + line) % 2 == 0:
            c_oval = 'grey'
        else:
            c_oval = 'white'

        print("the played move col   line  ", col, line)
        # remove the highlight from the possible square
        self.can.create_rectangle(col * self.BOARD_WIDTH, line * self.BOARD_WIDTH, (col + 1) * self.BOARD_WIDTH,
                                  (line + 1) * self.BOARD_WIDTH, fill=c_oval)

        # draw a new oval in the played square
        t=self.BOARD_WIDTH/5
        obj1 = self.can.create_oval(col * self.BOARD_WIDTH +t, line * self.BOARD_WIDTH+t, (col + 1) * self.BOARD_WIDTH-t,
                                    (line + 1) * self.BOARD_WIDTH-t, fill='red')
        self.can.tag_bind(obj1, "<Button-1>", self.show_possible_moves)
        # remove the old oval from the last position
        line = line + 1
        self.can.create_rectangle(col * self.BOARD_WIDTH, line * self.BOARD_WIDTH, (col + 1) * self.BOARD_WIDTH,
                                  (line + 1) * self.BOARD_WIDTH, fill=c_rectangle)
        # initialise the last selected Square
        self.last_selected = [-1, -1]

        # modify the player's pawn position
        self.player_pawns_position[col] = [col, line - 1]
