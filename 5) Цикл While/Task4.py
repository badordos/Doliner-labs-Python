#Дано натуральное число. Определить сумму его цифр

x = int(input('Введите натуральное число '))
s=0

while x>0:
    s=s+(x%10)
    x = x//10

print('Сумма его цифр',s)   
