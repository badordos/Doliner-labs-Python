#В списке хранятся года рождения некоторого числа людей.
#Составьте программу, которая определит разницу в возрасте
#между самым старшим и самым младшим из этого списка. Считать,
#что возраст можно определить как разность между текущим годом
#и их годом рождения. 

L = [1961,1984,1992,1939,1947,1998]
y = 2018
young = y - max(L)
old = y - min(L)
result = old - young
print('Разница в возрасте между самым старщим и самым младщим равна',
      result,'лет')
    
