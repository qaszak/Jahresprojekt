import board
from tkinter import *

# last selected pawn
last_selected = [0, 0]

# player and ki pawns position [column , line]
player_pawns_position = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]
KI_pawns_position = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]


page = Tk()
spiel = "bauernschach"
board.Board(page, spiel, player_pawns_position, KI_pawns_position)
