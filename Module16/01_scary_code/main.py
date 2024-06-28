# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# TODO переписать программу

a_list = [1, 5, 3]
b_list = [1, 5, 1, 5]
c_list = [1, 3, 1, 5, 3, 3]

a_list.extend(b_list)
count_FIVE = a_list.count(5)
print(count_FIVE)
for _ in range(count_FIVE):
    a_list.remove(5)

a_list.extend(c_list)
count_THREE = a_list.count(3)
print(count_THREE)
print(a_list)
