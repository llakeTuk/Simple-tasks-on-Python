y = 'y'
while y == 'y':
  number = input('enter number: ')
  digits = [int(i) for i in str(number)]
  print('digits in number: ', *digits)
  print('sum of digits: ', sum(digits))
  y = input('restart?(y/n): ')
  print('goodbye')
