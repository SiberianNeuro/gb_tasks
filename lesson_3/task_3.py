def my_func():
    try:
        var_1 = int(input('Введите первое число: '))
        var_2 = int(input('Введите второе число: '))
        var_3 = int(input('Введите третье число: '))
    except ValueError:
        return 'Можно вводить только числа!'
    if var_1 < var_2 and var_1 < var_3:
        var_sum = var_2 + var_3
    elif var_2 < var_1 and var_2 < var_3:
        var_sum = var_1 + var_3
    elif var_3 < var_1 and var_3 < var_2:
        var_sum = var_1 + var_2
    return var_sum

print(my_func())