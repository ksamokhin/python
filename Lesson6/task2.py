class Road:
    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht

    def calc(self, depth):
        return self._lenght * self._widht * 25 * depth


try:
    len, wid = map(int, input(f'Введите длину и ширну дороги через пробел: ').split())
    avenu = Road(len, wid)
    depth = int(input('Какой толщины в см делать дорогу? '))
    print(f'Потребуется {avenu.calc(depth)} тонн асфальта.')
except ValueError:
    print('Ошибка ввода даных.')
