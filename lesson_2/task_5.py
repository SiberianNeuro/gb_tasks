# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
while input('Добавим число? да/нет: ') == 'да':
    num = int(input('Введите число:  '))
    counter = my_list.count(num)
    for el in my_list:
        if counter > 0:
            index_num = my_list.index(num)
            my_list.insert(index_num + counter, num)
            break
        else:
            if num > el:
                index_num_2 = my_list.index(el)
                my_list.insert(index_num_2, num)
                break
            elif num < my_list[len(my_list) - 1]:
                my_list.append(num)
    print(my_list)