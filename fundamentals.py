# FUNDAMENTALS OF PYTHON

'''
1 Syntax
2 Operators & Operands
3 Statments & Conditions
4 Strings
5 Function Calls
6 Comments
'''

########################################################################################################################################


# SYNTAX - Values and Variables

#Illegal variable names:
'''
2myvar = "John"   # begining variable name with a number
my-var = "John"   # using a special character in the variable name (only underscore _ is allowed)
my var = "John"   # using a special character in the variable name
'''


x = 10            # assignment to int
y = "ten"         # assignment to string
#w = x + y         # assignment error data types are not computable
w = x,y           # assignment to tuple   (10, 'ten')
z = x + 5         

#print(x + y)      # error datas type is not computable
print(x,y,z)      # proper way to print multipule data types


# Multi-Assignment  
# assign values to multiple variables in one line
x, y, z = 35, "Banana", "Cherry"
print(x)
print(y)
print(z)

# assign the same value to multiple variables in one line
x = y = z = "Apple"
print(x)
print(y)
print(z)


# Global variables
# variables created outside of functions
# alternatively you can cast it to the global scope by using the keyword global
global lastnumber = 999

########################################################################################################################################


# OPERATORS & OPERANDS

'''
operatiors are icons for coomputation
  +   is addition
  -   is subtraction
  *   is multiplication
  **  is to the power of
  /   is division
  //  is floor division
  %   is modulus
  =   is assignment
  
 Logical operators
  ==  is check if equal
  !=  is check if not equal
  |   is logical OR
  &   is logical AND
  not is logical NOT
 
 Keywords
  in
  type

Python follows PEMDAS
'''

########################################################################################################################################


# STATEMENTS & CONDITIONS

i = 0
num1 = 12
num2 = 6
num3 = 10

# if statement
if(num2*2) == num1:
    print(num1, " is twice the size of ", num2)

# else statement
else:
    print("num2 is not a factor of num1")
    
# elif statement
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#while loop
while(i < num3):
    i += 1
    print("loop ", i)

# do-while loop 

#for loop
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for i in range(6):
  # grammerly correct
  if i == 1:
    print(i, " dollar")
  else:
    print(i, " dollars")

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: 
# range(2, 6), which means values from 2 to 6 (but not including 6)
for x in range(2, 6):
  print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for x in range(2, 30, 3):
  print(x)



########################################################################################################################################


# STRINGS


word = "I am a string \n"

word2 = "Hi "

word3 = word2 + word    # this is legal because the varibles are the same type, str

print(word3 * 3)


########################################################################################################################################


# FUNCTION CALLS

def function1():
  num1 = 10
  num2 = 5
  x = num1 * num2
  return x

def function2():
  num1 = 50
  num2 = 10
  x = num1 * num2
  print(x)

def main():
  # multi has the value of x
  multi = function1()
  print(multi)
  
  # you can also call without assigning a variable
  # but this would require having the print statement in the function
  function2()



########################################################################################################################################

    
#COMMENTS

# single line comment

# there is no multi-line comment syntax

"""

alternative to multi-line commenting

"""
