
# 2 задание
time = int(input('введите время в секундах '))
f=time
period = 60
hour = time//(period*period)  # вычисление часов
time -= hour*(period*period)  # отнимаем целые часы от общего времени
minute = time//period  # вычисление минут
sec = time - minute*period # вычисление секунд

print(f'{f} секунд это: \n{hour} час(а/ов),\n{minute} минут(ы/а), \n{sec} секунд(ы/а)')
