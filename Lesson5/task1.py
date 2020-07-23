file = open('out_task1.txt', 'w')
str_list = []
in_str = input("Введите данные для записи в файл (для завершения ввода введите пустую строку):")
str_list.append(in_str+'\n')
while in_str != '':
    in_str = input()
    str_list.append(in_str + '\n')
file.writelines(str_list)
file.close()