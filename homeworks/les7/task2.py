# -*- coding: utf-8 -*-
"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothing:
    def __init__(self, cloth_type, size: int):
        self.cloth_type = cloth_type
        self.size = size
        self.volume = 0

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if self.cloth_type == 'пальто':
            self.__volume = float(self.size/6.5 + 0.5)
        elif self.cloth_type == 'костюм':
            self.__volume = float(self.size * 2 + 0.3)
        else:
            self.__volume = 0

    @abstractmethod
    def get_volume(self):
        pass


class Suit(Clothing):
    def __init__(self, size: int):
        super().__init__('костюм', size)

    def get_volume(self):
        return f'На пошив костюма требуется {self.volume} ткани'


class Coat(Clothing):
    def __init__(self, size: int):
        super().__init__('пальто', size)

    def get_volume(self):
        return f'На пошив пальто требуется {self.volume} ткани'


new_suit = Suit(164)
new_coat = Coat(34)
print(new_suit.get_volume())
print(new_coat.get_volume())
