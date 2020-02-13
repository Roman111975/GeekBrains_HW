# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.


class Cloth:
    def __init__(self):
        pass

    
    def cost(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def cost(self):
        return self.size / 6.5 + 0.5


class Jacet(Cloth):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def cost(self):
        return self.height * 2 + 0.3



coat = Coat(42)
jac = Jacet(39)

print(f'Размер пальто: {coat.size} Ткани на пальто: {coat.cost:.2f}m')
print(f'Размер пиджака: {jac.height} Ткани на пиджак: {jac.cost:.2f}m')
print(f'Общее кол-во на две вещи: {coat.cost + jac.cost:.2f}')