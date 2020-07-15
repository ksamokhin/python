string = input('Введите несколько слов через пробел: ')
list = string.split()
i = 1
for el in list:
    print(f'{i}. {el[0:10]}')
    i += 1
