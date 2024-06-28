# TODO здесь писать код
u_name = input('enter u Name: ')
while True:
    print('увидеть текст чата введи: 1, написать сообщение введите: 2.')
    response = input('1 или 2: ')
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Служебное сообщение: пока ничего нет\n')
    elif response == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a') as file:
            file.write('{name}: {message}\n'.format(
                name=u_name, message=new_message))
    else:
        print('Неизвестная команда!')
# enter u Name: MIka
# увидеть текст чата введи: 1, написать сообщение введите: 2.
# 1 или 2: 2
# Введите сообщение: asd
# увидеть текст чата введи: 1, написать сообщение введите: 2.
# 1 или 2: 1
# MIka: asd
#
# увидеть текст чата введи: 1, написать сообщение введите: 2.
# 1 или 2: