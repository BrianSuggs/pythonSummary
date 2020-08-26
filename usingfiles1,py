# Given: A list of car speeds and a speed limit
# Find: The percentage of cars that exceed the speed limit
'''
# Get
def getSpeeds():
    numSpeeds = int(input("How many cars were monitored? "))

    speedList[]

    for i in range(numSpeeds):
        speed = float(input("Enter speed: "))
        speedList.append(speed)

    return speedlist
'''

# Open data file - using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        try:
            speedFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name, please try again")
    return speedFile


# Get the speeds from a data file
# use speed1.txt
def getSpeeds():
    #fname = input("Enter name of data file: ")
    speedFile = openFile()
    speedList = []

    for line in speedFile:
        line = line.strip()
        speed = float(line)
        speedList.append(speed)
    
    '''
    line = speedFile.readline()
    line = line.strip()
    while line != "":
        speed = float(line)
        speedList.append(speed)
        line = speedFile.readline()
        line = line.strip
    speedFile.close
    '''
    
    return speedList


# Get speed limit and make sure it is a number
def getSpeedLimit():
    OK = False
    while OK == False:
        try:
            speed = float(input("Enter speed limit: "))
            OK = True
        except ValueError:
            print("Speed must be a float, please try again...")
        return speedLimit
    

# Count the number of speeds that exceed the speed limit
def countAboveLimit(speedList):
    limit = float(input("limit: "))

    total = 0

    for i in range(len(speedList)):
        if speedList[i] > limit:
            total = total + 1

        return total

# use speed1.txt
def main():
    speedList = getSpeeds()
    totalAbove = countAboveLimit(speedList)
    percentAbove = totalAbove/ len(speedList) * 100
    print("The percentage of cars that exeed the speed limit is " +
          str(percentAbove) + "%")
