#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *

qwe = Tk()
qwe.title("12")
qwe.geometry('800x600')
asd = Canvas(qwe, bg='white', width=800, height=600)
asd.pack()
colors = ["#ffffff", "#ffce00", "#7f8000", "#353396"]

for i in range(4):
    asd.create_rectangle(0, i*100, 100, (i+1) * 100, fill=colors[i])
