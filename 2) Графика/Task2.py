#Составьте программу, которая рисует закрашенное кольцо.
#Радиус внешней окружности следует задавать в диалоге; 
from tkinter import *

window = Tk()
window.title('Surname')
window.geometry('800x600')

canvas = Canvas(window, bg='white', width=800, height=600)
canvas.pack()

canvas.create_text(400,300, fill="green", font="TimesNewRoman", text="Ярлыков")





