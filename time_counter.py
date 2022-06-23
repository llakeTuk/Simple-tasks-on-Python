y = 'y'
while y == 'y':
    seconds = int(input("Enter amount of seconds: "))
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')
    y = input('restart?(y/n): ')
