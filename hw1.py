# 1
# Brian Suggs
# 1/29/18
# CSC 110 Assignment 1 -----------------------------------------------
# This program prints out the result of a complex calculations
a = 5
b = 2
c = 3

z = ((2*a - 3*b)/8) + (42/(a**2 - b**2)) * (((2/a) + (c/6))/b)
print (z)



# Brian Suggs
# 1/29/18
# CSC 110 Assignment 1 -----------------------------------------------
# This program prompts the user to enter a number. The program will then
# calculate the sales tax of that number

salesDollars = float(input("Enter the value of the company's" +
                           " sales in dollars in Auguest 2016:  $"))
salesTax = .06 * salesDollars

print ("The sales tax for the month of Auguest is  $", salesTax)
