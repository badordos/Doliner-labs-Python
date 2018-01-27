#Создайте файл, содержащий фамилии студентов и их экзаменационные
#оценки по 5 предметам. Напишите программу печати фамилий студентов,
#сдавших экзамены только на "5". 

with open('exams.txt', 'r') as file:
    for line in file:
        if all([raiting[-1] == '5' for raiting in line[line.index('{') + 1:line.index('}')].split(', ')]):
            print(line[:line.index('=')].strip())
