"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

def my_func(arg1, arg2, arg3):
    new_list = [arg1, arg2, arg3]
    return sum(new_list) - min(new_list)

print(my_func(2.34, 5, 1.1))