#Напишите программу, переводящую время, указанное в минутах, во время в
#часах и минутах.
min = int(input('Укажите количество минут: '))
hours = min // 60
minutes = min % 60
print ("Это равняется: ", hours, "часов и ", minutes,"минут")
input("\n\nНажмите Enter чтобы выйти")

