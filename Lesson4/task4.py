from random import randint

list = [randint(0, 20) for el in range(20)]
newList = [list[el] for el in range(len(list)) if (list.count(list[el]) == 1)]
print(list)
print(newList)
