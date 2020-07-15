index = 1
catalog = []
while True:
    value = input(f'Введите название для товара №{index} (для звершения ввода нажмите ноль и Enter):')
    if value.isdigit() and int(value) == 0:
        break
    else:
        products = {'название': value}
        while True:
            value = input(f'Введите цену для товара №{index}:')
            if value.isdigit() and int(value) > 0:
                products.update({'цена': int(value)})
                break
        while True:
            value = input(f'Введите количество товара №{index}:')
            if value.isdigit() and int(value) > 0:
                products.update({'количество': int(value)})
                break
        value = input(f'Введите единицу измерения товара №{index}:')
        products.update({'ед': value})
        catalog.insert((index - 1), tuple([index, products]))
        index += 1
name = {'название': [], 'цена': [], 'количество': [], 'ед': []}

for el in catalog:
    if not (el[1]['название'] in name['название']):
        name['название'].append(el[1]['название'])
    if not (el[1]['цена'] in name['цена']):
        name['цена'].append(el[1]['цена'])
    if not (el[1]['количество'] in name['количество']):
        name['количество'].append(el[1]['количество'])
    if not (el[1]['ед'] in name['ед']):
        name['ед'].append(el[1]['ед'])

print(name)
