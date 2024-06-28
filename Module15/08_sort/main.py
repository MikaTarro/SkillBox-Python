rand_pool = []
correct_pool = []

h_many = int(input('Введите количество чисел в строке: '))

for pool in range(h_many):
    n = int(input('Введите число: '))
    rand_pool.append(n)

print(rand_pool)

print("Original List:", rand_pool)

# sorting list using nested loops
for i in range(0, len(rand_pool)):
    for j in range(i + 1, len(rand_pool)):
        if rand_pool[i] >= rand_pool[j]:
            rand_pool[i], rand_pool[j] = rand_pool[j], rand_pool[i]

# sorted list
print("Sorted List", rand_pool)



# значальный список: [1, 4, -3, 0, 10]
# Отсортированный список: [-3, 0, 1, 4, 10]
#                                                    Не понимаю, смотрю форумы. все используют sorted()


