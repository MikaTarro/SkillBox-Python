def is_prime(number):
    if number > 1:
        for j in range(2, int(number / 2) + 1):
            if (number % j) == 0:
                return False
        else:
            return True
    else:
        return False

def crypto(elem):
    answer = []
    for i, v in enumerate(elem):
        if is_prime(i) == True:
            answer.append(v)
    return answer

print(crypto('О Дивный Новый мир!'))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))