import math
A = 0
p = 0
s = 0
d = 0
B = (p, s, d)
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
