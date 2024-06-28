list_of_names = ['Василий', 'Николай', 'Надежда', 'Никита',  # пул имён
                 'Ян', 'Ольга', 'Евгения', 'Кристина']
file_name = 'people.txt'
def fun_err_and_char_count(list_of_names, file_name):  # передаем имена и фаил
    total_symbols = 0
    line_count = 0
    try:
        with open(file_name, 'w+', encoding='utf-8') as file:  # пишем пул имён в тхт
            file.write('\n'.join(list_of_names))
            file.seek(0)
            print(f'Содержимое файла people.txt: \n{file.read()}')
            file.seek(0)
            print('\nОтвет в консоли:')
            for line in file:
                try:
                    line_count += 1
                    total_symbols += len(line.strip())  # чистим строки
                    if len(line.strip()) < 3:  # проверка
                        raise ValueError
                except ValueError:
                    print(f'Ошибка: менее трёх символов в строке {line_count}.')
    finally:
        return total_symbols


total_number_of_characters = fun_err_and_char_count(list_of_names, file_name)
print(f'Общее количество символов: {total_number_of_characters}.')
