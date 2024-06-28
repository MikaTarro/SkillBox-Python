# Введите количество заказов: 6
# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5
#
# Иванов:
# 	Мексиканская: 2
# 	Мясная: 3
# 	Пепперони: 3
# Петров:
# 	Де-Люкс: 2
# 	Интересная: 5
# dict = {}
# for _ in range(int(input('Введите кол-во заказов: '))):
#     a, b, c = input('Имя заказчика, название пицы, кол-во: ').split()
#     dict['name'], dict['product'], dict['amount'] = a, b, c
#     print(dict)
# print(dict)


dict = dict()

for _ in range(int(input('введите количество заказов: '))):
    name, product, amount = input(f'\n{_ + 1}-й заказ: ').split()

    dict[name][product] = dict.setdefault(name, {}).setdefault(product, 0) + int(amount)
print(dict)
for key in sorted(dict):
    print(f'{key}:')
    for i in sorted(dict[key].items()):
        print('--', *i)
