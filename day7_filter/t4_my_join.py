from functools import reduce

input_str = input().split()
sign = input()


def my_join(sep, items):
    result = reduce(lambda x, y: x + (sep if x else '') + y, items, '')
    return result


print(my_join(sign, input_str))
