#5. Средняя наценка на товар составляет 18%. Пусть известна розничная цена
#товара. Вычислите оптовую цену.
price = float(input('Введите розничную цену на товар = '))
opt = price - (price/100*18)
print(opt)
input("\n\nНажмите Enter чтобы выйти")

