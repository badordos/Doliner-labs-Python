#Составить программу рисования следующей последовательности однотипных фигур

from tkinter import *

qwe = Tk()
qwe.title("12")
qwe.geometry('800x600')
asd = Canvas(qwe, bg='white', width=800, height=600)
asd.pack()
colors = ["#ffcb99", "#feff01", "#01ff00", "#963463", "#808080"]

j=10
for i in range(5):
    asd.create_rectangle(j, j, j + 100, j + 100, fill=colors[i])    
    j += 50
