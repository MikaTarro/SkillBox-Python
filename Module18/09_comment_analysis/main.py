def cntText (self):
      upper = sum(map(str.isupper, text))
      lower = sum(map(str.islower, text))
      return print (f'Заглавных букв: {upper} \nСтрочных букв: {lower}')


text = str(input('Введи строку для анализа: '))
print(cntText(text))



# print(f'Заглавных букв: {sum(map(str.isupper, text))} '
#       f'\nСтрочных букв: {sum(map(str.islower, text))}'
#       )




