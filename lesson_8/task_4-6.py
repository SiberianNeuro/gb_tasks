# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class WareHouse:

    def __init__(self):
        self.warehouse = {}

    def add_to_warehouse(self, unit):
        if unit.article in self.warehouse:
            self.warehouse[unit.article] += 1
        else:
            self.warehouse[unit.article] = 1

    def take_from_warehouse(self, unit):
        if unit.article in self.warehouse:
            self.warehouse[unit.article] -= 1
        else:
            return f'Такого оборудования на данный момент нет.'

    def warehouse_show(self):
        return f'Список техники на складе - {self.warehouse}'

class Equipment:
    def __init__(self, article, price):
        self.article = article
        if price == None:
            raise ValueError('Цена обязательна')
        else:
            self.price = price

class Printer(Equipment):
    def __init__(self, article, price, mode):
        super().__init__(article, price)
        if mode not in ['Ч/Б', 'ЦВ']:
            raise ValueError('Неверный параметр')
        else:
            self.mode = mode

class Scanner(Equipment):
    def __init__(self, article, price):
        super().__init__(article, price)


class Copier(Equipment):
    def __init__(self, article, price, type):
        super().__init__(article, price)
        if type not in ['Ч/Б', 'ЦВ']:
            raise ValueError('Неверный параметр')
        else:
            self.type = type

wh = WareHouse()
printer = Printer('HP', '5000', 'Ч/Б')
scanner = Scanner('Canon', '3000')
copier = Copier('Xerox', '1000', 'ЦВ')

wh.add_to_warehouse(printer)
wh.add_to_warehouse(scanner)
wh.add_to_warehouse(copier)
wh.warehouse_show()
print(wh.warehouse)