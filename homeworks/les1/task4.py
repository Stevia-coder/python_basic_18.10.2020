"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = input('Введите целое положительное число\n>>>:')
max_number = int(number) % 10
number = int(number) // 10

while number > 1:
    next_number = int(number) % 10
    if next_number > max_number:
        max_number = next_number
    number = number // 10

print('Самая большая цифра в числе:', max_number)