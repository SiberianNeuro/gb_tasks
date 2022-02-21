# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

from math import factorial

def fact(n):
    for el in range(1, n):
        yield el

fact_list = []
fact_number = int(input('Введите число: '))
for el in fact(fact_number + 1):
    fact_list.append(factorial(el))

print(f'Факториалы чисел от 1 до {fact_number} - {fact_list}')
