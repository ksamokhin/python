class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


try:
    name, surname, wage, bonus = input(f'Введите через пробел имя, фамилию, оклад и премию сотрудника:').split()
    pos1 = Position(name, surname, float(wage), float(bonus))
    print(pos1.get_full_name())
    print(pos1.get_total_income())
except ValueError:
    print('Ошибка ввода даных')
