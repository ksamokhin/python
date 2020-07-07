number = int(input('Ввеждите число: '))
sum = number
strNumber = str(number)+str(number)
sum += int(strNumber)
strNumber += str(number)
sum += int(strNumber)
print(f'Сумма {number} + {str(number)+str(number)} + {strNumber} равна: {sum}')