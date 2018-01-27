#Составьте программу, которая рисует закрашенное кольцо.
#Радиус внешней окружности следует задавать в диалоге; 
from tkinter import *

window = Tk()
window.title('Ovals')
window.geometry('250x250')

canvas = Canvas(window, bg='white', width=250, height=250)
canvas.pack()

canvas.create_oval(5,90,245,140, fill="orange")
canvas.create_oval(90,5,160,245, fill="blue")





