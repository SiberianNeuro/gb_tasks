# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

try:
    f_obj = open("task_5.txt", 'w')
    while input('Желаете ввести числа? да/нет: ').lower() == 'да':
        f_obj.write(input('Введите числа через пробел: ') + '\n')
except IOError:
    print('Произошла ошибка ввода-вывода!')
finally:
    f_obj.close()

summ = 0
with open("task_5.txt", 'r') as count_obj:
    for line in count_obj:
        content = line.rstrip().split(' ')
        content = list(map(int, content))
        summ += sum(content)
        print(content)
    print(f'Сумма всех чисел в файле - {summ}')