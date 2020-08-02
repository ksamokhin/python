class Cage():
    def __init__(self, num):
        self.num = num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if (num < 0):
            print('Операция запрещена!')
        else:
            self.__num = num

    def __str__(self):
        return f'{self.num}'

    def __mul__(self, other):
        return Cage(self.num * other.num)

    def __truediv__(self, other):
        return Cage(int(self.num / other.num))

    def __add__(self, other):
        return Cage(self.num + other.num)

    def __sub__(self, other):
        return Cage(self.num - other.num)

    def make_order(self, order):
        return '\n'.join(['*' * order for el in range(self.num // order)]) + '\n' + '*' * (self.num % order)


cel1 = Cage(5)
cel2 = Cage(10)
cel3 = cel1 + cel2
cel4 = cel2 - cel1
cel5 = cel3 / cel2
cel6 = cel1 * cel2
cel7 = cel1 - cel2

print(cel1, cel2, cel3, cel4, cel5, cel6)
print(cel3.make_order(7))
