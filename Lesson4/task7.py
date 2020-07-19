def fact(n):
    f = 1
    for el in range(1, n + 1):
        f *= el
        yield f


try:
    n = int(input('Введите число:'))
    for el in fact(n):
        print(el)
except ValueError:
    print('Нужно было ввести число!')
