# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
string = input('Введите набор слов: ')
string = string.split(' ')
for ind, el in enumerate(string, 1):
    if len(el) >= 10:
        print(ind, el[:10])
    else:
        print(ind, el)