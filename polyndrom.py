y = 'y'
while y == 'y':
    bool = 0
    string = input("enter string: ") 
    if string == ''.join(reversed(string)):
        print('This is polyndrom')
    else:
        print('This is not polyndrom')
    y = input("Restart?(y/n): ")
