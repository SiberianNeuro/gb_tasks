# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        if direction == 'right':
            print(f'{self.name} повернула направо.')
        elif direction == 'left':
            print(f'{self.name} повернула налево.')
        elif direction == 'around':
            print(f'{self.name} развернулась.')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed} км/ч.')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч. Зарегистрировано превышение скорости!')
        else:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч.')

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч. Зарегистрировано превышение скорости!')
        else:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч.')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


solaris = TownCar(65, 'white', 'Hyondai Solaris', False)
print(solaris.name, end=' ')
print(solaris.color, end=' ')
print(solaris.speed, end=' ')
print(solaris.is_police)
solaris.go()
solaris.stop()
solaris.turn('right')
solaris.turn('left')
solaris.turn('around')
solaris.show_speed()
solaris.speed = 60
solaris.show_speed()

granta = WorkCar(40, 'gray', 'Lada Granta', False)
print(granta.name, end=' ')
print(granta.color, end=' ')
print(granta.speed, end=' ')
print(granta.is_police)
granta.go()
granta.stop()
granta.turn('right')
granta.turn('left')
granta.turn('around')
granta.show_speed()
granta.speed = 45
granta.show_speed()

audi = SportCar(180, 'red', 'Audi TT', False)
print(audi.name, end=' ')
print(audi.color, end=' ')
print(audi.speed, end=' ')
print(audi.is_police)
audi.go()
audi.stop()
audi.turn('right')
audi.turn('left')
audi.turn('around')
audi.show_speed()

octavia = PoliceCar(60, 'blue-white', 'Skoda Octavia ', True)
print(octavia.name, end=' ')
print(octavia.color, end=' ')
print(octavia.speed, end=' ')
print(octavia.is_police)
octavia.go()
octavia.stop()
octavia.turn('right')
octavia.turn('left')
octavia.turn('around')
octavia.show_speed()

