##############                    #################
#######      JAHRESPROJEKT GROUP 3       ##########
##############                    #################

from bauernschach.bauernschach_logic import *
from dame.dame_logic import Dame


class Board:

    def __init__(self, master, spiel, login, difficulty, id_player_stat):
        self.master = master
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        ###  CHANGE SIZE OF THE BOARD AND THE WIDTH OF THE CASES HERE ###
        ###################
        self.spiel = spiel  ### which game bauernschach,dame, tic-tac-toe?
        self.BOARD_SIZE = 6  #
        self.BOARD_WIDTH = 90  #
        self.PAGE_WIDTH = 800  #
        self.PAGE_HEIGHT = 600  #
        self.COLOR1 = 'grey'  #
        self.COLOR2 = 'white'  #
        self.rand = 0  ####
        self.turn = 0
        ###################
        self.x1, self.y1, self.x2, self.y2 = self.rand, self.rand, self.BOARD_WIDTH + self.rand, \
                                             self.BOARD_WIDTH + self.rand
        self.color = self.COLOR1
        # self.can = Canvas(self.master, width=self.PAGE_WIDTH, heigh=self.PAGE_HEIGHT, bg='ivory')
        self.can = self.background()
        # b1 = Button(self.master, text='Play now', command=self.board)
        # b1.pack(side=RIGHT, padx=3, pady=3)
        self.board(login, difficulty, id_player_stat)
        # bauern = Bauernschach(self.can, self.BOARD_WIDTH, self.BOARD_SIZE, self.rand)
        # bauernschach_logic=Bauernschach(self.can,self.BOARD_WIDTH,self.BOARD_SIZE,self.rand,difficulty)

        b5 = Button(self.master, text='quit', command=self.quit)
        b5.pack(side=RIGHT, padx=3, pady=3)

        self.can.pack(side=TOP, padx=5, pady=5)

        master.mainloop()

    def background(self):
        background_color_primary = "#96bfd6"
        background_color_secondary = "#3f6d8c"
        background_square_primary_color = "#96bfd6"
        background_square_secondary_color = "#87b0c7"
        background_square_size = 16

        ### Widgets
        window_background = Canvas(self.master, width=800, height=600, bg=background_color_primary)

        # Checkerboard Pattern for Background
        for i in range(0, self.WINDOW_WIDTH, background_square_size):
            for j in range(0, self.WINDOW_HEIGHT, background_square_size):
                if (i / background_square_size) % 2 == 0:
                    if (j / background_square_size) % 2 == 0:
                        window_background.create_rectangle(i, j, i + background_square_size,
                                                           j + background_square_size,
                                                           fill=background_square_primary_color,
                                                           outline=background_square_primary_color)
                    else:
                        window_background.create_rectangle(i, j, i + background_square_size,
                                                           j + background_square_size,
                                                           fill=background_square_secondary_color,
                                                           outline=background_square_secondary_color)
                else:
                    if (j / background_square_size) % 2 == 0:
                        window_background.create_rectangle(i, j, i + background_square_size,
                                                           j + background_square_size,
                                                           fill=background_square_secondary_color,
                                                           outline=background_square_secondary_color)
                    else:
                        window_background.create_rectangle(i, j, i + background_square_size,
                                                           j + background_square_size,
                                                           fill=background_square_primary_color,
                                                           outline=background_square_primary_color)

        # window_background.create_rectangle(150, 175, 640, 500, fill=background_color_secondary)
        # window_background.place(x=0, y=0)
        return window_background

    # create an empty board
    def board(self, login, difficulty, id_player_stat):
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
            bauernschach = Bauernschach(self.can, self.BOARD_WIDTH, self.BOARD_SIZE, self.rand, login, difficulty,
                                        id_player_stat)
            bauernschach.fill_board_pawns()
        elif self.spiel == "dame":
            dame = Dame(self.can, self.BOARD_WIDTH, self.BOARD_SIZE, self.rand)
            dame.fill_board_queen()

    def quit(self):
        self.master.destroy()
