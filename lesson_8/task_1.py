# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data():
    global day, month, year
    day = 0
    month = 0
    year = 0

    def __init__(self, data):
        self.data = str(data)
        print(self.data)

    @classmethod
    def reformer(cls, self):
        cls.data = list(map(int, self.data.split('-')))
        day = cls.data[0]
        month = cls.data[1]
        year = cls.data[2]
        return f'Число: {cls.data[0]}\nМесяц: {cls.data[1]}\nГод: {cls.data[2]}'

    @staticmethod
    def DataTest():
        if year > 2022:
            print('Неверно указан год')
        elif month < 1 and month > 12:
            print('Неверно указан месяц')
        elif day < 1 and day > 31:
            print('Неверно указан день')
        else:
            print('Дата валидна')



x = Data('22-11-1995')
print(Data.reformer(x))
print(Data.DataTest())

# Неясно, откуда взялось None при проверке кода




