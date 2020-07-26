class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pan(Stationery):
    def __init__(self, title='Ручка'):
        self.title = title

    def draw(self):
        print(f'Запуск синей отрисовки {self.title}')


class Pencil(Stationery):
    def __init__(self, title='Карандаш'):
        self.title = title

    def draw(self):
        print(f'Запуск серой отрисовки {self.title}')


class Handle(Stationery):
    def __init__(self, title='Маркер'):
        self.title = title

    def draw(self):
        print(f'Запуск красной отрисовки {self.title}')


me = Stationery('Мел')
pa = Pan()
pe = Pencil()
ha = Handle()

me.draw()
pa.draw()
pe.draw()
ha.draw()
