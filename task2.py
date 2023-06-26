#Задача 2.
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# #Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


import fractions
str1 = str(input('Введите дробь вида числитель/знаменатель : '))
str2 = str(input('Введите вторую дробь вида числитель/знаменатель: '))
first = str1.split('/')
second = str2.split('/')
summa = str(int(first[0]) * int(second[1]) + int(first[1]) * int(second[0])) + '/' + str(int(second[1]) * int(first[1]))
mult = str( int(first[0]) * int( second[0])) + '/' + str ( int(first[1]) * int(second[1]))
print(f'Сумма {summa}, Произведение {mult}')
f1 = fractions.Fraction(int(first[0]), int(first[1]))
f2 = fractions.Fraction(int(second[0]), int(second[1]))
print(f'Проверка Fractions сумма {f1+f2}, произведение {f1*f2}')