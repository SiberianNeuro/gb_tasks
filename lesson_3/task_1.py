def div_func():
    try:
        var_1 = int(input('Введите делимое: '))
        var_2 = int(input('Введите делитель: '))
        var_3 = var_1 / var_2
    except ValueError:
        return 'Можно вводить только числа!'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return var_3
print(div_func())
