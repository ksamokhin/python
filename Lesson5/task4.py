dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
str_list = []
with open('task4.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split()
        str_list.append(dict[data[0]] + ' - ' + data[2] + '\n')
with open('out_task4.txt', 'w', encoding='utf-8') as out_file:
    out_file.writelines(str_list)
