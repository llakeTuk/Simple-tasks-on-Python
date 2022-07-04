import math
A = 0
B = (0, 0, 0)
def square(A):
    A = int(input("Input value of square side: "))
    p = A * 4
    s = A ** 2
    d = A * math.sqrt(2)
    return p, s, d
i = 'y'
while i == 'y':
    B = square(A)
    print(B)
    i = input("Would you like to start new calculation?(y/n) ")
print("Goodbye")
