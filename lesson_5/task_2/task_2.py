# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

f_obj = open("task_file.txt", 'r')
line_counter = 0
for line in f_obj:
    line_counter += 1
    words_in_line = line.split()
    print(f'Общее количество слов в {line_counter}-й строке - {len(words_in_line)}')
print(f'Общее количество строк - {line_counter}')
f_obj.close()