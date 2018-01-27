#Для иллюстрации дискретных динамических процессов довольно
#часто используются столбиковые диаграммы (гистограммы).  
#Составьте программу, которая по введенным данным строила
#бы такую гистограмму на экране.

import matplotlib.pyplot as plt
import numpy as np

x = []
l = []
n = int(input('Введите количество столбцов '))
for i in range(n):
    newKey = input('Введите имя столбца ')
    newValue = int(input('Введите значение cтолбца '))
    l.append(newKey)
    x.append(newValue)
        
    
y = np.arange(len(x))

plt.bar(y,x, align='center')
plt.xticks(y, l)
plt.show()
