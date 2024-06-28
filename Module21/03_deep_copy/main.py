site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

import copy
import pprint
def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, meaning)
            if result:
                return site


d_copy = dict()
goods = dict()
for _ in range(int(input('Сколько сайтов: '))):
    product_name = input('Введите название нового сайта: ')
    key = {'title': f'Куплю/Продам {product_name} недорого', 'h2': f'У нас самая низкая цена на :{product_name}'}
    for i in key:
        find_key(site, i, key[i])
    name_of_product = f'Сайт для {product_name}:'
    d_copy = copy.deepcopy(site)
    goods[name_of_product] = d_copy
    for key, value in goods.items():
        print(key)
        pprint.pprint(value)
        print()