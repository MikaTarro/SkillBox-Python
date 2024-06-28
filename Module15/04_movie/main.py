films = ['Хищник', 'Чужой', 'Властелин Колец', 'Звёздные воины', 'Стар трек', 'Город бога', 'Паразиты', 'Отступники', 'Хороший плохой злой']
add_films = []

films_count = int(input('Сколько фильмов хотите добавить?'))

for i in range(films_count):
    film_name = input('Введите название фильма: ')
    if film_name not in films:
        print(f'Ошибка. Фильма {film_name} у нас нет :(\n{'_' * 30}')

        continue
    add_films.append(film_name)
    print(film_name, 'добавлен в список Любимых фильмов')
print('Ваш спиоск любимых фильмов:', end='')
for i in add_films:
    print(i, end=',')

