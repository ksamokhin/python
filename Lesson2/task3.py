i = 1
while i:
    mon = input('Введите месяц в виде целого числа от 1 до 12: ')
    if (mon.isdigit()):
        mon = int(mon)
        if (mon > 0 and mon < 13):
            i = 0

mon_list = [('январь', 'зима'), ('февраль', 'зима'), ('март', 'весна'), ('апрель', 'весна'), ('май', 'весна'),
            ('июнь', 'лето'), ('июль', 'лето'), ('август', 'лето'), ('сентябрь', 'осень'), ('октябрь', 'осень'),
            ('ноябрь', 'осень'), ('декабрь', 'зима')]
print(f'{mon_list[mon - 1][0].capitalize()} это {mon_list[mon - 1][1]}.')
