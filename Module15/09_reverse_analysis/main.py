from typing import List

numbers_list: list[int] = [7, 14, 3, 18, 21, 10, 9, 6]

for i in range(len(numbers_list) - 1, -1, -1):
    if numbers_list[i] % 2 == 0:
        print(numbers_list[i])
