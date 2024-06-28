import random

errors = [
    'Не повезло',
    'Повезло но не сильно',
    'Красавчик, продолжай дальше'
]

rnd = 0
fl = 0
with open('out_file.txt', 'w') as file:
    while rnd <= 777:
        nums = int(input('Введите число: '))
        rnd += nums
        if 13 == random.randint(1, 13):
            raise Exception(random.choice(errors))
        print(nums, file=file)
    print('Вы успешно выполнили условие для выхода из порочного цикла!')