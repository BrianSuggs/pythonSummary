# Brian Suggs
# 3/19/18
# CSC 110 Assignment 6-1 -----------------------------------------------
# This program is composed of two different search algorithms:
# linear search and binary search
# this program will prompt the user for a year which would then find that year
# in a list using both linear and binary search
# after the year is found, the program will print out how many comparisons each
# algorithm took as well as the data of the file from that year

# Function to open a file - using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        # Begin exception handling
        try:
            # Try to open the file using the name given
            infile = open(fname, 'r')
            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("Invalid filename, please try again ... ")
    return infile


# Function to read data into lists
def getLists():
    infile = openFile()

    # dodge header by reading the next line
    line = infile.readline()
    line = infile.readline()
    
    yearList = []
    totalList = []
    maleList = []
    femaleList = []
    femalePercentList = []

    while line != "":
        line = line.strip()
        # split data into items
        year, total, male, female, femalePercent = line.split(',')

        # add items to list
        yearList = yearList + [year]
        totalList = totalList + [total]
        maleList = maleList + [male]
        femaleList = femaleList + [female]
        femalePercentList = femalePercentList + [femalePercent]
        
        line = infile.readline()

    infile.close()

    return yearList, totalList, maleList, femaleList, femalePercentList


# Linear search
def getYearLinear(yearList, userYear):
    linearComparison = 0 
    i = 0
    found = 0
    
    while i < len(yearList) and found == 0:
        # comparison counter
        linearComparison += 1
        
        if yearList[i] == userYear:
            # position of year the user is searching for in the list
            linePosition = i
            found = 1
        else:
            # increment
            i += 1

    if i == len(yearList) and found == 0:
        print("Linear search: comps = ", linearComparison)
        print("year not found")
        return
    else:
        print("Linear search: comps = ", linearComparison)
        # return the position in the list of that year
        return linePosition


# Binary search
def getYearBinary(yearList, userYear):
    binaryComparison = 0
    
    # left side of list    
    left = 0	
    # right side of the list				
    right = len(yearList) - 1		
    found = 0

    # sample code
    while right >= left and found == 0:
        binaryComparison += 1
        
	# find the middle of the list
        m = (left + right) // 2

        # condition used to figure out where to place the marker
        if yearList[m] == userYear:
            found = 1

        # cut out left side of list
        elif userYear > yearList[m]:
            left = m + 1

        # cut out right side of list
        else:
            right = m - 1

    print("Binary search: comps = ", binaryComparison)
            
    if found == 0:
        return ""

    # return the position in the list of that year
    else:
        bPosition = m
        return bPosition

def main():
    yearList, totalList, maleList, femaleList, femalePercentList = getLists()

    userYear = input("Enter year to search for: ")

    bPosition = getYearBinary(yearList, userYear)
    linePosition = getYearLinear(yearList, userYear)

    print("The number of graduates in ", str(userYear), " was, ",
          str(totalList[bPosition]))
    print("Male: ", str(maleList[bPosition]))
    print("Female: ", str(femaleList[bPosition]))
    print("Percent Female: ", str(femalePercentList[bPosition]))

# the worst case input for linear search is when the year or item you are trying
# to find happens to be the last item in the list
# the worst case input for linear search is when the year or item you are
# trying to find is either the first or last item in the list

# linear search usually requires more work than binary search. However, linear
# search performs better when the item that is being searched happens to be
# the first item in the list



###########################################################################################################################################################



# Brian Suggs
# 3/19/18
# CSC 110 Assignment 6-2 -----------------------------------------------
# This program will sort two lists based on female percent values


# Function to open a file - using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        # Begin exception handling
        try:
            # Try to open the file using the name given
            infile = open(fname, 'r')
            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("Invalid filename, please try again ... ")
    return infile


# get nessecary data
def getLists():
    infile = openFile()
    line = infile.readline()
    
    yearList = []
    femalePercentList = []

    while line != "":
        line = line.strip()
        # split data into items
        year, total, male, female, femalePercent = line.split(',')

        # add item to list
        yearList = yearList + [year]
        femalePercentList = femalePercentList + [femalePercent]
        
        line = infile.readline()

    infile.close()
    return yearList, femalePercentList


# function that sorts two lists at the same time
# if you swap a value in list1, the value in list2 in the same position
# will also be swapped
def dualSort(femalePercentList, yearList):
    for i in range(0, len(femalePercentList)):            
        min = i
        for j in range(i + 1, len(femalePercentList)):
            # comparison
            if femalePercentList[j] < femalePercentList[min]:
                min = j
        # swap
        femalePercentList[i], femalePercentList[min] = femalePercentList[min], femalePercentList[i]
        yearList[i], yearList[min] = yearList[min], yearList[i]
    return yearList, femalePercentList


def main():
   yearList, femalePercentList = getLists()
   yearList, femalePercentList = dualSort(femalePercentList, yearList)
   for i in range(len(yearList)):
       print(yearList[i], femalePercentList[i])


