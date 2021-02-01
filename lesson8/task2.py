
"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
- При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivision(Exception):
    """
        input type:string day month year
        example: '01 12 2021'
    """
    def __init__(self):
        self.text = 'ZeroDivisionError'


try:
    while True:
        i = int(input())
        if i <= 0:
            raise ZeroDivision
        else:
            print(i)

except (Exception, ZeroDivision) as exp:
    print(exp.text)

finally:
    print('script finished')
