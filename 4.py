import math
Number = 0
def simple(Number):
    Divisor = 2
    Number = int(input("Input number: "))
    if Number == 1:
        return False
    while Divisor < math.sqrt(Number):
        if Number % Divisor == 0:
            return False
        Divisor += 1
    return True  
i = 'y'
while i == 'y':
    Answer = simple(Number)
    if Answer:
        print("Number is simple")
    else:
        print("Number is not simple")
    i = input("Would you like to continue?(y/n) ")
print("Goodbye")
