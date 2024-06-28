with open('registrations.txt', 'r', encoding='utf-8') as file, \
    open('registrations_good.log', 'w', encoding='utf-8') as good_log_file, \
    open('registrations_bad.log', 'w', encoding='utf-8') as bad_log_file:
    for line in file:
        line = line.rstrip()
        info_list = line.split()
        try:
            if len(info_list) != 3:
                raise IndexError(f'{line}  -  НЕ присутствуют все три поля.')
            if not info_list[0].isalpha():
                raise NameError(f'{line}  -  Поле «Имя» содержит НЕ только буквы.')
            if ('@' not in info_list[1]) or ('.' not in info_list[1]):
                raise SyntaxError(f'{line}  -  Поле «Имейл» НЕ содержит @ и . (точку)')
            if not 10 <= int(info_list[2]) <= 99:
                raise ValueError(f'{line}  -  Поле «Возраст» НЕ является числом от 10 до 99.')
        except (IndexError, NameError, SyntaxError, ValueError) as exception:
            bad_log_file.write(f'{exception}\n')
        else:
            good_log_file.write(f'{line}\n')
