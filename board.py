##############                    #################
#######      JAHRESPROJEKT GROUP 4       ##########
##############                    #################
from tkinter import *
import numpy as np

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

# last selected pawn
last_selected = [0, 0]

# player and ki pawns position [column , line]
player_pawns_position = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]
KI_pawns_position = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]


def removeSelectionFromOthers():
    i = last_selected[0]
    j = last_selected[1]
    print(" i   j  ", i, j)
    can.create_rectangle(i * BOARD_WIDTH, j * BOARD_WIDTH, (i + 1) * BOARD_WIDTH,
                         (j + 1) * BOARD_WIDTH, outline='black')


def selectedCase(x, y):
    global last_selected
    col = int(x / BOARD_WIDTH)
    line = int(y / BOARD_WIDTH)
    removeSelectionFromOthers()
    last_selected = [col, line]
    print(col, line)
    can.create_rectangle(col * BOARD_WIDTH, line * BOARD_WIDTH, (col + 1) * BOARD_WIDTH, (line + 1) * BOARD_WIDTH,
                         outline='red')


def onObjectClick(event):
    print('Clicked', event.x, event.y, event.widget, )
    print(event.widget.find_closest(event.x, event.y))
    selectedCase(event.x, event.y)


# create an empty board
def board():
    global x1, x2, y1, y2, color, board
    ite, i = 0, 1
    board = np.empty((0, 4), int)
    while x1 < BOARD_WIDTH * BOARD_SIZE and y1 < BOARD_WIDTH * BOARD_SIZE:
        obj1 = can.create_rectangle(x1, y1, x2, y2, fill=color)
        board = np.append(board, np.array([[x1, y1, x2, y2]]), axis=0)
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
        obj1 = can.create_oval(x3, x4, y3, y4, fill='red')
        can.tag_bind(obj1, "<Button-1>", onObjectClick)
        ite, x3, x4, y3, y4 = ite + 1, x3 + BOARD_WIDTH, x4, y3 + BOARD_WIDTH, y4


# fill the board with both KI and player pawns
def fill_board_pawns():
    fill_board_player_pawns()
    fill_board_KI_pawns()
    print(board)


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
            BOARD_SIZE - 2) + BOARD_WIDTH / 5, BOARD_WIDTH - BOARD_WIDTH / 5, BOARD_WIDTH * (
                                  BOARD_SIZE - 1) - BOARD_WIDTH / 5
    i = 0
    while i < BOARD_SIZE:
        can.create_oval(x3, x4, y3, y4, fill='red')
        i, ite, x3, x4, y3, y4 = i + 1, ite + 2, x3 + BOARD_WIDTH * 2, x4, y3 + BOARD_WIDTH * 2, y4
        if ite == 6:
            ite, x3, x4, y3, y4 = 0, BOARD_WIDTH / 5 + BOARD_WIDTH, BOARD_WIDTH * (
                    BOARD_SIZE - 2) + BOARD_WIDTH / 5 + BOARD_WIDTH \
                , BOARD_WIDTH - BOARD_WIDTH / 5 + BOARD_WIDTH, BOARD_WIDTH * BOARD_SIZE - BOARD_WIDTH / 5


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
