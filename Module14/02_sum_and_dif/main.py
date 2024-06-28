def summa(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ


def numbers(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count



n = int(input('Введите число N: '))

print(f'Сумма чисел N: {summa(n)}')
print(f'\nКоличество цифр числа N: {numbers(n)}')
print(f'Разность суммы и количества циф: {(summa(n)) - numbers(n)}')
