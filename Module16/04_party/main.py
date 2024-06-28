guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

                                           # пришёл \ ушёл \ конец \
while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    askQuestion = input('Гость пришёл или ушёл? ')
    if askQuestion == 'пришёл':
        new_name = input('Введите новое имя: ')
        print(f'Привет! {new_name}\n')
        guests.append(new_name)
        if len(guests) > 6:
            print(f'Прости {new_name}, больше мест нет!\n')
            guests.remove(new_name)

    elif askQuestion == 'ушёл':
        leve_name = input('Введите имя гостя: ')
        print(f'Пока! {leve_name}\n')
        guests.remove(leve_name)

    elif askQuestion == 'конец':
        print('Вечеринка закончилась, все легли спать.')
        break

    else:
        var = askQuestion != 'пришёл' or askQuestion != 'ушёл'
        print(f'Неправильный ввод: {askQuestion}\n')


