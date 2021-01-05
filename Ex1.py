#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Составить программу, которая печатает «столбиком» все вхождения в
# предложение некоторого символа

if __name__ == '__main__':
    sentence = list(input("Введите предложение ").split())
    symbol = input("Введите символ который хотите проверить ")
    for i in range(len(sentence)):
        if sentence[i].count(symbol) == 1:
            print(sentence[i])
