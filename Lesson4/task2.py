from random import randint

list = [randint(0, 1000) for el in range(10)]
newList = [list[el + 1] for el in range(len(list) - 1) if list[el + 1] > list[el]]
print(list)
print(newList)
