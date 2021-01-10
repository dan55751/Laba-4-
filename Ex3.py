#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово из 12 букв. Переставить его буквы следующим способом: первая, двенадцатая,
# вторая, одиннадцатая, ..., пятая, восьмая, шестая, седьмая

if __name__ == '__main__':
    word = input("Введите слово из 12 букв ")
    word = word.replace(word[0], word[11], 1)
    word = word.replace(word[1], word[10], 1)
    word = word.replace(word[2], word[9], 1)
    word = word.replace(word[3], word[8], 1)
    word = word.replace(word[4], word[7], 1)
    word = word.replace(word[5], word[6], 1)
    print(word)