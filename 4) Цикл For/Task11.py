#11. Составить программу рисования мишени, состоящей из окружностей
#разного цвета.

from tkinter import *

qwe = Tk()
qwe.title("Круг")
qwe.geometry('800x600')
asd = Canvas(qwe, bg='white', width=800, height=600)
asd.pack()
colors = ["green", "red", "lightblue", "magenta", "yellow", "blue"]

for i in range(1, 7):
    asd.create_oval(200 + i*20, 200 + i*20, 460 - i*20, 460 - i*20,
                    fill=colors[i-1])
