a = int(input('Сколько км пробежит спортсмен в первый день? '))
b = int(input('Сколько км должен пробегать спортсмен в день? '))
day = 1
while b > a:
    a = a * 1.1
    day += 1

print('На %d-й день спортсмен прбежит не менее %d км.' % (day,b))
