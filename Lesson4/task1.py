from sys import argv


def wage(product, rate, bonus):
    return product * rate + bonus


try:
    script, product, rate, bonus = argv
    print(f'Сотрудник заработал {wage(int(product), int(rate), int(bonus))} рублей.')
except ValueError:
    print('В параметрах нужно указать через пробел: выработку в часах, ставку за час и премию.')
