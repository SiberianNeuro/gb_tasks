# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = int(input('Введите расстояние пробежки в первый день (км): '))
b = int(input('Введите желаемое расстояние: '))
d = 0
while a > 0 and d >= 0:
    print('{}-й день: '.format(d + 1), '{:.2f}'.format(a), 'км')
    d = d + 1
    a = a * 1.1
    if a > b:
        break
print('{}-й день: '.format(d + 1), '{:.2f}'.format(a), 'км')
print('на', '{}-й день'.format(d + 1), 'спортсмен достиг результата - не менее', b, 'км')
