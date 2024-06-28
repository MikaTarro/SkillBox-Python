# sum([[1, 2, [3]], [1], 3])
# Ответ в консоли: 10
#
# sum(1, 2, 3, 4, 5)
# Ответ в консоли: 15

def mika_sum(*args, total=0):
    for arg in args:
        if isinstance(arg, (int | float)):
            total += arg
        elif isinstance(arg, list | tuple):
            total += mika_sum(*arg)                 # * что бы раскрыть списки в списках
    return total


print(mika_sum([[1, 2, [3]], [1], 3]))
print(mika_sum(1, 2, 3, 4, 5))
