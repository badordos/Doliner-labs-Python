#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *

qwe = Tk()
qwe.title("12")
qwe.geometry('800x600')
asd = Canvas(qwe, bg='white', width=800, height=600)
asd.pack()
colors = ["#fffe9a", "#01ffff", "#2cced1", "#7b047c", "#808080"]

j=400
k=400
for i in range(5):
    asd.create_rectangle(k, j, k + 100, j - 100, fill=colors[i])
    j -= 50
    k +=50
