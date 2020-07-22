from functools import reduce

calc = lambda x, y: int(x) * int(y)
list = [el for el in range(100, 1001) if el % 2 == 0]
print(list)
print(reduce(calc, list))
