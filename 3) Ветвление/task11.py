# Составьте программу, которые вводит три числа и определяет,
#является ли треугольник со сторонами данной длины прямоугольным.

import math
a=int(input('Введите сторону А треугольника'))
b=int(input('Введите сторону B треугольника'))
c=int(input('Введите сторону C треугольника'))

if (math.sqrt(a)+math.sqrt(b)==math.sqrt(c) or
    math.sqrt(a)+math.sqrt(c)==math.sqrt(b) or
    math.sqrt(c)+math.sqrt(b)==math.sqrt(a)):
    print ('Треугольник является прямоугольным')
else: print('Треугольник НЕ является прямоугольным')
