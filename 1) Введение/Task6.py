#6. Даны координаты двух точек. Вычислите расстояние между ними.
import math
x1 = float(input('Введите координату Х первой точки '))
y1 = float(input('Введите координату Y первой точки '))
x2 = float(input('Введите координату Х второй точки '))
y2 = float(input('Введите координату Y второй точки '))
d = math.sqrt (((x2-x1)**2)+((y2-y1)**2))
print('Расстояние между двумя точками = ',d)
input("\n\nНажмите Enter чтобы выйти")

