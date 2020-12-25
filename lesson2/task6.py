# encoding: utf-8
"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

info = """добавить - добавление товара\n\
товары - просмотр товаров\n\n
"""
form = 'формат ввода: ключевое слово\n'

base = list()
print(len(base))

while True:
    user_input = input(form+info).lower()
    if user_input == 'добавить':
        base_input = input(form + 'название товара_цена_количество_еденица измерения\n').split('_')
        base.append((len(base), {'название':            base_input[0],
                                 'цена товара':         base_input[1],
                                 'количество':          base_input[2], 
                                 'еденица измерения':   base_input[3]
                                 }))

    elif user_input == 'товары':
        for i in base:
            for j in i[1]:
                print(j, end=' / ')
            print('\n')
            for j in i[1]:
                print(i[1][j], end=' ')
            
            print('\n')

    elif user_input == 'выход':
        break
    
print(base)
(0, {'название': {'компьютер'}, 'цена товара': {'20000'}, 'количество': {'10'}, 'еденица измерения': {'шт.'}}) 
(1, {'название': {'компьютер'}, 'цена товара': {'20000'}, 'количество': {'10'}, 'еденица измерения': {'шт.'}})
