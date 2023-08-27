pers_number = int(input('put ur number: '))

counter = 0

for i in range(2, pers_number // 2 + 1):
    if pers_number % i == 0:
        counter += 1
if counter == 0:
    print('ur number is prime')
else:
    print('number is not prime')


