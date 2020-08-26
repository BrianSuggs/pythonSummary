# Given: Data file with names and grades
# Find: All students with passing grades
# use name_grades.txt

# Function to open data file
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter file name: ")
        try:
            gradeFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename, try again")
            
    return gradeFile

# Function to get data from file and store in two lists
def getData():
    gradeFile = openFile()
    nameList = []
    gradeList = []

    for line in gradeFile:
        line = line.strip()
        name, grade = line.split(',') # spliting at the comma and assign

        nameList.append(name)
        gradeList.append(int(grade))

    gradeFile.close    
    return nameList, gradeList

# Function to get passing grade
def getPassingGrade():
    OK = False
    while OK == False:
        try:
            passingGrade = int(input("Enter passing grade: "))
            OK = True
        except:
            print("Passing grade must be an integer")
    return passingGrade

# Function to print names of student with passing grades
def printPassingStudentNames(passingGrade, nameList, gradeList):
    for i in range(len(gradeList)):
        if gradeList[i] >= passingGrade:
            print(nameList[i])
    return

# Main function
def main():
    # when calling a function that returns a value, you must assign it
    # to a variable
    nameList, gradeList = getData()
    passingGrade = getPassingGrade()
    printPassingStudentNames(passingGrade, nameList, gradeList)
