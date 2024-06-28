# Придумайте пароль: qwerty
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty12
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty123
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qWErty123
# Это надёжный пароль!

def master_Password(pass_word: object) -> object:
    if (sum(map(str.isupper, pass_word)) >= 1               # Кол-во Заглавных
            and len(pass_word) >= 8                         # Проверяем на длину более 8 символов
            and sum(c.isdigit() for c in pass_word) >= 3):  # Кол-во цифр более 3трёх =)
        print("Это надёжный пароль!", pass_word)
    else:
        print('Пароль ненадёжный.')



while True:
    password = input("\nПридумайте пароль: ")
    print(master_Password(password))
