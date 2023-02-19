seconds = int(input('please write number of seconds: '))
output = f' days {seconds // (24 * 3600)}\n hours {seconds // 3600}\n minutes {seconds // 60}\n seconds {seconds % 60}'
print(output)

