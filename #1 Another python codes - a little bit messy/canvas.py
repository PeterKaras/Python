import tkinter as tk
from tkinter import *

"""master = tk.Tk()

tk.Label(master,text="First input").grid(row=1)
tk.Label(master,text="SECOND input").grid(row=2)
e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=1,column=1)
e2.grid(row=2,column=1)"""
"""width = 1000
height = 800
w = Canvas(master,width = width,height =height)
w.pack()
e1 = Entry(canvas)"""
"""

hlavny = tk.Button(text='Zadajte skóre', command="bb", bg='yellow', fg='black', font=('helvetica', 9, 'bold'))
#master.create_window(900, 400, window=hlavny)
#self.entry1 = tk.Entry(root)
#canvas1.create_window(900, 370, window=self.entry1)
"""
master = Tk()
canvas = Canvas(master,width=1500,height=900)
canvas.pack()
canvas.create_line(10,10,10,880)
canvas.create_line(10,10,1480,10)
canvas.create_line(1480,10,1480,880)
canvas.create_line(1480,880,10,880)

zaciatok = 30+10
for i in range(50):
    canvas.create_line(zaciatok,10,zaciatok,880)
    zaciatok += 30

zaciatok = 30+10
for i in range(50):
    canvas.create_line(10,zaciatok,1480,zaciatok)
    zaciatok += 30
    
