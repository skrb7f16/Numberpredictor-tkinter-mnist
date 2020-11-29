from tkinter import *
from PIL import Image,ImageDraw,ImageGrab
import checking
from tkinter import messagebox


canvas_width = 500
canvas_height = 500
white = (255, 255, 255)
green = (0,128,0)


def paint( event ):
   x1, y1 = ( event.x - 20 ), ( event.y - 20 )
   x2, y2 = ( event.x + 20 ), ( event.y + 20 )
   w.create_oval( x1, y1, x2, y2, fill = 'black' )


def saveImg():
    x=master.winfo_rootx()+w.winfo_x()+60
    y=master.winfo_rooty()+w.winfo_y()+50
    x1=x+w.winfo_width()
    y1=y+w.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save("tel.png")
    number=checking.check('tel.png')
    messagebox.showinfo("Number found!!",f"{number} is the number you drew. if not Sorry :'(")
    w.delete(ALL)


master = Tk()
master.title( "Draw the number with mouse" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height,bg='white')
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM, fill=X )
button=Button(message,text="Predict",command=saveImg).pack(side=LEFT)  
mainloop()



