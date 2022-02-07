# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def data_func(firstname, lastname, bdate, city, email, phone):
    print(f'Имя - {firstname}, Фамилия - {lastname}, День рождения - {bdate}, Город проживания - {city}, Email - {email}, Телефон - {phone}')

data_func(firstname='Никита', lastname='Канушин', bdate='22.11.1995', city='Омск', email='email@email.com', phone='Iphone 11')