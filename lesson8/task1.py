
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода:
 - Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
 - Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных.
"""


class Date:
    """
        input type:string day month year
        example: '01 12 2021'
    """

    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @classmethod
    def get_as_days(cls, date):
        if cls.is_valid(date):
            date = date.split(' ')
            day = int(date[0])
            month = (int(date[1])-1)*31
            year = int(date[2]) * 365
            return day + month + year

        else:
            return None

    @staticmethod
    def is_valid(date):
        try:
            date_param = date.split(' ')
            if 0 <= int(date_param[0]) <= 31 and 0 <= int(date_param[1]) <= 12:
                return True
            else:
                return False

        except Exception as excp:
            print(type(excp))
            return False

        finally:
            del date_param


c1 = Date('10 111 2000')
c2 = Date('11 11 2020')

for i in [c1, c2]:
    print(i)
    print(i.date)
    print(i.get_as_days(i.date), 'days')
    print('is valid', Date.is_valid(i.date))
    print()

    i.date = '20 1 2000'
    print(i.date)
    print(i.get_as_days(i.date), 'days')
    print('is valid', Date.is_valid(i.date))
    print()
