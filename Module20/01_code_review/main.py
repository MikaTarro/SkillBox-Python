students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
# Список пар "ID студента — возраст": [(1, 23), (2, 24), (3, 22)]
# Полный список интересов всех студентов: {'running', 'computer games', 'math', 'languages', 'biology, swimming', 'health food'}
# Общая длина всех фамилий студентов: 20


def stud_info(dict):
    id_age = [(i, dict[i]['age']) for i in dict]
    interests = [j for i in dict for j in dict[i]['interests']]
    len_surname = 0
    for i in dict:
        len_surname += len(dict[i]['surname'])

    print(f'''Список пар: {id_age}
Список интересов: {interests}
Общая длина всех фамилий: {len_surname}''')

stud_info(students)



