#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *

qwe = Tk()
qwe.title("12")
qwe.geometry('800x600')
asd = Canvas(qwe, bg='white', width=800, height=600)
asd.pack()
colors = ["#ffcb99", "#ffffff", "#329a67", "#cc99fe", "#7e0100"]
for i in range(5):
    asd.create_oval(i*100+1, 2, (i+1) * 100, 102, fill=colors[i])
