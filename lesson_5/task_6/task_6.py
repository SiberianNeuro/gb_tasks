# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import string
school_dict = {}

with open("task_6.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        hours = 0
        line = line.rstrip().split(': ')
        line[1] = line[1].translate(str.maketrans('','', string.punctuation)).translate(str.maketrans('','', 'л')).\
            translate(str.maketrans('','', 'лаб')).translate(str.maketrans('', '', 'пр')).split(' ')
        line[1] = [i for i in line[1] if i != '']
        line[1] = sum(list(map(int, line[1])))
        school_dict[line[0]] = line[1]

    print(school_dict)
