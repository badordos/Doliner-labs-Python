#Составьте программу-переводчик, которая на основе имеющего словаря
#будет переводить предложения. В случае, если подобного слова нет в словаре,
#программа должна запросить это слово и его перевод 

import shelve
db=shelve.open('db_file')
while True:
    inp = (input('Введите предожение для перевода с английского на русский: '))
    words=inp.split()
    translate = list
    for i in words:
        if db.get(i) == None:
            print (i,'- слова нет в базе')
            newValue = input('Введите перевод: ')
            db[i] = newValue
            db.update()
        else: print ('Перевод: ',i,':',(db.get(i)))
