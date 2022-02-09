# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

def sum_func():
    my_list = input('Введите числа через пробел: ').split(' ')
    int_list = []
    for el in my_list:
        int_list.append(int(el))
        int_list_sum = sum(int_list)
    print(f'Получившаяся сумма - {int_list_sum}')
    while input('Ввести еще один набор чисел? да/нет: ') == 'да':
        new_list = input('Введите числа через пробел: ').split(' ')
        for elem in new_list:
            int_list.append(int(elem))
            int_list_sum = sum(int_list)
        print(f'Получившаяся сумма - {int_list_sum}')
    return int_list_sum

print(f'Итоговая сумма чисел - {sum_func()}')