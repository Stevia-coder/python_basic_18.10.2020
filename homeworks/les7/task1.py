# -*- coding: utf-8 -*-
"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, *args):
        self.matrix = []
        for el in args:
            self.matrix.append(el)

    def __str__(self):
        for el in self.matrix:
            return f'{el} \n'

    def __add__(self, other):
        new_matrix = []
        for el in range(0, self.str_length(self.matrix)):
            self_matrix_el = self.matrix[el]
            other_matrix_el = other.matrix[el]
            new_line = []
            for item in range(0, self.str_length(self_matrix_el)):
                new_line.append(self_matrix_el[item] + other_matrix_el[item])
            new_matrix.append(new_line)
        return new_matrix

    def str_length(self, self_list):
        return len(self_list)


mat1 = Matrix([1, 2, 3], [4, 5, 6])
mat2 = Matrix([8, 9, 10], [32, 23, 13])

print(mat1+mat2)
