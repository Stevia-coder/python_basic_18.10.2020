# -*- coding: utf-8 -*-
"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
"""

from random import randint


class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return self.make_order(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count > 0:
            return self.make_order(self.count - other.count)
        else:
            return f'Разница меньше 0'

    def __mul__(self, other):
        return self.make_order(self.count * other.count)

    def __truediv__(self, other):
        truediv = int(self.count / other.count)
        return self.make_order(truediv)

    def make_order(self, size, cell_strip=5):
        new_string = ''
        while size // cell_strip != 0:
            new_string += '*' * cell_strip
            new_string += '\n'
            size -= cell_strip
        new_string += '*' * size
        return new_string


cell1 = Cell(randint(1, 30))
cell2 = Cell(randint(1, 30))
print(cell1 + cell2)
print(1)
print(cell1 - cell2)
print(1)
print(cell1 / cell2)
print(1)
print(cell1 * cell2)
