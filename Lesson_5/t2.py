#2. Создать текстовый файл (не программно),
#сохранить в нем колько строк, выполнить подсчет
#количества строк, количества слов в каждой строке.

import sys
import os
import json

def exe_2():
    with open('text_2.txt', 'r') as f:
        print(f.read())
        f.seek(0, 0)
        print(f'Кол-во слов: {len(f.read().split())}')
        f.seek(0, 0)
        print(f'Кол-во строк: {len(f.read().splitlines())}')