# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class AbsClothes(ABC):

    def __init__(self, param, name):
        self.param = int(param)
        self.name = str(name)
        self.consumption = 0

    @abstractmethod
    def show(self):
        pass

class Clothes(AbsClothes):

    list_of_consumption = []

    @classmethod
    def summ(cls):
        return f'Текущий расход ткани на все представленные изделия составляет {round(sum(cls.list_of_consumption), 2)} кв. м'

class Coat(Clothes):

    def __init__(self, param, name):
        super().__init__(param, name)

    @property
    def calc_coat_consumption(self):
        self.consumption = self.param / 6.5 + 0.5
        Clothes.list_of_consumption.append(self.consumption)
        return f'Расход ткани на пальто типа {self.name} составит {self.consumption:.2f} кв. м'

    @property
    def show(self):
        print(f'Представлено пальто под названием {self.name}, размера {self.param:}')

class Suit(Clothes):

    def __init__(self, param, name):
        self.param = float(param)
        self.name = name

    @property
    def calc_suit_consumption(self):
        self.consumption = self.param * 2 + 0.3
        Clothes.list_of_consumption.append(self.consumption)
        return f'Расход ткани на костюм типа {self.name} составит {self.consumption:.2f} кв. м'

    @property
    def show(self):
        print(f'Представлен костюм под названием {self.name}, рассчитанный для роста {self.param} м')

coat = Coat(50, 'Coaty')
coat.show
print(coat.calc_coat_consumption)
suit = Suit(2.02, 'Suity')
suit.show
print(suit.calc_suit_consumption)
print(Clothes.summ())