# -*- coding: utf-8 -*-
"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen
(ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    pass

    def draw(self):
        print('Новая ручка')


class Pencil(Stationery):
    pass

    def draw(self):
        print('Возьми лучше карандаш')


class Handle(Stationery):
    pass

    def draw(self):
        print('Этот маркер не отмывается')


new_pen = Pen('Лучший')
new_pen.draw()
new_pencil = Pencil('Гибкий')
new_pencil.draw()
new_handle = Handle('Стойкий')
new_handle.draw()

