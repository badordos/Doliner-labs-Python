#8. Длина некоторого отрезка составляет p метров. Напишите программу
#перевода ее в русскую неметрическую систему. Указание: 1 верста = 500
#саженей, 1 сажень = 3 аршина, 1 аршин = 16 вершков, 1 вершок = 44,45 мм.
p = float(input('Длина отрезка в метрах = '))
vershok = p/0.04445
arshin = vershok/16
sazhen = arshin/3
versta = sazhen/500
print('Длина отрезка равна:', "%.2f" % versta,'верст, либо', "%.2f" % sazhen,
      'саженей либо,', "%.2f" % arshin,'аршин, либо', "%.2f" % vershok,'вершков.')
input("\n\nНажмите Enter чтобы выйти")

