# 6. Расписание звонков. В учебном заведении задается начало учебного
# дня, продолжительность «пары» или урока, продолжительность
# обычного и большого перерывов (и их «место» в расписании),
# количество пар (уроково). Составить программу, которая выведет на
# экран расписание звонков на весь учебный день.


startDayH = int(input("Начало учебного дня (часы): "))
startDayM = int(input("Начало учебного дня (минуты): "))
lessonDurationM = int(input("Продолжительность урока(в минутах): "))
standartIntervalM = int(input("Продолжительность обычного перерыва(в минутах): "))
bigIntervalM = int(input("Продолжительность большого перерыва(в минутах): "))
indexBigInterval = int(input("Позиция большого перерыва: "))
countLessons = int(input("Кол-во уроков: "))


for i in range(1, countLessons+1):
    print("%20s" % ("Урок №" + str(i)))
    print("Начало в", str(startDayH)+":"+str(startDayM))
    startDayM += lessonDurationM
    if startDayM >= 60:
        startDayH +=  int(startDayM/60)
        startDayM = startDayM%60
    print("Конец в", str(startDayH)+":"+str(startDayM))
    print("")
    if i != countLessons:
        print("Начало перерыва в:", str(startDayH)+":"+str(startDayM))

        if i != indexBigInterval:
            startDayM += standartIntervalM
        else:
            startDayM += bigIntervalM

        if startDayM >= 60:
            startDayH +=  int(startDayM/60)
            startDayM = startDayM%60

        print("Конец перерыва в:", str(startDayH)+":"+str(startDayM))
        print("")
