def my_func(x, y):
    return 1 / (x ** abs(y))


def my_func1(x, y):
    z = x
    for i in range(abs(y+1)):
        z *= x
    return 1 / z


while True:
    try:
        x = float(input('Введите действительное положительное число: '))
        if x > 0:
            break
        else:
            print('Число должно быть положительным!')
    except ValueError:
        print('Некорректный ввод действительного числа!')

while True:
    try:
        y = int(input('Введите целое отрицательное число: '))
        if y < 0:
            break
        else:
            print('Число должно быть отрицательным!')
    except ValueError:
        print('Некорректный ввод целого отрицательного числа!')

print(my_func(x, y))
print(pow(x, y))
print(my_func1(x, y))
