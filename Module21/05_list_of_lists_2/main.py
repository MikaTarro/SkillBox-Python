s = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def mika_good(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return(mika_good(s[0]) + mika_good(s[1:]))
    return(s[:1] + mika_good(s[1:]))

print("Выпрямленный список: ", mika_good(s))
