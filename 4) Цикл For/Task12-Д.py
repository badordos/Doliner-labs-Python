#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *

qwe = Tk()
qwe.title("12")
qwe.geometry('800x600')
asd = Canvas(qwe, bg='white', width=800, height=600)
asd.pack()
colors = ["#ffffff", "#ffcb99", "#97cc02", "#ff00fe", "#02007d"]

for i in range(5):
    asd.create_rectangle(i*100, 0, (i+1) * 100, 100, fill=colors[i])
