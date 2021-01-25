"""
    1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
     который должен принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
    Примеры матриц вы найдете в методичке.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__()
    для реализации операции сложения двух объектов класса Matrix (двух матриц).
    Результатом сложения должна быть новая матрица.
    Подсказка: сложение элементов матриц выполнять поэлементно — 
    первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

"""

from random import randint


class Matrix:
    def __init__(self, matrix=None):
        self.matrix = matrix

    def __str__(self):
        list1 = ''
        for z in range(len(self.matrix)):
            for x in self.matrix[z]:
                list1 += str(x) + ' '
            list1 += '\n'

        return list1

    def __add__(self, other):
        if len(self.matrix) <= len(other.matrix):  # print('M1 <= M2')

            # если матрица1 меньше или равна матрице2 по количеству строк
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) > len(other.matrix[i]):  # print('M1[i] > M2[i]')

                    # если длинна матрицы 1 больше матрицы 2 то принимать значение первой как единственные
                    for j in range(len(other.matrix[i])):
                        self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

                    for k in range(len(other.matrix[i]) - len(self.matrix[i]), 0, -1):
                        self.matrix[i][k + len(other.matrix[i])] = self.matrix[i][k]

                else:  # print('M1[i] <= M2[i]')

                    # что бы не писать еще два ветвления я сделал так
                    for j in range(len(self.matrix[i])):
                        self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

                    if len(self.matrix[i]) < len(other.matrix[i]):
                        # если длинна матрицы 2 больше матрицы 1 то принимать значения второй как единственные
                        # print('M1[i] < M2[i]')
                        k = abs(len(self.matrix[i]) - len(other.matrix[i]))
                        self.matrix[i] += other.matrix[i][-k:]

            if len(self.matrix) < len(other.matrix):
                # print('M1 < M2')
                self.matrix += other.matrix[-1:]

        else:  # print('M1 > M2')

            # если матрица1 больше матрицы2 по количеству строк
            for i in range(len(other.matrix)):
                if len(self.matrix[i]) > len(other.matrix[i]):
                    # если длинна матрицы 1 больше матрицы 2 то принимать значение первой как единственные
                    # print('M1[i] > M2[i]')
                    for j in range(len(other.matrix[i])):
                        self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

                    for k in range(len(other.matrix[i]) - len(self.matrix[i]), 0, -1):
                        self.matrix[i][k + len(other.matrix[i])] = self.matrix[i][k]

                else:
                    # что бы не писать еще ветвления я сделал так
                    # print('M1[i] <= M2[i]')
                    for j in range(len(self.matrix[i])):
                        self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

                    if len(self.matrix[i]) < len(other.matrix[i]):
                        # если длинна матрицы 2 больше матрицы 1 то принимать значения второй как единственные
                        # print('M1[i] < M2[i]')
                        k = abs(len(self.matrix[i]) - len(other.matrix[i]))
                        self.matrix[i] += other.matrix[i][-k:]

        return Matrix(self.matrix)

    def generate(self, y, x, nums=9):
        return Matrix([[randint(0, nums) for _ in range(x)] for _ in range(y)])


i = 3
j = 5

print('массивы одинаковые', ' - ' * 5 * 5)
m1 = Matrix().generate(i, j)
m2 = Matrix().generate(i, j)
print(f'M1: \n{m1}\nM2: \n{m2}\nm21: \n{m2 + m1}\n', '- '*10)

print('массив1 < массив2', ' - ' * 5 * 5)
m1 = Matrix().generate(i, j)
m2 = Matrix().generate(i + 3, j + 3)
print(f'M1: \n{m1}\nM2: \n{m2}\nm21: \n{m2 + m1}\n', '- '*10)

print('массив1 > массив2', ' - ' * 5 * 5)
m1 = Matrix().generate(i + 3, j + 3)
m2 = Matrix().generate(i, j)
print(f'M1: \n{m1}\nM2: \n{m2}\nm21: \n{m2 + m1}\n','- '*10)

m21 = m1+m2
print('888'*100,'\n', m21+ m1)
