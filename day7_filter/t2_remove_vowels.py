input_list = [i for i in input().split()]


def remove_vowels(l):
    outputlist = list(filter(lambda letter: letter not in 'aeyoiu', l))
    return outputlist


print(remove_vowels(input_list))
