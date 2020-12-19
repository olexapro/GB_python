
# # 1 задание
# var_int = int(input('введите целое число '+"пример - 10 "))
# print(type(var_int), var_int)
#
# var_flt = float(input('введите число с плавающей точкой '+"пример - 10.0 "))
# print(type(var_flt), var_flt)
#
# var_str = input('введите строку '+'пример - слово "пример:)" ')
# print(type(var_str), var_str)


# # 2 задание
# time = int(input('введите время в секундах '))
# f=time
# period = 60
# hour = time//(period*period)  # вычисление часов
# time -= hour*(period*period)  # отнимаем целые часы от общего времени
# minute = time//period  # вычисление минут
# sec = time - minute*period # вычисление секунд
#
# print(f'{f} секунд это: \n{hour} час(а/ов),\n{minute} минут(ы/а), \n{sec} секунд(ы/а)')


# # 3 задание
# n = input('введите целое число ')
# print(int(n) + int(f'{n}{n}') + int(f'{n}{n}{n}'))


# # 4 задание
# # тут если честно я не понимаю, как можно добавить арифметику
# number = input('введите целое число ')
# biggest = int(number[0])  # принимаем 0 элемент за наибольшее число
# i = 0  # счетчик
#
# while i < len(number):  #
#     i += 1
#     if int(number[i-1]) > biggest:
#         biggest = int(number[i-1])
#
# print('ваш ввод: {}\наибольшая цифра числа: {}'.format(number, biggest))


# # 5 задание
# currency = input('Введите валюту: ')
# proceeds = int(input('Введите выручку: '))
# costs = int(input('Введите издержеки: '))
# profit = proceeds-costs
# if proceeds > costs:
#     print('прибыль {} {}'.format(str(profit), currency))
#     # profitability = proceeds/costs*100
#     print('Рентабельность :', profit/costs*100, '%')
#     print(f"Выручка на одного сотрудника {profit/int(input('Введите количество сотрудников: '))} {currency}")
# else:
#     print('убыток ', profit, currency)


# # 6 задание
# a, b = int(input('Введите первый день')), int(input('Введите ожидаемый результат'))
# i = 1
# while (a//b) < 1:
#     a += 0.1*a
#     i += 1
#
# print(i, a)
