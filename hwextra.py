# HOMEWORKS IN PYTHON part 1

'''
1 USING FUNCTIONS
2 
3 
'''

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
