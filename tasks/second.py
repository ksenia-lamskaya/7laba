#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    numbers = [int(s) for s in (input('Введите элементы списка: ').split())]

    # 1. минимальный по модулю элемент списка
    min_abs = min(numbers, key=abs)
    print("Минимальный по модулю элемент списка:", abs(min_abs))

    # 2. сумма модулей элементов списка после первого элемента, равного нулю
    if 0 in numbers:
        zero_index = numbers.index(0)
        sum_abs = sum(abs(x) for x in numbers[zero_index+1:])
        print("Сумма модулей элементов списка, расположенных после первого элемента, равного нулю:", sum_abs)
    else:
        print("В списке нет элемента 0")

