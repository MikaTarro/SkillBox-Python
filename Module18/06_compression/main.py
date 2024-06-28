#                   Введите строку: aaAAbbсaaaA
#                   Закодированная строка: a2A2b2с1a3A1


text = 'aaAAbbсaaaA'                     # input('Введите строку: ')
lenght=len(text)
cnt=1
for i in range(lenght):
    if i==(lenght - 1):
        print(text[i] + str(cnt), end='')
    else:
        if text[i]==text[i + 1]:
            cnt=cnt+1
        else:
            print(text[i] + str(cnt), end='')
            cnt=1