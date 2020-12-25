
# 5 задание
currency = input('Введите валюту: ')
proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержеки: '))
profit = proceeds-costs
if proceeds > costs:
    print('прибыль {} {}'.format(str(profit), currency))
    # profitability = proceeds/costs*100
    print('Рентабельность :', profit/costs*100, '%')
    print(f"Выручка на одного сотрудника {profit/int(input('Введите количество сотрудников: '))} {currency}")
else:
    print('убыток ', profit, currency)
