list = list(input('Введите произвольную строку: '))
i = 1;
while i < len(list):
    list[i - 1], list[i] = list[i], list[i - 1]
    i += 2

print(''.join(list))
