"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

one, two = input('Введите два числа через пробел\n>').split(' ')

def my_func(arg_1, arg_2):
    try:
        arg = arg_1 / arg_2
    except ZeroDivisionError:
        return 0
    return arg

print(round(my_func(int(one), int(two)), 2))