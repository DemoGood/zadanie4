#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    k, j = 0, 0
    s = input("Введите предложение: ")

    for i in s:
        j += 1  # Четность итерации
        # Буквы "и" стоящие на четных местах
        if (i == 'и') and (j % 2 == 0):
            print(i)
            k += 1  # счетчик букв "и" на четных местах

    # Если счетчик пуст, то в предложении нет "и" на четных местах
    if k == 0:
        print("В предложении нет 'и' стоящих на четных местах.")
