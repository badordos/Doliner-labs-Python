#Разработайте простейший тренажер, который проверяет умение решать
#линейные уравнения вида ax=b

from random import *
while True:
    a = randint(1,10)
    b = randint(1,1000)
    x = int(b/a)    
    print('Решите уравнение:',a,'*x=',b)
    print('Ответ округлите до целого числа')
    q = int(input('Ответ: '))
    if x==q:
        print('Верно')
    else: print('Неверно')
