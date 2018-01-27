#Напишите программу вычисления стоимости покупки, состоящей из
#нескольких карандашей, линеек и тетрадей. Их количество и цену задать
#вводом. Ответ вывести в виде:
#Сумма к оплате: … руб … коп.
pencil = int(input('Сколько карандашей вы купили? '))
pencilPrice = float(input('Сколько стоит карандаш, 1шт? '))
ruler = int(input('Сколько линеек вы купили? '))
rulerPrice = float(input('Сколько стоит одна линейка? '))
notebook = int(input('Сколько тетрадей вы купили? '))
notebookPrice = float(input('Сколько стоит одна тетрадь? '))
sum = (pencil*pencilPrice)+(ruler*rulerPrice)+(notebook*notebookPrice)
sum = "%.2f" % sum
sumResult = str(sum)
sumResult = sumResult.split(".")
print ("Сумма к оплате:", sumResult[0],"руб",sumResult[1], "коп.")
input("\n\nНажмите Enter чтобы выйти")

