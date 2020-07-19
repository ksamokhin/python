int_func = lambda word: word.capitalize()
newText = ''
text = input('Введите несколько слов через пробел:').split()
for el in text:
    newText += int_func(el.lower()) + ' '

print(newText)
