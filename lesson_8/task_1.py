# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data():

    day = 0
    month = 0
    year = 0

    def __init__(self, data):
        self.data = str(data)
        print(self.data)

    @classmethod
    def reformer(cls, self):
        cls.data = list(map(int, self.data.split('-')))
        Data.day = cls.data[0]
        Data.month = cls.data[1]
        Data.year = cls.data[2]
        return f'Число: {cls.data[0]}\nМесяц: {cls.data[1]}\nГод: {cls.data[2]}'

    @staticmethod
    def DataTest():
        if 0 < Data.year <= 2022:
            print('Год указан валидно')
        else:
            print('Невалидный год')
        if 1 <= Data.month <= 12:
            print('Месяц указан валидно')
        else:
            print('Невалидный месяц')
        if 1 <= Data.day <= 31:
            print('День указан валидно')
        else:
            print('Невалидный день')





x = Data('1-0-0')
print(Data.reformer(x))
Data.DataTest()

# Неясно, откуда взялось None при проверке кода




