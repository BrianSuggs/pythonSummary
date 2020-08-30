# CLASS HOMEWORKS IN PYTHON part 1

'''
1 COMPLEX CALCULATION
2 
3 
4 
5 
6 USING FUNCTIONS
'''


########################################################################################################################################

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


########################################################################################################################################

# 2
# Brian Suggs
# 2/5/18
# CSC 110 Assignment 2-1 -----------------------------------------------
# This program asks the user for the amount of a sales, and
# outputs the final sale after the discount is given.

# Get users input in form of sales amount
saleAmount = float(input("Enter amount of sale: $"))

# Calaulate the discounted sales amount based on the initial sales amount
if saleAmount > 4000:
    discount = .6 * saleAmount
elif saleAmount > 2000 and saleAmount < 4000:
    discount = .7 * saleAmount
elif saleAmount > 1000 and saleAmount < 2000:
    discount = .8 * saleAmount
elif saleAmount <= 1000:
    discount = .9 * saleAmount

# Print new amount to user
print ("Your discounted sale amount is $", discount)


# Brian Suggs
# 2/5/18
# CSC 110 Assignment 2-1 -----------------------------------------------
# This program asks for the score for each of the days a golfer plays,
# finds the lowest score, and prints out the result

# golfing 3 times a week for 3 weeks gives us 9 scores to keep track of
num = 9

# Initialize counter
i = 1

# Get user's initial input score that will be used as a reference as the
# lowest score for the time being
lowest_score = int(input("Enter score:  "))

# allows us to cycle through the rest of the users list of scores
while i < num:
    # use to get the last 8 numbers from the user
    golf_score = int(input("Enter score:  "))

    # condition use to replace the previous lowest score with the newest
    # lowest score
    if golf_score < lowest_score:
        lowest_score = golf_score

    # Increment to terminate the while loop
    i += 1

# print message to user
print ("Your lowest score for the three weeks is:  ", lowest_score )

    
# Brian Suggs
# 2/5/18
# CSC 110 Assignment 2-1 -----------------------------------------------
# keeps a running average of the number of bugs collected during the 7 days
# The program should ask for the number of bugs collected each day
# when the loop is finished, the program should display the average number
# of bugs collected in the week

# Variable used to control while loop
week = 7

# Varible that describes what day of the week it is to the user
num_days = 0

# Must initialize variable such that it is not a local variable within the
# while loop
bug_total = 0

#
while num_days < week:
    # Increment num_days to terminate the while loop
    num_days += 1

    # get users input of the number of bugs collected
    # change num_days, and int, into a string so that it can be concatinated
    # to the rest of the message
    num_bugs = int(input("How many bugs did you collect on day " + str(num_days) + "? "))

    # Get the sum of the bugs collected by adding the user's input number
    # with each interation
    bug_total += num_bugs

# Get average by dividing the total amount of the bugs collected by the number
# of days it took to collect them which in this case would be 7
bug_average = bug_total / week

# print average to user
print ("The average number of bugs collected this week is", round(bug_average,2))


########################################################################################################################################

# 1

########################################################################################################################################

# 1
# Function to get Data
def getData():
    numGrades = int(input("Enter number of grades: "))
    gradeList = []

    for i in range(numGrades):
        grade = int(input("Enter grade: "))
        gradeList.append(grade)

    threshold = int(input("Enter grade threshold: "))
    return gradeList, threshold


# Function to compute average of failing grades
def computeAverageFailing(gradeList, threshold):
    totalFailing = 0
    countFailing = 0
    for i in range(len(gradeList)):
        if gradeList[i] < threshold:
            totalFailing = totalFailing + gradeList[i]
            countFailing = countFailing + 1

        # Compute Average
        if countFailing > 0:
            averageFailing = totalFailing/ countFailing
            return averageFailing
        else:
            return -1


# Print Results
def printResults(average):
    if average == -1:
        print("No failing grades")
    else:
        print("Average failing grade is", average)
    return


# Main function
def main():
    gradeList, threshold = getData()
    average = computeAverageFailing(gradeList, threshold)
    printResults(average)

    
########################################################################################################################################

# 2
