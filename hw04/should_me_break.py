# Программа выводит на экран числа от 0 до 100.
# После вывода каждого числа спрашивайте у пользователя “Should we break?”.

while True:
    for i in range(101):
        x = input('Should we break? ').lower() == 'no'
        if x == 'yes':
            break
        print(i)



