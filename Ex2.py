#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Напечатать все символы, расположенные между первой и второй
# запятыми. Если второй запятой нет, то должны быть напечатаны все символы,
# расположенные после единственной имеющейся запятой.

if __name__ == '__main__':
    s = list(input("Введите предложение ").split(','))
    print(s[1])
