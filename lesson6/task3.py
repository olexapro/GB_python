
"""
    3.
    Реализовать базовый класс Worker (работник), в котором определить атрибуты:
    name, surname, position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
    оклад и премия, например, {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
    (get_total_income).
    Проверить работу примера на реальных данных
    (создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}


class Position(Worker):

    def get_total_income(self):
        print(f'{self.name} total income: ', int(self._income['wage']) + int(self._income['bonus']))

    def get_full_name(self):
        print(f'name: {self.name} \nsurname: {self.surname}')


w = Position('Alex', 'b', 'c', '10', '5')
w.get_full_name()
w.get_total_income()
