time = int(input('Введите время в секундах (не более 86400): '))
if time <= 86400:
    sec = time % 60
    time = int(time / 60)
    min = time % 60
    time = int(time / 60)
    print ('Получилось %.2d:%.2d:%.2d' % (time, min, sec))
else:
    print('Вы ввели слишком большое число')