# Percentage finder PART 2

# finds the percentage difference between two numbers
def ptEval(startNum, endNum):
    numDiff = endNum - startNum
    percent = (numDiff / startNum) * 100
    percent = round(percent, 2)

    if numDiff < 0:
        print('Start: ', startNum, '\t End: ', endNum,
              '\t', percent, '%')
    
    if numDiff > 0:
        print('Start: ', startNum, '\t End: ', endNum,
              '\t +', percent, '%')

    return endNum


# Finds the percentage change from a sequence of numbers while using a list
def percentList():
    entryNum = int(input('How many entries? '))
    numList = []

    for x in range(entryNum):
        entry = float(input('Enter number '))
        numList.append(entry)

        if len(numList) > 1:
            ptEval(numList[x-1], numList[x])

    # prints the percentage change from first and last entry
    print('\n')
    ptEval(numList[0], numList[x])


# Finds the percentage change from a sequence of numbers
def main():
    entryNum = int(input('How many entries? '))
    startNum = float(input('Enter the inital number '))
    
    for x in range(entryNum):
        endNum = float(input('Next number '))

        # the new starNum is the old endNum
        startNum = ptEval(startNum, endNum)

