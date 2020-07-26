data = {}
str = []
with open('task6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        str = line.replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('—',
                                                                                                        '0').split()
        data[str[0]] = int(str[1]) + int(str[2]) + int(str[3])
print(data)
