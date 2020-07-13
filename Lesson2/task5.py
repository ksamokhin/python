rating = [7, 5, 4, 4, 2]
i = 1
while i:
    num = input('Введите натуральное число: ')
    if (num.isdigit()):
        num = int(num)
        if (num > 0):
            i = 0
pos = 0
for el in rating:
    if num > el:
        rating.insert(pos, num)
        break
    else:
        pos += 1

print(rating)
