class Car:
    def __init__(self, speed, color, name, is_polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} составляет {self.speed} км в час.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(
                f'Внимание! Городская машина {self.name}  превыcила скорость 60 км в час! Текущая скорость {self.speed}')
        else:
            print(f'Текущая скорость городской машины {self.name} составляет {self.speed} км в час.')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(
                f'Внимание! Рабочая машина {self.name}  превыcила скорость 40 км в час! Текущая скорость {self.speed}')
        else:
            print(f'Текущая скорость рабочей машины {self.name} составляет {self.speed} км в час.')


class SportCar(Car):
    pass


class PoliseCar(Car):
    def __init__(self, speed, color, name, is_polise=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise


tc = TownCar(70, 'Красный', 'Додж')
wc = WorkCar(40, 'Желтый', 'Кран')
sc = SportCar(220, 'Синий', 'Панамера')
pc = PoliseCar(59, 'Черный', 'Веста')

tc.go()
wc.stop()
sc.turn("на лево")
pc.show_speed()
pc.speed = 180
pc.show_speed()
tc.show_speed()
wc.show_speed()
is_polise = tc.is_polise, wc.is_polise, sc.is_polise, pc.is_polise
print(is_polise)
