#7. Создать (не программно) текстовый файл, в котором
#каждая строка должна содержать данные о фирме: название,
#форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой
#компании, а также среднюю прибыль. Если фирма получила убытки,
#в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами
#и их прибылями, а также словарь со средней прибылью. Если фирма
#получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
#{“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.

import sys
import os
import json

def exe_7():
    my_list = []
    frm_list = {}

    with open('text_7.txt', 'r') as f:
        for line in f:
            name, form, cash, costs = line.split()
            frm_list[name] = int(cash) - int(costs)
        a_cash = [i for i in frm_list.values() if i > 0]
        avr_list = {'Average': int(sum(a_cash) / len(a_cash))}
        my_list.append(frm_list), my_list.append(avr_list)

    with open('text_7.json', 'w') as fl:
        json.dump(my_list, fl, indent=4, ensure_ascii=False)

    with open('text_7.json', 'r') as fq:
        print(fq.read())

