# Lab5 World Series Results
    # FILE LOST
# Given a file with the World Series Champions since 1904
# Allow user to ask various questions about the results

def getChamps():
    # This function will get the data from the data file - be sure to look at the format of the data in the
    # file and read each line as we did with the phone search program in class.
    goodFile = False
    while goodFile == False:
        fname = input("Enter file name: ")
        try:
            dataFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename; try again.")
    print("")
    print("This is where you will get the data from the data file.")
    print("")
    yearList = []
    winnerList = []
    loserList = []
    for line in dataFile:
        line= line.strip()
        year, winner, loser = line.split(',')
        yearList.append(year)
        winnerList.append(winner)
        loserList.append(loser)
    dataFile.close()
    # Make sure to return the correct information from this function
    return yearList, winnerList, loserList

def getChoice():
    # This function displays the menu of choices for the user
    # It reads in the user's choice and returns it as an integer
    print("")
    print("Make a selection from the following choices:")
    print("1 - Find the World Series Winner and Loser for a particular year")
    print("2 - Count how many times a team has won the World Series")
    print("3 - Write to an output file all teams that have won the World Series")
    print("4 - Find the team that has won the most World Series Championships")
    print("5 - Find the team that has lost the most World Series Championships")
    print("6 - Quit")
    try:
        choice = int(input("Enter your choice --> "))
    except:
        print("That was not an option")
        choice = getChoice()
    print("")
    return choice

# find winner and loser for inputed year
def findWinnerandLoser(year, yearList, winnerList, loserList):
    i = 0
    winner = 0
    loser = 0
    passed = False
    while i < len(yearList):
        if year == yearList[i]:
            winner = winnerList[i]
            loser = loserList[i]
            passed = True
        i += 1
    if i == len(yearList):
        print("That year was not on the list.")
    return winner, loser, passed

        
# count win function
def countWins(team, winnerList):
    winCounter = 0
    i = 0
    while i < len(winnerList):
        if team == winnerList[i]:
            winCounter += 1
        i += 1
    return winCounter

# create win file
def teamWinnerFile(team, yearList, winnerList, loserList):
    outFile = open('parte.txt','w')
    i = 0
    while i < len(winnerList):
        if team == winnerList[i]:
            content = yearList[i] + ", " + loserList[i] + "\n"
            outFile.write(content)
        i += 1
    outFile.close()
    return

# find team that won the most
def wonMost(winnerList):
    i = 0
    teams = []
    counts = []
    while i < len(winnerList):
        thisTeam = winnerList[i]
        counts.append(winnerList.count(thisTeam))
        teams.append(thisTeam)
        while thisTeam in winnerList:
            winnerList.remove(thisTeam)
        i += 1

    countMost = 0
    for j in range(len(counts)):
        if counts[j] > countMost:
            countMost = counts[j]
            teamMost = teams[j]
    return teamMost, countMost



# find team that lost the most
def lostMost(loserList):
    i = 0
    teams = []
    counts = []
    while i < len(loserList):
        thisTeam = loserList[i]
        counts.append(loserList.count(thisTeam))
        teams.append(thisTeam)
        while thisTeam in loserList:
            loserList.remove(thisTeam)
        i += 1

    countLeast = 0
    for j in range(len(counts)):
        if counts[j] > countLeast:
            countLeast = counts[j]
            teamLeast = teams[j]
    return teamLeast, countLeast
    

# main function    
def main():    
    # Call the function to get the data from the data file and store the results in three lists
    yearList, winnerList, loserList = getChamps()
    choice = getChoice()
    while choice != 6:
        if choice == 1:
            year = input("Enter the year to search for: ")
            # Call the function to get the winner and the loser
            winner, loser, passed = findWinnerandLoser(year, yearList, winnerList, loserList)
            if (passed):
                print("The winner for ",year, " was ",winner,".")
                print("The loser for ", year, "was ",loser,".")
            choice = getChoice()

        elif choice == 2:
            team = input("Enter the team name: ")
            # Call the function to get the number of wins for the team
            winCounter = countWins(team, winnerList)
            print(team, " won the World Series ", str(winCounter), " times.")
            choice = getChoice()

        elif choice == 3:
            team = input("Enter the team name: ")
            # Call the function to create output file containing teams defeated by chosen team
            teamWinnerFile(team, yearList, winnerList, loserList)
            choice = getChoice()

        elif choice == 4:
            # Call the function to find the team that won the most championships
            teamMost, countMost = wonMost(winnerList)
            print(teamMost," won the World Series the most at ",countMost, " times.")
            choice = getChoice()

        elif choice == 5:
            # Call the function to find the team that lost the most championships
            teamLeast, countLeast = lostMost(loserList)
            print(teamLeast," lost the World Series the most at ",countLeast, " times.")
            choice = getChoice()

        else:
            print("Error in your choice")
            choice = getChoice()
    print("Good-bye")
