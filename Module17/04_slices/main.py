# 1: abcdefg
# 2: gfedcba
# 3: aceg
# 4: bdf
# 5: a
# 6: g
# 7: d
# 8: efg
# 9: de
# 10: ed

alphabet = 'abcdefg'

print('1: ', alphabet[:])
print('2: ', alphabet[::-1])
print('3: ', alphabet[::2])
print('4: ', alphabet[1::2])
print('5: ', alphabet[:1])
print('6: ', alphabet[-1:-2:-1])
print('7: ', alphabet[3:4])
print('8: ', alphabet[-3:])
print('9: ', alphabet[3:5])
print('10: ', alphabet[4:2:-1])
# abcdefg