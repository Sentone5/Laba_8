#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Напишите функцию, которая считывает с клавиатуры числа и перемножает их до тех пор, пока не будет введен 0.
# Функция должна возвращать полученное произведение. Вызовите функцию и выведите на экран результат ее работы.

def proiz():
    while True:
        a = int(input("a = "))
        b = int(input("b = "))

        if a == 0 or b == 0:
            break
        p = a*b
        pro = 0
        pro = pro + p
        print("Произведение чисел равно", pro)


if __name__ == '__main__':
    proiz()
