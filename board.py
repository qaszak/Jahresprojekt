##############                    #################
#######      JAHRESPROJEKT GROUP 4       ##########
##############                    #################
from tkinter import *

###  CHANGE SIZE OF THE BOARD AND THE WIDTH OF THE CASES HERE ###
###################
BOARD_SIZE = 6  #
BOARD_WIDTH = 80  #
PAGE_WIDTH = 500  #
PAGE_HEIGH = 500  #
COLOR1 = 'grey'  #
COLOR2 = 'white'  #
###################


x1, y1, x2, y2 = 0, 0, BOARD_WIDTH, BOARD_WIDTH
color = COLOR1


# create an empty board
def board():
    global x1, x2, y1, y2, color
    ite, i = 0, 1

    while x1 < BOARD_WIDTH * BOARD_SIZE and y1 < BOARD_WIDTH * BOARD_SIZE:
        can.create_rectangle(x1, y1, x2, y2, fill=color)
        i, ite, x1, x2 = i + 1, ite + 1, x1 + BOARD_WIDTH, x2 + BOARD_WIDTH
        if ite == BOARD_SIZE:
            y1, y2 = y1 + BOARD_WIDTH, y2 + BOARD_WIDTH
            i, ite, x1, x2 = i + 1, 0, 0, BOARD_WIDTH
        if i % 2 == 0:
            color = COLOR2
        else:
            color = COLOR1


# draw the pawns on the KI side
def fill_board_KI_pawns():
    ite, x3, x4, y3, y4 = 0, BOARD_WIDTH / 5, BOARD_WIDTH / 5, BOARD_WIDTH - BOARD_WIDTH / 5, BOARD_WIDTH - BOARD_WIDTH / 5
    while ite < BOARD_SIZE:
        can.create_rectangle(x3, x4, y3, y4, fill='yellow')
        ite, x3, x4, y3, y4 = ite + 1, x3 + BOARD_WIDTH, x4, y3 + BOARD_WIDTH, y4


# draw the pawns on the player side
def fill_board_player_pawns():
    ite, x3, x4, y3, y4 = 0, BOARD_WIDTH / 5, BOARD_WIDTH * (
            BOARD_SIZE - 1) + BOARD_WIDTH / 5, BOARD_WIDTH - BOARD_WIDTH / 5, BOARD_WIDTH * BOARD_SIZE - BOARD_WIDTH / 5

    while ite < BOARD_SIZE:
        can.create_oval(x3, x4, y3, y4, fill='red')
        ite, x3, x4, y3, y4 = ite + 1, x3 + BOARD_WIDTH, x4, y3 + BOARD_WIDTH, y4


# fill the board with both KI and player pawns
def fill_board_pawns():
    fill_board_player_pawns()
    fill_board_KI_pawns()


def fill_board_queen():
    fill_board_KI_queen()
    fill_board_player_queen()


def fill_board_KI_queen():
    ite, x3, x4, y3, y4 = 0, BOARD_WIDTH / 5, BOARD_WIDTH / 5, BOARD_WIDTH - BOARD_WIDTH / 5, BOARD_WIDTH - BOARD_WIDTH / 5
    i = 0
    while i < 6:
        can.create_rectangle(x3, x4, y3, y4, fill='yellow')
        i, ite, x3, x4, y3, y4 = i + 1, ite + 2, x3 + BOARD_WIDTH * 2, x4, y3 + BOARD_WIDTH * 2, y4
        if ite == 6:
            ite, x3, x4, y3, y4 = 0, BOARD_WIDTH / 5 + BOARD_WIDTH, BOARD_WIDTH + BOARD_WIDTH / 5, BOARD_WIDTH - BOARD_WIDTH / 5 + BOARD_WIDTH, \
                                  BOARD_WIDTH * 2 - BOARD_WIDTH / 5



def fill_board_player_queen():
    ite, x3, x4, y3, y4 = 0, BOARD_WIDTH / 5, BOARD_WIDTH * (
            BOARD_SIZE - 2) + BOARD_WIDTH / 5, BOARD_WIDTH - BOARD_WIDTH / 5, BOARD_WIDTH * (BOARD_SIZE-1) - BOARD_WIDTH / 5
    i=0
    while i < BOARD_SIZE:
        can.create_oval(x3, x4, y3, y4, fill='red')
        i,ite, x3, x4, y3, y4 = i+1,ite + 2, x3 + BOARD_WIDTH*2, x4, y3 + BOARD_WIDTH*2, y4
        if ite == 6:
            ite, x3, x4, y3, y4 = 0 , BOARD_WIDTH / 5+ BOARD_WIDTH, BOARD_WIDTH * (BOARD_SIZE - 2) + BOARD_WIDTH / 5 + BOARD_WIDTH\
                , BOARD_WIDTH - BOARD_WIDTH / 5 + BOARD_WIDTH,  BOARD_WIDTH * BOARD_SIZE - BOARD_WIDTH / 5

page = Tk()
can = Canvas(page, width=PAGE_WIDTH, heigh=PAGE_HEIGH, bg='ivory')
b1 = Button(page, text='Create Game', command=board)
b2 = Button(page, text='start Bauernschach ', command=fill_board_pawns)
b3 = Button(page, text='start dame ', command=fill_board_queen)
can.pack(side=TOP, padx=5, pady=5)
b1.pack(side=LEFT, padx=3, pady=3)
b2.pack(side=RIGHT, padx=3, pady=3)
b3.pack(side=RIGHT, padx=3, pady=3)
page.mainloop()
