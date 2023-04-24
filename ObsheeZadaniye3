#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Введите значение: ")


def test_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(value):
    return int(value)


def print_int(value):
    print(f"Введенное значение: {value}")


# Основная ветка программы
if __name__ == '__main__':
    value = get_input()
    if test_input(value):
        value_int = str_to_int(value)
        print_int(value_int)
    else:
        print("Ошибка: введенное значение не является целым числом")
