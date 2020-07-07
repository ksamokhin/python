cost = int(input('Какие издержки у вашей компании? '))
proceeds = int(input('Какая выручка у вашей компании? '))

if proceeds > cost:
    rent = (proceeds - cost) / proceeds * 100
    print('Поздраляем Ваша компания в плюсе. Рентабельность выручки составляет %.2f' % (rent))
    staff = int(input('Сколько сотрудников в вашей компании? '))
    profit = (proceeds - cost) / staff
    print('Доход на одного сотрудника составляет %.2f' % (profit))
else:
    if proceeds == cost:
        print('Ваша компания отработала в ноль!')
    else:
        print('Ваша компания отработала в убыток!')
