import Tkinter

pnc = Tkinter.Tk()

def ciz():
    c.delete("all")
    coord = int(ex0.get()),int(ex1.get()),int(ey0.get()),int(ey1.get())
    c.create_line(coord,fill="orange")
    
def solaa():
    gnc = int(ex0.get())-10
    ex0.delete(0,'end')
    ex0.insert(0,gnc)
    gnc2 = int(ey0.get())-10
    ey0.delete(0,'end')
    ey0.insert(0,gnc2)
    ciz()

def sols(event):
    solaa()
    
def sags(event):
    sagaa()
    
def yukaris(event):
    yukariya()
    
def asags(event):
    asagiya()

def yukariya():
    gnc = int(ex1.get())-10
    ex1.delete(0,'end')
    ex1.insert(0,gnc)
    gnc2 = int(ey1.get())-10
    ey1.delete(0,'end')
    ey1.insert(0,gnc2)
    ciz()

def asagiya():
    gnc = int(ex1.get())+10
    ex1.delete(0,'end')
    ex1.insert(0,gnc)
    gnc2 = int(ey1.get())+10
    ey1.delete(0,'end')
    ey1.insert(0,gnc2)
    ciz()

def sagaa():
    gnc = int(ex0.get())+10
    ex0.delete(0,'end')
    ex0.insert(0,gnc)
    gnc2 = int(ey0.get())+10
    ey0.delete(0,'end')
    ey0.insert(0,gnc2)
    ciz()

cizdir = Tkinter.Button(text="ciz",command=ciz)
cizdir.pack()

saga = Tkinter.Button(text="saga",command=sagaa)
saga.pack()

sola = Tkinter.Button(text="sola",command=solaa)
sola.pack()

yukari = Tkinter.Button(text="yukari",command=yukariya)
yukari.pack()

asag = Tkinter.Button(text="asag",command=asagiya)
asag.pack()

lx0 = Tkinter.Label(text="x0:") 
ex0 = Tkinter.Entry()
lx0.pack()
ex0.pack()

lx1 = Tkinter.Label(text="x1:")
ex1 = Tkinter.Entry()
lx1.pack()
ex1.pack()

ly0 = Tkinter.Label(text="y0:")
ey0 = Tkinter.Entry()
ly0.pack()
ey0.pack()

ly1 = Tkinter.Label(text="y1:")
ey1 = Tkinter.Entry()
ly1.pack()
ey1.pack()

lstart = Tkinter.Label(text="start:")
estart = Tkinter.Entry()
lstart.pack()
estart.pack()

lextent = Tkinter.Label(text="extent:")
eextent = Tkinter.Entry()
lextent.pack()
eextent.pack()

c = Tkinter.Canvas(pnc,bg="blue",height=400,width=500)
c.pack()


frame = Tkinter.Frame(pnc, width=400, height=500)
pnc.bind("<Left>",sols)
pnc.bind("<Right>",sags)
pnc.bind("<Up>",yukaris)
pnc.bind("<Down>",asags)
frame.pack()

Tkinter.mainloop()
