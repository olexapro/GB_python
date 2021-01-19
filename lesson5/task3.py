
"""

3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
 Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
 Выполнить подсчет средней величины дохода сотрудников.

"""


with open('task3', encoding='utf-8') as file:
    file = file.read()
    file = [i.split(' ') for i in file.split('\n')]

    list1 = []
    for line in file:
        if int(line[1]) < 20000:
            print(line[0])
        else:
            list1.append(int(line[1]))

    print(sum(list1)/len(list1))
