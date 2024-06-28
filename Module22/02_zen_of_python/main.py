import os
print()

# with open('zen.txt') as f:
#     for text in reversed(f.readlines()):
#         print(text, end='\n')

file = open('zen.txt', 'r')
s = file.readlines()
s.reverse()
print(''.join(s).strip('\n'))

file.close()