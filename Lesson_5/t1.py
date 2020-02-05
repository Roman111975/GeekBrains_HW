#1. Создать программно файл в текстовом формате, записать
#в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.

import sys
import os
import json

def t_1():
    with open('text_1.txt', 'w+') as f:
        while True:
            a = input("Enter str: ")
            if not a:
                break
            f.write(f'{a}\n')
