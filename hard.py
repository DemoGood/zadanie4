#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s1 = ''
    s = input("Введите предложение: ")

    for i in reversed(s):
        s1 += i

    print(s1)
