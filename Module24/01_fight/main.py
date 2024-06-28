import random
class Warrior:
    def __init__(self):
        self.hp_warrior = 0

warrior_1 = Warrior()
warrior_2 = Warrior()
warrior_1.hp_warrior = 100
warrior_2.hp_warrior = 100

while True:
    who_beats = random.randint(0, 1)
    if warrior_1.hp_warrior == 0:
        print('Победил Ваня')
        break
    elif warrior_2.hp_warrior == 0:
        print('Победил Вася')
        break
    elif who_beats == 0:
        warrior_2.hp_warrior -= 20
        print('Вася дубасит Ваню')
        print(f'У Вани осталось {warrior_2.hp_warrior} здоровья\n')
    elif who_beats == 1:
        warrior_1.hp_warrior -= 20
        print('Ваня лупит Васю')
        print(f'У Васи осталось {warrior_1.hp_warrior} здоровья\n')
