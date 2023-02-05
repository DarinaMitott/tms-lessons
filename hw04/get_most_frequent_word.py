from collections import Counter

input_list = [i for i in input('put number with space ').split()]

counterWord = Counter(input_list)
output = counterWord.most_common(1)
print(output)
print(f'the most frequent word "{output[0][0]}", it occurs {output[0][1]} times')

