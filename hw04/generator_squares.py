input_list = [int(i) for i in input('put number with space ').split()]


def transform_into_squares(new_list):
    return [x ** 2 for x in new_list]


print(transform_into_squares(input_list))
