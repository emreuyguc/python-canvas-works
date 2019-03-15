from Tkinter import *
import tkMessageBox
import time

top = Tk()

c = Canvas(top,bg="blue",height=250,width=300)

coord = 10,50,170,210

lab = Label(text="")
lab.pack()
c.pack()

for i in range(0,350,3):
    #lab["text"] = i
    time.sleep(0.15)
    #c.delete("all")
    arc = c.create_arc(coord,start=0,extent=i,fill="orange")
    top.update()
    


    
mainloop()
