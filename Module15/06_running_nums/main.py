

n = [1, 2, 3, 4, 5]
print(*n)
while True:
    steps = int(input('Насколько сдвинуть: '))
    n = n[-steps:] + n[:-steps]
# for i in range(steps):
#     n.insert(0, n.pop())
    print(*n)


# Сдвиг: 1
# Изначальный список: [1, 2, 3, 4, 5]
# Сдвинутый список: [5, 1, 2, 3, 4]
