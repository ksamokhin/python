import json
list = []
dict = {}
aver = {'average_profit': 0}
num = 0
with open('task7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        list = line.split()
        dict[list[0]] = int(list[2]) - int(list[3])
        if dict[list[0]] >= 0:
            aver['average_profit'] += dict[list[0]]
            num += 1
aver['average_profit'] = aver['average_profit'] / num
list = []
list.append(dict)
list.append(aver)
with open('task7.json', 'w', encoding='utf-8') as file:
    json.dump(list, file, ensure_ascii=False)
