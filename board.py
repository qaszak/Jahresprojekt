from tkinter import *

BOARD_SIZE=6
BOARD_WIDTH=80
PAGE_WIDTH=500
PAGE_HEIGH=500
COLOR1='grey'
COLOR2='white'

x1,y1,x2,y2=0,0,BOARD_WIDTH,BOARD_WIDTH
color=COLOR1

def board():
    global x1,x2,y1,y2,color
    ite,i=0,1
    while x1<BOARD_WIDTH*BOARD_SIZE and y1<BOARD_WIDTH*BOARD_SIZE:
        can.create_rectangle(x1,y1,x2,y2,fill=color)
        i,ite,x1,x2=i+1,ite+1,x1+BOARD_WIDTH,x2+BOARD_WIDTH
        if ite == BOARD_SIZE:
            y1,y2=y1+BOARD_WIDTH,y2+BOARD_WIDTH
            i,ite,x1,x2=i+1,0,0,BOARD_WIDTH
        if i%2 == 0:
            color=COLOR2
        else: color=COLOR1


page=Tk()
can=Canvas(page,width=PAGE_WIDTH,heigh=PAGE_HEIGH,bg='ivory')
b1=Button(page,text='Create Game',command=board)
can.pack(side=TOP,padx=5,pady=5)
b1.pack(side=LEFT,padx=3,pady=3)
page.mainloop()