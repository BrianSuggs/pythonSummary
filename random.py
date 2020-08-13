# How to generate random numbers

import random


print(random.randrange(1, 10))

valid = false

while valid == false:
  low = int(input('Enter lower bound number '))
  high = int(input('Enter upper bound number '))
  
  if low < high:
    valid = true
  
  if low > high:
    print('Invalid parameters ')

print(random.randrange(low, high))
