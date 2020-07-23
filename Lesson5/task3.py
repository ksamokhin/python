sum = 0
num = 0
try:
    with open('task3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.split()
                if int(data[1]) < 20000:
                    print(data[0])
                sum += int(data[1])
                num += 1

    print(f'Средняя зарплата равна: {int(sum/num)}')
except ValueError:
    print('Не верный формат файла!')