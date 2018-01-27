#Напишите программу печати слов предложения в обратном порядке

s = input('Введите предложение: ')

mylist=list(map(str,s.split()))
print (' '.join(map(str,reversed(mylist))))
