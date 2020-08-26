# Given: List of grades and a failing threshold
# Find: Average of all failing grades

#----------------------------------------------------------------------
# Get student grades and store in a list
gradeList = []

# Get number of grades from user
numGrades = int(input("Enter number of grades: "))

i = 0
while i < numGrades:
    grade = int(input("Enter a grade: "))
    gradeList.append(grade)
    i += 1

print(gradeList)

# Get failing threshold
threshold = int(input("What is the failing threshold? "))

#Initialize accumulator for total failing grades
total = 0

# Initialize failing counter
failCounter = 0

for i in range(len(gradeList)):
    if gradeList[i] < threshold:
        total = total + [i]
        failCounter = failCounter + 1

if failCounter == 0:
    print("No failing grades")
else:
    average = total / failCounter
    print("The average of failing grades is ")

# For every grade in the list
# if grade < threshold
#    add grade to total
#    add 1 to failing counter

# compute average
# print average

