import math
value = 0
years = 0
percent = 0
def bank(value, years, percent):
    value = int(input("Input value of money: "))
    years = int(input("Input years: "))
    percent = int(input("Input percent: "))
    while years != 0:
        years -= 1
        value *=(1 + (percent / 100))
    print("value is ",round(value, 2))
i = 'y'
while i == 'y':
    bank(value, years, percent)
    i = input("Would you like to continue?(y/n) ")
print("Goodbye")
