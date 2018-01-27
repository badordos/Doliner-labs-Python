#Составьте программу, которая рисует фигуру, состоящую из окружности
#и прямоугольника с закруглеными углами. Толщина линий – 5 точек,
#яркого цвета, такой же, как на рисунке, штриховки.
#Фигура расположена в центре окна 250×150 точек.  
from tkinter import *

window = Tk()
window.title('Figure')
window.geometry('250x150')

canvas = Canvas(window, bg='white', width=250, height=150)
canvas.pack()

canvas.create_oval(55,10,195,145, fill='purple',outline="black",width=5)
canvas.create_polygon([5,10],[10,5],[235,5],[240,10],[240,75],[235,80],[10,80],[5,75],
                      fill="yellow",outline="black", width=5, smooth=0)
