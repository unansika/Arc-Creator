#import

from tkinter import *

#variables

x1 = 0
x2 = 0
x3 = 0
x4 = 0
d = 0

#function to create arc

def create_arc():

    #get variables from entries

    x1 = e1.get()
    x1 = int(x1)
    y1 = e2.get()
    y1 = int(y1)
    x2 = e3.get()
    x2 = int(x2)
    y2 = e4.get()
    y2 = int(y2)
    d = e5.get()
    d = int(d)
    coord = x1, y1, x2, y2

    #canvas window & arc creation

    window_new = Tk()
    window_new.geometry('800x800')
    window_new.title('Arc Creator 1.0')

    c = Canvas(window_new,height = 800,
               width = 800,
               bg = 'white')

    c.pack()

    arc = c.create_arc((coord),
                       start = 0,
                       extent = d,
                       fill = 'white')

    window_new.mainloop()

#start Window


window = Tk()
window.geometry('400x200')
window.title('Arc Creator 1.0')

button_createarc = Button(window,
                          text = 'Create arc',
                          command = create_arc)
button_createarc.grid(column = 2,row = 12)

label = Label(window, text = 'Enter Value x1')
label.grid(column = 0,row = 0)

label2 = Label(window, text = 'Enter Value y1')
label2.grid(column = 0,row = 2)

label3 = Label(window, text = 'Enter value x2')
label3.grid(column = 0,row = 4)

label4 = Label(window, text = 'Enter value y2')
label4.grid(column = 0,row = 6)

label5 = Label(window, text = 'Enter degrees of extension')
label5.grid(column = 0,row = 8)

e1 = Entry(window)
e1.grid(column = 4,row = 0)

e2 = Entry(window)
e2.grid(column = 4,row = 2)

e3 = Entry(window)
e3.grid(column = 4,row = 4)

e4 = Entry(window)
e4.grid(column = 4,row = 6)

e5 = Entry(window)
e5.grid(column = 4,row = 8)

window.mainloop()