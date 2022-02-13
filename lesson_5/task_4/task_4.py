# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from translate import Translator

translator = Translator(to_lang="Russian")
line_list = []
with open("task_4.txt", 'r') as f_obj:
    for line in f_obj:
        another_line = line.split(' - ')
        another_line[0] = translator.translate(another_line[0])
        another_line = ' - '.join(another_line)
        line_list.append(another_line)
print(line_list)

try:
    file_obj = open("task_4_new.txt", 'w')
    file_obj.writelines(line_list)
except IOError:
    print('Произошла ошибка ввода-вывода!')
finally:
    file_obj.close()

