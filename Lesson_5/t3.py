#3. Создать текстовый файл (не программно), построчно записать
#фамилии сотрудников и величину их окладов. Определить, кто из
#сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
#сотрудников. Выполнить подсчет средней величины дохода сотрудников.

import sys
import os
import json

def exe_3():
    dictionary = {}
    with open('text_3.txt', 'r') as f:
        for line in f:
            name, cash = line.split()
            dictionary[name] = float(cash)
        for key, value in dictionary.items():
            if value < 20000:
                print(f'Outsiders: {key} = {dictionary[key]}')
        print(f'Average cash is {sum(dictionary.values()) / len(dictionary):.2f}')
