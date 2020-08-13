# How to generate random numbers
import random

# generates random number from 1-10
print(random.randrange(1, 10))


valid = False

while valid == False:
  low = int(input('Enter lower bound number '))
  high = int(input('Enter upper bound number '))
  
  if low < high:
    valid = True
  
  if low > high:
    print('Invalid parameters ')

# generates random number between low and high
print(random.randrange(low, high))
