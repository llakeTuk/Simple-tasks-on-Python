A = 0
print("welcome to leap year check")
def leapyear(A):
    A = int(input("Input year: "))
    if A % 4 == 0:
        return print('year is leap')
    elif A % 400 == 0:
        return print('year is leap')
    else:
        return print('year is not leap')
i = 'y'
while i == 'y':
    leapyear(A)
    i = input("Would you like to start new check?(y/n) ")
print("Goodbye")
