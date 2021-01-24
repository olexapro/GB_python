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
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                list1 += str(j) + ' '
            list1 += '\n'

        return list1

    def __add__(self, other):
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) > len(other.matrix[i]):
                print('M1 > M2')
                # если длинна матрицы 1 больше матрицы 2 то принимать значение первой как единственные
                for j in range(len(other.matrix[i])):
                    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

                for k in range(len(other.matrix[i]) - len(self.matrix[i]), 0, -1):
                    self.matrix[i][k + len(other.matrix[i])] = self.matrix[i][k]

            else:
                print('M1 <= M2')
                # что бы не писать еще два ветвления я сделал так
                for j in range(len(self.matrix[i])):
                    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

                if len(self.matrix[i]) < len(other.matrix[i]):
                    # если длинна матрицы 2 больше матрицы 1 то принимать значения второй как единственные
                    print('M1 < M2')
                    k = abs(len(self.matrix[i]) - len(other.matrix[i]))
                    self.matrix[i] += other.matrix[i][-k:]

        return self.matrix


matrix1 = Matrix([[randint(0, 9) for _ in range(6)] for _ in range(2)])
print(matrix1)

matrix2 = Matrix([[randint(0, 9) for _ in range(5)] for _ in range(2)])
print(matrix2)

m21 = Matrix(matrix1 + matrix2)
print(m21)

# for i in matrix1:
#     print(i)
