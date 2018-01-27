#10. Построить окружность, состоящую из 6 секторов, раскрашенных в
#разные цвета.

from tkinter import *

qwe = Tk()
qwe.title("Круг")
qwe.geometry('300x300')
asd = Canvas(qwe, bg='white', width=300, height=300)
asd.pack()
colors = ["green", "red", "lightblue", "magenta", "yellow", "blue"]

for i in range(6):
    j = 60*i
    asd.create_arc(100, 100, 250, 250, start=j, extent=60, fill=colors[i])
