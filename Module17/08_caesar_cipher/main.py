# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.

alfaVit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' # алфавит
text = input("Сообщение для шифровки >> ").upper() # ввод сообщения
shifr = '' # наш шифр
for i in text: # занимаемся преобразованием введенного нами сообщения
    mesto = alfaVit.find(i)
    new_mesto = mesto + 3
    if i in alfaVit:
        shifr = shifr + alfaVit[new_mesto]
    else:
        shifr = shifr + i
print(shifr) # выводим полученный шифр