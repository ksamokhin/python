def delim(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'


try:
    a, b = input('Введите делимое и делитель через пробел: ').split()
    print(delim(float(a), float(b)))
except ValueError:
    print('Некорректный ввод данных!')
