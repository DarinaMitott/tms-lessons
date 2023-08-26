import random


class Generator:
    def __init__(self, l, number):
        self.l = l
        self.number = number

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration
        self.counter += 1
        name = ''.join([self.l[random.randint(0, len(self.l)-1)] for _ in range(random.randint(1, 10))])

        return f'{name}{self.counter}'


def new_name(n):
    letters = ['a', 'd', 'c', 'f', 'k', 'j', 'o', 'p', 'q']

    for counter in range(1, n + 1):

        name = ''.join([random.choice(letters) for _ in range(random.randint(1, 10))])

        yield f'{name}{counter}'


for item in new_name(5):
    print(item)


# for item in Generator(['a', 'd', 'c', 'f', 'k', 'j', 'o', 'p', 'q'], 5):
#     print(item)