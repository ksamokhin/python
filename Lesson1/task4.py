number = int(input('Введите целое положительное число: '))
count = 0
digit = number % 10
while number > 9:
    count += 1
    if digit == 9:
        break
    else:
        number = int(number / 10)
        newDigit = number % 10
        if digit < newDigit:
            digit = newDigit

if count == 0:
    print('Нужно было ввести положительное число')
else:
    print(f'Максимально число {digit}')

