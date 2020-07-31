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

x = 10            # assignment to int
y = "ten"         # assignment to string
w = x + y         # assignment error
w = x,y           # assignment to tuple   (10, 'ten')
z = x + 5         

print(x + y)      # error datas type is not computable
print(x,y,z)      # proper way to print multipule data types


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

#if statement
if(num2*2) == num1:
    print(num1, " is twice the size of ", num2)

#else statement
else:
    print("num2 is not a factor of num1")
    
#if-else statement

#while loop
while(i < num3):
    i += 1
    print("loop ", i)

#do-while loop

#for loop
for i in range(6):
    if i == 1:
        print(i, " dollar")
    else:
        print(i, " dollars")
    


########################################################################################################################################


# STRINGS


word = "I am a string \n"

word2 = "hi "

word3 = word2 + word

print(word3 * 3)


########################################################################################################################################


# FUNCTION CALLS


#main:



########################################################################################################################################

    
#COMMENTS

# single line comment

# there is no multi-line comment syntax
