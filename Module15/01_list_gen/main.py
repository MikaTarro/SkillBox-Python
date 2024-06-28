# TODO здесь писать код
odd_pool = []
number = int(input('Введите число: '))
for i in range(number + 1):
    if i % 2!= 0:
        odd_pool.append(i)
print('Список из нечётных чисел от одного до N:',odd_pool)