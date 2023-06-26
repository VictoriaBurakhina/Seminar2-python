#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

#number = int(input("Введите целое число "))
#h = hex(number)
#print(h)


number = int(input('Введите любое число : '))
digit = number
numericStr = '0123456789ABCDEF'
str = ''
while digit > 0:
    str = numericStr[digit % 16] + str
    digit = digit // 16
print(f'Число {number} в 16-ой системе - {str}')
print('Проверка hex() - ', hex(number))