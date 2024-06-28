violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

time_sound = 0
sunds_counter = int(input('Введите количество песен: '))
for sounds in range(1, sunds_counter + 1):
    sound_name = input('Введите название песни: ')
    if sound_name in violator_songs:
        s = violator_songs.get(sound_name)
        time_sound += s
    else:
        print('Песня с названием  {0} не найдена'.format(sound_name))
print('Общее время звучания песен {0} :',time_sound, 'минуты.'.format(sound_name)) # Не понимаю почему название не выводит.. ((



