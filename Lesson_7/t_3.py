# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv(
# )).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не
# целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого
# числа.

class Cell:
    def __init__(self, nuc):
        self.nuc = nuc

    def __str__(self):
        return str(f'Ячейка имеет {self.nuc} клеток')

    def __add__(self, other):
        return Cell(self.nuc + other.nuc)

    def __sub__(self, other):
        return Cell(self.nuc - other.nuc if (self.nuc - other.nuc) > 0 else print('Отрицательно!'))

    def __mul__(self, other):
        return Cell(int(self.nuc * other.nuc))

    def __truediv__(self, other):
        return Cell(round(self.nuc // other.nuc))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.nuc / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        print(f'{"=" * 10}')
        row += f'{"*" * (self.nuc % cells_in_row)}'
        return row



cells1 = Cell(50)
cells2 = Cell(40)

print(cells1)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 / cells2)
print(cells1 * cells2)
print(cells2.make_order(8))
print(cells1.make_order(13))







