skatesNUM: int = int(input('Кол-во коньков: '))
skatesCOUNT = []
footSiZE = []

for numbers in range(1, skatesNUM + 1):
    SkaNum = int(input(f'Размер {numbers}-й пары: '))
    skatesCOUNT.append(SkaNum)

countPL = int(input('\nКол-во людей: '))
for NumFoot in range(1, countPL + 1):
    FootNum = int(input(f'Размер ноги {NumFoot}-го человека: '))
    footSiZE.append(FootNum)

sovpadenie = list(set(skatesCOUNT) & set(footSiZE))

print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {len(sovpadenie)}')
