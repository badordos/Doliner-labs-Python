#Составьте программу, которая рисует закрашенное кольцо.
#Радиус внешней окружности следует задавать в диалоге; 
from tkinter import *

window = Tk()
window.title('Ring')
window.geometry('300x300')

canvas = Canvas(window, bg='white', width=300, height=300)

r = int(input('Введите внешний радиус кольца'))

canvas.create_oval(150-r,150-r,150+r,150+r, fill='white',outline="black", width=10+r)
canvas.pack()


