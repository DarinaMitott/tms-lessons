from calendar import monthrange

year = int(input('year: '))
month = int(input('month: '))
days = monthrange(year, month)[1]
print(days)
