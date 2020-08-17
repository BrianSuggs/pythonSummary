# Percentage finder
# finds the percentage difference between two numbers

def ptEval(startNum, endNum):
    #endNum = float(input('Next number '))

    numDiff = endNum - startNum
    percent = (numDiff / startNum) * 100
    percent = round(percent, 2)

    print('Start: ', startNum, '\t End: ', endNum)

    if numDiff < 0:
        print('Account decreased by ', percent, '%')
    
    if numDiff > 0:
        print('Account increased by ', percent, '%')
    
    return endNum


def main():
    entryNum = int(input('How many entries? '))
    startNum = float(input('Enter the inital number '))
    endNum = float(input('Next number '))
    
    for x in range(entryNum):
      startNum = ptEval(startNum, endNum)
      



