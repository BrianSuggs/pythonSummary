# Lab 2 

# Part 1 Implementing Exponentials
a = int(input("Enter base number "))
b = int(input("Enter power number "))
c = 1

i = 0
while i < b:
    c = c * a
    i += 1
print (a, "To the power of ", b, "is ", c)



# Part 2 even vs odd
odd = 0
even = 0
i = 0

while i < 10:
    num = int(input("Enter integer: "))
    
    if num % 2 > 0:
        odd = odd + 1
    elif num % 2 == 0:
        even = even + 1

    i += 1
              

print("even: ", even)
print("odd: ", odd)



# Part 3 Find the sum of numbers that are divisible by 3 and 5
num = int(input("number: "))
sum = 0
i = 0

while i < num:
    num -= 1
    if num % 3 == 0:
        sum += num
    elif num % 5 == 0:
        sum += num

print ("The sum is: ",sum)



# Part 4 Guessing game
import random

n = random.randint(1,100)
user_num = 0 
num_guess = 0
i = 0

while user_num != n:
    num_guess += 1
    user_num = int(input("Enter num: "))
    if user_num > n:
        print("Guess is too high")
    elif user_num < n:
        print("Guess is too low")
    elif user_num == n:
        print("Guess is correct")


print("You took ", num_guess, "guesses to guess right")

