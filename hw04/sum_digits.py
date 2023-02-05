pers_number = int(input('ur number '))
sum_output = 0

while pers_number:
    temporary_variable = pers_number % 10
    sum_output += temporary_variable
    pers_number //= 10

print(sum_output)

