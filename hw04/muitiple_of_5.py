# вывести на экран числа кратные 5 от 0 до 100 включительно.
# Сделать это с помощью функции range с шагом 5
# Сделать это с помощью функции range c шагом 1 и вложенным if
list_mult5 = []
for i in range(5, 101, 5):
    list_mult5.append(i)

print(list_mult5)

new_list_mult5 = []

for i in range(5, 101):
    if i % 5 != 0:
        continue

    else:
        new_list_mult5.append(i)

print(new_list_mult5)
