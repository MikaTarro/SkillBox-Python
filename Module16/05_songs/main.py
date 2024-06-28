violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

myList = []
songs_count = int(input('Введите кол-во песен: '))
for number in range(songs_count):
    selected = ''.join(['Название ', str(number + 1),'-й', ' песни: '])
    myList.append(input(selected))

summ = 0

for k in violator_songs:
    if k[0] in myList:
        summ += k[1]

print('Общее время звучания песен', float('{:.4}'.format(summ)))