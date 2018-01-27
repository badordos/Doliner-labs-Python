#Напишите программу, которая считывает исходный текст программы
#на языке Python и подставляет номера строк (в виде комментариев)
#в начало каждой строки файла с исходным текстом


temp = []
file = open('example.py', 'r')
for line in file.read().split('\n'):
    temp.append(line)

file.close()

file1 = open('example.py', 'w')
i = 1
for line in temp:
    newline = "#{0} {1}".format(i, line)+'\n'
    file1.write(newline)
    i = i+1

file1.close()
