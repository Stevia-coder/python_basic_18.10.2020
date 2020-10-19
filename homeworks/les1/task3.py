"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

number_one = input('Введите число\n>>>:')
number_two = number_one * 2
number_three = number_one * 3
print(int(number_one) + int(number_two) + int(number_three))