
"""
    2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
     Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
     К типам одежды в этом проекте относятся пальто и костюм.
     У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
     Это могут быть обычные числа: V и H, соответственно.

    Для определения расхода ткани по каждому типу одежды использовать формулы:
     для пальто (V/6.5 + 0.5),
     для костюма (2 * H + 0.3).
     - Проверить работу этих методов на реальных данных.
     - Реализовать общий подсчет расхода ткани.
     - Проверить на практике полученные на этом уроке знания:
     - реализовать абстрактные классы для основных классов проекта,
     - проверить на практике работу декоратора @property.

"""

from abc import abstractmethod


class Cloth:
    def __init__(self, name, size):
        self._size = size
        self.name = name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @abstractmethod
    def count(self):
        pass


class Coat(Cloth):
    def count(self):
        return self.size / 6.5 + 0.5


class Suit(Cloth):
    def count(self):
        return 2 * self.size + 0.3


coat = Coat('Пальто', 10)
print(coat.size)
coat._size = 100
print(coat.size)
print(coat.count(), coat.name)
print()

coat = Suit('Костюм', 10)
print(coat.size)
coat._size = 100
print(coat.size)
print(coat.count(), coat.name)
