
# 4 задание
# тут если честно я не понимаю, как можно добавить арифметику
number = input('введите целое число ')
biggest = int(number[0])  # принимаем 0 элемент за наибольшее число
i = 0  # счетчик

while i < len(number):  #
    i += 1
    if int(number[i-1]) > biggest:
        biggest = int(number[i-1])

print('ваш ввод: {}\наибольшая цифра числа: {}'.format(number, biggest))
