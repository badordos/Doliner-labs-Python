#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *

qwe = Tk()
qwe.title("12")
qwe.geometry('800x600')
asd = Canvas(qwe, bg='white', width=800, height=600)
asd.pack()
colors = ["#ffffff", "#ffd206", "#32cdc7", "#a12e69", "#810000"]

j=10
for i in range(5):
    asd.create_oval(j, j, j + 100, j + 100, fill=colors[i])    
    j += 30
