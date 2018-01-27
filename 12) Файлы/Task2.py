#Напишите программу, которая считывает текстовый файл,
#выравнивает его содержимое по правой границе и выводит
#результат в другой текстовый файл.

e = open('output.txt','w')
with open('input.txt','r') as f:
    for line in f:
        e.write('{:>50}'.format(line.strip())+ '\n')
f.close()
e.close()
input("\n\nНажмите Enter чтобы выйти")
