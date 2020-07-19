from itertools import count
from itertools import cycle


def iterator1(start):
    stop = 0
    list = []
    for el in count(start):
        list.append(el)
        stop += 1
        if stop > 10:
            break
    return list


def iterator2(str):
    stop = 0
    list = []
    for el in cycle(str):
        list.append(el)
        stop += 1
        if stop > 10:
            break
    return list


str = "ABCDE"
try:
    start = int(input('Введите стартовоечисло: '))
    print(iterator1(start))
    print(iterator2(str))
except ValueError:
    print('Нужно ввести число!')
