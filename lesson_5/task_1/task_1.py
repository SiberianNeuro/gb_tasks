# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

f_obj = open("task_file.txt", 'w')

strings = []
while True:
    string = input('Введите данные:')
    if string == '':
        break
    else:
        string_1 = string + '\n'
        strings.append(string_1)
f_obj.writelines(strings)
print(strings)
f_obj.close()
