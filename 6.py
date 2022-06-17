month = 0
def seasons(month):
    month = int(input("Input month: "))
    if month in range(1,12):
      if month in (12,1,2):
        print('this is winter')
      elif month in (3,4,5):
        print('this is spring')
      elif month in (6,7,8):
        print('this is summer')
      else:
        print('this is autumn')
    else:
      print('incorrect number, enter number of month in range 1 - 12')
i = 'y'
while i == 'y':
    seasons(month)
    i = input("Would you like to continue?(y/n) ")
print("Goodbye")