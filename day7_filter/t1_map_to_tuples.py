input_information = map(str, input().split())


def map_to_tuples(input_inf):
    just_list = [i.lower() for i in input_inf]
    output = []
    for i in just_list:
        output.append((i.upper(), i))
    return output


print(map_to_tuples(input_information))
