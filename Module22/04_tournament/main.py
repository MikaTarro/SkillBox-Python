import os

text_first_tour = ['80', 'Ivanov Serg 80', 'Sergeev Petr 92',
                   'Petrov Vasiliy 98', 'Vasiliev Maxim 78']
with open('first_tour.txt', 'w') as new_file_one:
    for line in text_first_tour:
        new_file_one.write(line + '\n')

number_of_scores = []
with open('first_tour.txt', 'r') as read_line_add_in_list:
    k = int(read_line_add_in_list.readline())
    for line in read_line_add_in_list:
        new_line = line.split()
        if int(new_line[-1]) > k:
            number_of_scores.append(new_line)

number_of_scores.sort(key=lambda a: int(a[-1]))
number_of_scores.reverse()
with open('second_tour.txt', 'w') as new_file_two:
    new_file_two.write(str(len(number_of_scores)))
    for i_elem_list, obj_elem_list in enumerate(number_of_scores, 1):
        new_file_two.write('\n' + str(i_elem_list) + ')' + ' ' +
                           obj_elem_list[1][0] + '. ' + obj_elem_list[0]
                           + ' ' + obj_elem_list[2])

with open('first_tour.txt') as file_one, open('second_tour.txt') as file_two:
    print(f'Содержимое файла first_tour.txt:\n{file_one.read()}'
          f'\nСодержимое файла second_tour.txt:\n{file_two.read()}')