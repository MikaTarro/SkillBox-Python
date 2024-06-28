import random

team_1 =[round(random.uniform(5.0, 10.0),2) for _ in range(1, 20 + 1)]
team_2 =[round(random.uniform(5.0, 10.0),2) for _ in range(1, 20 + 1)]
result = []
for i in range(len(team_1)):
    result.append(max(team_1[i], team_2[i]))



print(f'первая команда: {team_1}\nВторая команда: {team_2}\nПобедители тура!{result}')




