"""

5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""
from random import randint


with open('task5', mode='w', encoding='utf-8') as file:
    file.write(' '.join([str(randint(0, 100)) for _ in range(randint(10, 20))]))


with open('task5', mode='r', encoding='utf-8') as f:
    print(sum([int(i) for i in f.read().split(' ')]))
