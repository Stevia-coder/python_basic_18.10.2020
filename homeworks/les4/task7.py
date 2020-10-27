"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""
from math import factorial


def fact(n):
    factor = factorial(n)
    return factor


def generator(n):
    for el1 in range(1, n+1):
        yield fact(el1)


g = generator(5)

for el in g:
    print(el)
