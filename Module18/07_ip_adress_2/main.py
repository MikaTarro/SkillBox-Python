while True:
    enter_IP = input("\nВведите IP: ").split(".")

    for i_numb in enter_IP:
        if not i_numb.isdigit():
            print(f"{i_numb} - это не целое число.")
            break
        elif int(i_numb) > 255:
            print(f"{i_numb} превышает 255.")
            break
        elif len(enter_IP) != 4:
            print("Адрес — это четыре числа, разделённые точками.")
            break
    else:
        print("IP-адрес корректен.")

# Введите IP: 128.16.35.a4
# a4 — это не целое число.
#
# Введите IP: 240.127.56.340
# 340 превышает 255.
#
# Введите IP: 34.56.42,5
# Адрес — это четыре числа, разделённые точками.
#
# Введите IP: 128.0.0.255
# IP-адрес корректен.