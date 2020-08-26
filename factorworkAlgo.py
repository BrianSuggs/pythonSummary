# Find:  All pairs of integer factors of n.

import math

# Function to find all factor pairs of a given number n
# Considers all possible combinations of number pairs from 1 to n
# Goes through from 1 to n n times 
def findFactors1(n):
    work = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            work = work + 1
            if i*j == n:
                a = 0
                print(i, " and ", j, " are factors of ", n)
    print("Amount of work: ", work)
    return



# Function to find all factor pairs of a given number n
# Goes through the loop n times 
def findFactors2(n):
    work = 0
    for i in range(1,n+1):
        work = work + 1
        if n % i == 0:
            j = int(n/i)
            print(i, " and ", j, " are factors of ", n)
    print("Amount of work: ", work)
    return



# Function to find all factor pairs of a given number n
# Uses the least amount of work of the three functions
# Goes through the loop only sqrt(n) times
def findFactors3(n):
    i = 1
    work = 0
    while i <= math.sqrt(n):
        work = work + 1
        if n % i == 0:
            j = int(n / i)
            print(i, " and ", j, " are factors of ", n)
        i = i + 1
    print("Amount of work: ", work)
    return
