"""

7. Создать (не программно) текстовый файл,
 в котором каждая строка должна содержать данные о фирме:
  название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
 а также среднюю прибыль. Если фирма получила убытки,
 в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
 а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.

"""

import json

with open('task7.json', mode='w', encoding='utf-8') as w_file:
    with open('task7.txt', mode='r', encoding='utf-8') as r_file:
        firm_dict = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in r_file}
        average_profit_lst = [firm_profit for firm_profit in firm_dict.values() if firm_profit > 0]
        json.dump([firm_dict,
                   {'average_profit': sum(average_profit_lst) / len(average_profit_lst)}],
                  w_file,
                  ensure_ascii=False,
                  indent=4)
