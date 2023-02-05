input_list = [i for i in input('put number with space ').split()]

words = dict()


def get_longest_word(new_list):
    for word in new_list:
        words[len(word)] = word

    biggest_word = words[max(words)]
    return biggest_word


print(get_longest_word(input_list))
