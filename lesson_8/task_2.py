# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt

try:
    dividend = int(input('Введите делимое: '))
    divider = int(input('Введите делитель: '))
    if divider == 0:
        raise OwnError('Вы ввели 0. На ноль делить нельзя!')
except ValueError:
    print('Вы ввели не число')
except OwnError as err:
    print(err)
else:
    res = dividend / divider
    print(f'Все хорошо. Результат деления - {int(res)}.')
finally:
    print('Программа завершена.')