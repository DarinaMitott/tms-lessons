pers_sum, deposit_years = int(input('ur sum: ')), int(input('for how many years: '))

while deposit_years:
    deposit_years -= 1
    pers_sum += 0.1 * pers_sum
print(f'ur sum will be {pers_sum:.02f}')
