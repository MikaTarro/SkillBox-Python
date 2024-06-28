N = int(input('Введите длину списка: '))

result = [(1 if x % 2 == 0 else x % 5)for x in range(N)]
print(result)

# Введите длину списка: 10
# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]