from typing import Any

u_num = int(input('Введите число: '))


def divider_n(a):
    divider = 1
    while divider <= a:
        divider: int | Any = divider + 1
        if a % divider == 0:
            return divider


print(f'Наименьший делитель, отличный от единицы: {divider_n(u_num)}')
#