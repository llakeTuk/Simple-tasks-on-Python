y = 'y'
while y == 'y':
  a, b = int(input("enter number of people: ", )), int(input("enter count number: ", ))
  survivor = 0
  for i in range(1, a + 1):
    survivor = (survivor + b) % i
  print("survivor is number: ", survivor + 1)
  y = input("restart?(y/n): ", )
Print("goodbye")
