def my_decorator(func):
    def inner_func(y):
        print(y)
        value = func(y)
        print(value)
        return value

    return inner_func


@my_decorator
def my_func(x):
    return x ** 2


y = my_func(3)
print(f'y = {y}')
