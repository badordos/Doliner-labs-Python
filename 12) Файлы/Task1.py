# Напишите программу на языке Python, которая считывает из Интернета файл с
#информацией архив, видео, музыку и т.п.). 


import urllib.request

url = input('Введите ссылку на файл')
fileName = input('Введите название файла')

urllib.request.urlretrieve(url, fileName)
