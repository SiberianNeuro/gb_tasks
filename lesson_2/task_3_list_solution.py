# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
month_number = int(input('Введите месяц числовом формате: '))
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month_number == 1 or month_number == 2 or month_number == 12:
    print(season_list[0])
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(season_list[1])
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(season_list[2])
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(season_list[3])

# Это решение кажется мне топорным, но более лаконичного способа придумать не смог.