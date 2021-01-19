"""
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""


with open('task4', mode='r+', encoding='utf-8') as file:
    list1 = []
    var1 = {'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'}

    for i in file.readlines():
        list1.append(i.replace('\n', '').split(' - '))

    filename = 'task4_a.txt'
    with open(filename, mode='w', encoding='utf-8') as f:
        for j in list1:
            f.write(var1[j[0]] + ' - ' + j[1] + '\n')
