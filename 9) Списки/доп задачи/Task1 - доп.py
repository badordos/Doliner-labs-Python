#Определить, имеются ли в заданном списке одинаковые элементы

L = ['a','b','c','b']
if len(L) != len(set(L)):
    print ('В списке имеются одинаковые элементы')
else: print('В списке нет одинаковых элементов')
