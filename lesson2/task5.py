# encoding: utf-8
"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

import random

rangs = sorted([random.randint(0, 10) for i in range(5)], reverse=True)

print(rangs)
         
while True:
    input_rang = int(input())
    if input_rang in rangs:
        rangs.insert(rangs.index(input_rang)+1, input_rang)
    elif input_rang > max(rangs):
        rangs.insert(0, input_rang)
    elif input_rang < min(rangs):
        rangs.append(input_rang)
    else:
        for i in range(len(rangs)):
            if rangs[i] > input_rang and input_rang > rangs[i+1] :
                rangs.insert(i+1, input_rang)
                break
    print(rangs)