from random import randint
str = ''
try:
    num = int(input('Сколько чисел использовать? '))
    for el in range(num):
        str += (f'{randint(0,100)} ')
    str += '\n'
    with open('task5.txt', 'w', encoding='utf-8') as file:
        file.writelines(str)
    with open('task5.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(f'Сумма всех чисел в файле {file.name} равна: {sum([int(el) for el in line.split()])}')

except IOError:
    print("Ошибка ввода данных.")