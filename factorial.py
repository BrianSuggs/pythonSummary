# Factorial Function 

def factorial(n):
    i = n
    f = 1
    while i > 0:
        f = f * i
        i = i - 1
    return f
