shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]


# Название детали: седло
# Кол-во деталей — 3
# Общая стоимость — 4500

name = input('Название детали: ')
details_count: int = 0
price_sum: int = 0
for product in shop:
    if product[0] == name:
        details_count += product.count(name)
        price_sum += product[1]
print(f'\nКол-во деталей - {details_count}\nОбщая стоимость - {price_sum}')
