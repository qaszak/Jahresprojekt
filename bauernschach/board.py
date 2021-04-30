##############                    #################
#######      JAHRESPROJEKT GROUP 3       ##########
##############                    #################
from random import choice
from tkinter import *

from bauernschach.bauernschach_logic import *
from bauernschach.dame_logic import Dame


class Board:

    def __init__(self, master, spiel):
        self.master = master
        ###  CHANGE SIZE OF THE BOARD AND THE WIDTH OF THE CASES HERE ###
        ###################
        self.spiel = spiel  ### which game bauernschach,dame, tic-tac-toe?
        self.BOARD_SIZE = 6  #
        self.BOARD_WIDTH = 96  #
        self.PAGE_WIDTH = 580  #
        self.PAGE_HEIGHT = 600  #
        self.COLOR1 = 'grey'  #
        self.COLOR2 = 'white'  #
        self.rand = 0  ####
        self.turn = 0
        ###################
        self.x1, self.y1, self.x2, self.y2 = self.rand, self.rand, self.BOARD_WIDTH + self.rand, \
                                             self.BOARD_WIDTH + self.rand
        self.color = self.COLOR1
        self.can = Canvas(self.master, width=self.PAGE_WIDTH, heigh=self.PAGE_HEIGHT, bg='ivory')

        b1 = Button(self.master, text='Play now', command=self.board)
        b1.pack(side=RIGHT, padx=3, pady=3)
        #bauern = Bauernschach(self.can, self.BOARD_WIDTH, self.BOARD_SIZE, self.rand)
        #b4 = Button(master, text='back', command=bauern.back())
        #b4.pack(side=RIGHT, padx=3, pady=3)
        b5 = Button(self.master, text='quit', command=self.quit)
        b5.pack(side=RIGHT, padx=3, pady=3)

        self.can.pack(side=TOP, padx=5, pady=5)

        master.mainloop()

    # create an empty board
    def board(self):
        ite, i = 0, 1

        while self.x1 < self.BOARD_WIDTH * self.BOARD_SIZE and self.y1 < self.BOARD_WIDTH * self.BOARD_SIZE:
            self.can.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)
            i, ite, self.x1, self.x2 = i + 1, ite + 1, self.x1 + self.BOARD_WIDTH, self.x2 + self.BOARD_WIDTH
            if ite == self.BOARD_SIZE:
                self.y1, self.y2 = self.y1 + self.BOARD_WIDTH, self.y2 + self.BOARD_WIDTH
                i, ite, self.x1, self.x2 = i + 1, 0, self.rand, self.BOARD_WIDTH + self.rand
            if i % 2 == 0:
                self.color = self.COLOR2
            else:
                self.color = self.COLOR1

        if self.spiel == "bauernschach":
            bauernschach = Bauernschach(self.can, self.BOARD_WIDTH, self.BOARD_SIZE, self.rand)
            bauernschach.fill_board_pawns()
        elif self.spiel == "dame":
            dame = Dame(self.can, self.BOARD_WIDTH, self.BOARD_SIZE, self.rand)
            dame.fill_board_queen()

    def quit(self):
        self.master.destroy()
