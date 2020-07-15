def my_func(a, b, c):
    return a + b + c - min(a, b, c)


try:
    a, b, c = input('Введите три числа через пробел: ').split()
    print(my_func(float(a), float(b), float(c)))
except ValueError:
    print('Некорректный ввод данных!')
