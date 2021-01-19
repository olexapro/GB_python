
"""

2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке.

"""

with open('task2.txt', 'r', encoding='utf-8') as file:
    file_data = file.readlines()
    for x, y in enumerate(file_data):
        print('Строка ', x, ' -  слов ',  len(y.split(' '))-1, sep=' ')
