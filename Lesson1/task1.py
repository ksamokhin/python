myName = 'Костя'
myAge = 38
name = input('Как Вас зовут? ')
age = int(input('Сколько Вам лет? '))
if (myName == name):
    print('Круто! Меня тоже зовут Костя!')
else:
    if (myAge == age):
        print('Вот это совпадение! Мне тоже 38 лет!')
    else:
        print(f'Привет, {name}! Меня зовут {myName}! ')

print(f'{name} Вам {age} лет! Вся жизнь в переди!')
