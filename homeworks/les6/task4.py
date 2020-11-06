# -*- coding: utf-8 -*-
"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'left':
            print('Поворот на лево')
        else:
            print('Поворот на право')

    def show_speed(self):
        print(f'Скорость {self.speed}')


class TownCar(Car):
    pass

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена на {self.speed - 60}')
        else:
            print(f'Скорость {self.speed}')

class SportCar(Car):
    pass


class WorkCar(Car):
    pass

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена на {self.speed - 40}')
        else:
            print(f'Скорость {self.speed}')


class PoliceCar(Car):
    pass


japan = TownCar(70, 'blue', 'Subaru cool', False)
ferrari = SportCar(150, 'red', 'Formula1', False)
worker = WorkCar(35, 'grey', 'TakeOne', False)
police = PoliceCar(90, 'white', 'SuperCop', True)

print(japan.color)
print(police.speed)
print(worker.is_police)

japan.show_speed()
ferrari.show_speed()
worker.show_speed()
police.show_speed()

japan.go()
japan.turn('left')
japan.turn('right')
japan.stop()
