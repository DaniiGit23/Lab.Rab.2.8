#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def circle(radius):
    return math.pi * radius**2


def cylinder():
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))
    side = 2 * math.pi * radius * height
    command = input("Вы хотите получить полную площадь цилиндра? (Да/Нет): ")
    if command.lower() == 'да':
        circle_area = 2 * circle(radius)
        full_area = side + circle_area
        print("Полная площадь цилиндра равна", full_area)
    else:
        print("Площадь боковой поверхности цилиндра равна", side)


if __name__ == '__main__':
    cylinder()
