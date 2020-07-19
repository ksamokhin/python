summ = 0
end = 1
while end:
    data = input('Введите несколько числ через пробел (для завершения введите любую букву): ').split()
    for el in data:
        try:
            summ += float(el)
        except ValueError:
            print(f'Ввод данных завершен.')
            end = 0
            break
    print(f'Текущая сумма: {summ}')
