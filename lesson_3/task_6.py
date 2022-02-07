# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

"""Часть 1:
# def int_func():
    # word = input('Введите слова на латинице и без заглавной буквы: ')
    # word = word.title()
    # return word
# print(int_func())"""

"""Часть 2:"""
def int_func():
    words = input('Введите слова на латинице нижним регистром через пробел: ').split(' ')
    words = ' '.join(words)
    words.title()
    return words.title()

print(int_func())