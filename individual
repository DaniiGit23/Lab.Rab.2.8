#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def input_data():
    """
    Функция для ввода данных в список из словарей заданной структуры
    """
    data = []
    while True:
        person = {}

        person['surname'] = input('Введите фамилию: ')
        person['name'] = input('Введите имя: ')
        person['phone_number'] = input('Введите номер телефона: ')

        birthdate = input('Введите дату рождения через пробел (день месяц год): ')
        birthdate = birthdate.split()
        birthdate = [int(i) for i in birthdate]
        person['birthdate'] = birthdate

        data.append(person)

        add_more = input('Хотите добавить еще одного человека? (да/нет) ')
        if add_more.lower() == 'нет':
            break

    # Сортировка по фамилии и имени
    data = sorted(data, key=lambda x: (x['surname'], x['name']))

    return data


def get_birthdays(data):
    """
    Функция для вывода информации о людях, чьи дни рождения приходятся на
    месяц, значение которого введено с клавиатуры
    """
    month = int(input('Введите месяц: '))

    birthdays = []
    for person in data:
        if person['birthdate'][1] == month:
            birthdays.append(person)

    if len(birthdays) == 0:
        print('Нет людей с таким днем рождения')
    else:
        print('Люди, у которых день рождения в выбранном месяце:')
        for person in birthdays:
            print(f"{person['surname']} {person['name']}: "
                  f"{person['birthdate'][0]}.{person['birthdate'][1]}.{person['birthdate'][2]}")


def main():
    """
    Основная функция
    """
    data = input_data()
    get_birthdays(data)


if __name__ == '__main__':
    main()
