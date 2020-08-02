from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return self.calc + other.calc


class Coat(Clothing):
    @property
    def calc(self):
        return float(self.size / 6.5 + 0.5)


class Costume(Clothing):
    @property
    def calc(self):
        return float((self.size * 2) / 100 + 0.3)


try:
    ks, ps = map(float, input('Введите рост костюма и размер пальто (два числа через пробел)? ').split())
    k = Costume(ks)
    p = Coat(ps)
    print(
        f'Для костюма потребуется {k.calc:.2f} ткани. \nДля пальто потребуется {p.calc:.2f} ткани.\nВсего будет израсходовано {k + p:.2f} ткани')
except ValueError:
    print("Не верный ввод даных!")
