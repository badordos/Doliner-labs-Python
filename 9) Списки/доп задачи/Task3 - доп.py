#В списке рост юношей задан отрицательным числом, рост девушек – положительным.
#Определите отдельно средний рост юношей и девушек

L = [150, 168, -182, -174, 178, -175, -165, 185, -190, 172, 164]

girls = []
boys = []
for i in L:
    if i < 0:
        boys.append(i)
    elif i > 0:
        girls.append(i)

resBoys = -(sum(boys)/len(boys))
resGirls = sum(girls)/len(girls)
print('Средний рост юношей = ',resBoys)
print('Средний рост девушек = ',resGirls)

        
