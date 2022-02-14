# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
firm_list = []
firm_dict = {}
firm_list.append(firm_dict)
average_profit_1 = 0
firm_counter = 0
with open("task_7.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        line = line.strip().split(' ')
        firm_dict[line[0]] = int(line[2]) - int(line[3])
        average_profit_1 += (int(line[2]) - int(line[3]))
        firm_counter += 1
        print(average_profit_1)
        print(firm_counter)
    average_profit_1 = int(average_profit_1 / firm_counter)
    average_profit_dict = dict(average_profit = average_profit_1)
    firm_list.append(average_profit_dict)
    print(firm_list)

try:
    write_f = open("task_7.json", 'w')
    json.dump(firm_list, write_f)
except IOError:
    print('Произошла ошибка ввода-вывода!')
finally:
    write_f.close()
