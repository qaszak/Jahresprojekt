from tkinter import *

ROWS = 6
COLUMNS = 6
SQUARE_SIZE = 70

window = Tk()
window.title('Dame')

canvas = Canvas(window, bg='lightgray', height=(ROWS) * SQUARE_SIZE, width=(COLUMNS) * SQUARE_SIZE)
canvas.pack(side=TOP, padx=20, pady=20)

white_field = True
x = 1
y = 1
for rows in range(ROWS):
    for columns in range(COLUMNS):
        color = "white"
        if not white_field:
            color = "black"
        x = columns*SQUARE_SIZE
        y = rows*SQUARE_SIZE
        canvas.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=color)
        white_field = not white_field
    white_field = not white_field

button = Button(window, text='quit game', width=10, command=window.quit)
button.pack(side=RIGHT, padx=10, pady=10)

window.mainloop()