# Программа загадывает случайное число от 0 до 100.
# Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если пользователь не угадал, подскажите ему в в какую сторону идти.
# То есть, если число пользователя слишком большое - выведите “не угадал, ваше число больше загаданного”.
# Если меньше - выведите “не угадал, ваше число меньше загаданного”.

import random

random_number = random.randint(0, 100)
attempts = 10
set_num_guest = set()
while attempts:
    pesr_guest = int(input(f'try to guess, u have {attempts} left '))
    attempts -= 1
    if pesr_guest in set_num_guest:
        print('this number has already been')
    else:
        set_num_guest.add(pesr_guest)
        if pesr_guest == random_number:
            print('u are right!')
            break
        elif pesr_guest > random_number:
            print('ur number is bigger')
        else:
            print('ur number is smaller')
else:
    print(f'no more attempts, hidden number was {random_number}')
