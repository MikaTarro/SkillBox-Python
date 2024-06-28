# Название файла не должно начинаться на один из специальных символов: @№$%^&\*().
# Файл заканчивается расширением .txt или .docx
while True:
    # word = input('Введите название файла: ')
    # if word.startswith(tuple("@№$%^&*()")):
    #     print('Ошибка: в названии файла запрещенный символ!')
    # elif not word.endswith((".txt", ".docx")):
    #     print('Ошибка: формат файла не txt')
    # else:
    #     print('все хорошо!')

        fileName = input('\nВведите название файла: ')
        if fileName.startswith(tuple("@№$%^&*()")):
            print('Ошибка: в названии файла запрещенный символ!')
        elif not fileName.endswith((".txt", ".docx")):
            print('Ошибка: формат файла не txt')
        else:
            print('все хорошо!')