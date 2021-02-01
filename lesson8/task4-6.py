"""
4. Начните работу над проектом «Склад оргтехники».
 Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 В базовом классе определить параметры, общие для приведенных типов.
 В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы,
 отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
 Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
 можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
 Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
 изученных на уроках по ООП.
"""

global_id = 0


class WrongValue(Exception):
    """An error occured"""
    pass


class OrgTechnic:
    """Baseclass for Technic
    Well actually i don't understood which specific parametres should have other childs of this class
    """
    def __init__(self,
                 name: str,
                 price: int,
                 size: int):

        global global_id
        try:
            if type(name) is str:
                self.name = name

            else:
                raise WrongValue

            if type(price) is int and type(size) is int:
                self.price = price
                self.size = size

            else:
                raise WrongValue

        except WrongValue:
            print('Atribute Error! please check all your parametres')

        self.item_id = global_id
        global_id += 1


class Warehouse:
    """Typical warehouse"""
    def __init__(self, capacity=100):
        # let's imagine that's dict it's a database link
        self.items_list = dict()

        self.capacity = capacity

    def add_to_list(self, cls):
        self.items_list[str(cls.item_id)] = cls


tec1 = OrgTechnic('hgad', 1000, 10)
tec2 = OrgTechnic('сканер', 1000, 10)
tec3 = OrgTechnic('ксерокс', 1000, 10)

w = Warehouse()
w.add_to_list(tec1)
w.add_to_list(tec2)
w.add_to_list(tec3)

for j in w.items_list:
    k = w.items_list[j]
    print(f'id: {j}\nname: {k.name}\nprice: {k.price}\nsize: {k.size}\n')
