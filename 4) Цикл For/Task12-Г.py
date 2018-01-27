#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *

qwe = Tk()
qwe.title("12")
qwe.geometry('800x600')
asd = Canvas(qwe, bg='white', width=800, height=600)
asd.pack()
colors = ["#003466", "#017f02", "#97cb04", "#ffffff"]

for i in range(4):
    asd.create_oval(2, i*100+1, 102, (i+1) * 100, fill=colors[i])
