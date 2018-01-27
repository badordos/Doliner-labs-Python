#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *

qwe = Tk()
qwe.title("12")
qwe.geometry('800x800')
asd = Canvas(qwe, bg='white', width=800, height=800)
asd.pack()
colors = ["#ffffff", "#9acb00", "#0200f7", "#993400"]

j=10
for i in range(4):
    asd.create_oval(j, j, j*i + 100, j*i + 100, fill=colors[i])    
    j += 30
