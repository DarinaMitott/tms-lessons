input_list = [int(i) for i in range(0, int(input()))]


def generate_natural_cubes(new_list):
    return [x ** 2 for x in new_list]


print(generate_natural_cubes(input_list))


