#               Пример 1:

# Введите строку: я есть строка
# Самое длинное слово: строка
# Длина этого слова: 6

#               Пример 2:

# Введите строку: а б
# Самое длинное слово: а
# Длина этого слова: 1

#               Пример 3:

# Введите строку:    б
# Самое длинное слово: б
# Длина этого слова: 1

def largest_word(sentence):
    split_sentence = sentence.split(' ')
    largest_word = ''
    for i in range(len(split_sentence)):
        if len(split_sentence[i]) > len(largest_word):
           largest_word = split_sentence[i]
    print('Самое длинное слово:',largest_word)
    print('Длина этого слова: ',len(largest_word))


sentence = input('Введите строку: ')

largest_word(sentence)
