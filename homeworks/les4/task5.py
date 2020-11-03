"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""
import operator
from functools import reduce


new_list = [el for el in range(100, 1000) if el % 2 == 0]
result = reduce(operator.mul, new_list)
print(result)
