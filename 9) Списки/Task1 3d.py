from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
dz = []
n = int(input('Введите количество столбцов '))
for i in range(n):
    newKey = int(input('Введите числовое наименование столбца '))
    newValue = int(input('Введите значение cтолбца '))
    x.append(newKey)
    dz.append(newValue)

col = input('Введите цвет столбцов ')

y = [0]*len(x); z = [0]*len(x); dx = 0.6; dy = 0.5

ax.bar3d(x, y, z, dx, dy, dz, color=col, zorder='max')
# adding labels
for xx,yy,zz in zip(x,y,dz):
    ax.text(xx,yy+dy/2,zz*1.025, str(zz),
            family='monospace', size='larger', weight='bold', color='b')
ax.bar3d(x, 1, z, 0, 0.5, 0, color='white', zorder=-1)
plt.xticks(x, x)
plt.yticks(y, y)

plt.show()
