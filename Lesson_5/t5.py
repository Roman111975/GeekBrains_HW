#5. Создать (программно) текстовый файл, записать в него
#программно набор чисел, разделенных пробелами. Программа
#должна подсчитывать сумму чисел в файле и выводить ее на экран.

import sys
import os
import json


def exe_5():
    with open('text_5.txt', 'w+') as f:
        num = [1,2,3,4,5,6,7,8,9,10]
        f.writelines(' '.join(list(map(str, num))))
        f.seek(0, 0)
        print(f'Original list: {f.read()}')
        print(f'Sum numbers: {sum(num)}')