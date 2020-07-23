str_num = 1
with open('out_task1.txt', 'r') as file:
    for line in file:
        print(f'В строке №{str_num} {len(line.split())} слов.')
        str_num += 1

print(f'Количество строк в фале {file.name} равно {str_num - 1}.')
