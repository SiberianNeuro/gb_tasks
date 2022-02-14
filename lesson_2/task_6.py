# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
# — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество,
# единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:

# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:

# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

merch_list = []
num = 1
while input('Добавить товар? да/нет: ') == 'да':
    merch = {}
    merch['название'] = input('Введите название товара: ')
    merch['цена'] = int(input('Введите цену товара: '))
    merch['количество'] = int(input('Введите количество товара: '))
    merch['ед.'] = input('Введите единицу измерения: ')
    merch_list.append(tuple([num, merch]))
    num += 1
list_element = 0
# Окончание с разбитием кортежей на строки, но без списка:
while list_element < len(merch_list):
    print(merch_list[list_element])
    list_element += 1
# Окончание с кортежами в списке, но без разбития на строки:
# print(merch_list)

analytics = {}
if input('Провести аналитику товаров? да/нет: ') == 'да':
    for merch_pos in merch_list:
        for merch_key, merch_value in merch_pos[1].items():
            if merch_key in analytics:
                analytics[merch_key].append(merch_value)
            else:
                analytics[merch_key] = [merch_value]
    for i, j in analytics.items():
        analytics[i] = list(set(j))

    print(analytics)
else:
    print('Программа завершена')

# Не смог понять, как убрать повторяющиеся значения из словаря, поэтому при проведении аналитики товара повторяются
# значения единиц измерения.
