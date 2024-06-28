# big_list = [[x for x in range(1, 13, 4)], [x for x in range(2, 13, 4)], [x for x in range(3, 13, 4)], [x for x in range(4, 13, 4)]]
new_list = [[x for x in range(i, 13, 4)] for i in range(1,5)]
print(new_list)