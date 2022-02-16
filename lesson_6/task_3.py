# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        print('Данные о сотруднике сохранены.')


class Position(Worker):

    def get_full_name(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')

    def get_total_income(self):
        print(f'{self.surname} {self.name}:')
        print(f"Полный доход сотрудника составляет {self._income.get('wage') + self._income.get('bonus')} р.")
        print('из которых:')
        print(f"Оклад: {self._income.get('wage')} р.")
        print(f"Премия: {self._income.get('bonus')} р.")


worker_1 = Position('Denis', 'Ivanov', 'tester', 30000, 20000)
print(worker_1.name)
print(worker_1.surname)
print(worker_1._income)
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position('Elena', 'Ivanova', 'manager', 20000, 10000)
print(worker_2.name)
print(worker_2.surname)
print(worker_2._income)
worker_2.get_full_name()
worker_2.get_total_income()
