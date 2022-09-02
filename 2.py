import math
A = 0

def leap(A):
    A = int(input("Input year to check: "))
    if A % 4 == 0 and A % 100 != 0:
        print("Year is leap")
    elif A % 400 == 0:
        print("Year is leap")
    else:
        print("Year is not leap")   
  
i = 'y'
while i == 'y':
    leap(A)
    i = input("Would you like to start new check?(y/n) ")
print("Goodbye")
