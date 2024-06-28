list_container = []
cont_count = int(input('Введите количество контейнеров: '))
for _ in range(cont_count):
    kg_cont = int(input('Вес контейнера: '))
    list_container.append(kg_cont)
new_container = int(input('\nНовый контейнер: '))
name = 0
while name < len(list_container) and list_container[name] >= new_container:
    name += 1
    if name == len(list_container):
        break
print('Номер, который получит новый контейнер:', name + 1)
