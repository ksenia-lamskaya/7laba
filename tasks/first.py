#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    print('Введите элементы списка: ')
    lst = [input() for _ in range(10)]
    element = input('Введите элемент: ')
    index = []

    for ind, value in enumerate(lst):
        if value == element:
            index.append(ind)

    if len(index) == 0:
        print("Такого элемента в списке нет")
    else:
        print('Индексы этого элемента: ')
        [print(i) for i in index]
