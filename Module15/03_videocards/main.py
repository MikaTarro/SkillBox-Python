cards_count = int(input('Введите количество видеокарт: '))
old_list = []
new_list = []
for i in range(cards_count):
    print(i + 1, "Видеокарта:",  end=' ')
    seria = int(input())
    if seria < 3090:
        new_list.append(seria)
    old_list.append(seria)
print(f'Старый список видеокарт:, {old_list}\nСтарый список видеокарт:", {new_list}')


# Кол-во видюх 5
# 1 Видеокарта: 3070
# 2 Видеокарта: 2060
# 3 Видеокарта: 3090
# 4 Видеокарта: 3070
# 5 Видеокарта: 3090

# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
# Новый список видеокарт: [ 3070 2060 3070 ]