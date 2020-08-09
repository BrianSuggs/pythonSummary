# Percentage finder
# finds the percentage difference between two numbers

def ptEval(startNum, endNum):
    numDiff = endNum - startNum
    percent = (numDiff / startNum) * 100
    percent = round(percent, 2)

    print('Start: ', startNum, '\t End: ', endNum)

    if numDiff < 0:
        print('Account decreased by ', percent, '%')
    
    if numDiff > 0:
        print('Account increased by ', percent, '%')




# finds the number that is a certain percentage away from the base number
def ptChange(startNum, percent):
    endNum = 0
    percent /= 100
    
    if percent > 0:
        endNum = startNum * (1 + percent)

    if percent < 0:
        endNum = startNum * (1 + percent)

    endNum = round(endNum, 2)

    print('Start', '\t % Change', '\t Result')
    print(startNum, '\t', percent, '% \t \t', endNum)

        

# finds the return on an initial investment over x number of months
def ptInvest(startNum, percent, months):

    print('Initial investment of $', startNum,
          ' with a monthly return of ', percent, '%')
    
    percent = 1 + (percent / 100)
    endNum = startNum * (percent ** months)
    endNum = round(endNum, 2)

    print('becomes $', endNum,
          ' after ', months, ' months')


def main():
    print('1 -- Find the percentage difference between two numbers')
    print('2 -- Find the number given the percent change')
    print('3 -- Find the return on an initial investment over a number of months')
    choice = int(input('Make a selection '))

    if choice == 1:
        startNum = float(input('type your starting number '))
        endNum = float(input('type your ending number '))
        choice1 = ptEval(startNum, endNum)

    if choice == 2:
        startNum = float(input('type your starting number '))
        percent = float(input('type your percent change '))
        choice2 = ptChange(startNum, percent)

    if choice == 3:
        startNum = float(input('Enter initial investment '))
        percent = float(input('Enter monthly return percent rate '))
        months = int(input('Enter the number of months '))
        choice3 = ptInvest(startNum, percent, months)

    if choice != 1 and choice != 2 and choice != 3:
        print('Invalid entry')




