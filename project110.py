# Brian Suggs
# 4/30/18
# CSC 110 Programming Porject Part 2 ------------------------------------------
# Program Title:  Movies Data

# The program will allow the user to get answers to various questions about
# the movies in the data file.

# For this assignment you will write a program to read in a large data file
# with information about movies that were released between 2000 and 2009.

def getData():
    # throw exception for invalid


# 1 Function finds all films produced by a certain studio

def firstOption(titleList, genreList, timeList, ratingList, studioList, yearList):
    userStudio = input('Enter studio: ')
    # throw exception...
    if userStudio in studioList:
    #-append all movie information of studio to a new list called userList1-
    return userList1


# 2 Function finds the longest film of a specific genre
def secondOption():
    userGenre = input('Enter genre')
    # throw exception...
    if userGenre in genreList:
    # compare the runtime of all movies in the chosen genre using selection sort
    # -maybe have to make another list-
    # return the movie information with longest runtime
    return userList2


# 3 Function finds all films made in a given year range with a chosen rating
def thirdOption():
    userYear1 = int(input('Year1: '))
    userYear2 = int(input('Year2: '))
    if userYear1 > userYear2:
        print('Second year should be after first year - try again')
        # prompt user again for years in the right order
    userRating = input('Enter rating: ')
    # throw exception...
    if userRating in ratingList:
        # append movies from year range with specified rating
        # use linear search
        if yearList[i] >= userYear1 and yearList[i] <= userYear2 and
                                            ratingList == userRating:
        # add list items to userList3
    return userList3


# 4 Function searches for a film by title (binary search)
# display all info about the film with a specific title
def fourthOption():
    userTitle = input('Enter title: ')
    # throw exception...
    if userTitle in titleList:
    # use binary search to find placement of userTile
        userList4 = titleList[i] + genreList[i] + str(timeList[i]) + rating[i] +
                                               studioList[i] + yearList[i]
    return userList4


# 5 Find the average runtime of films with a certain rating
def fifthOption():
    userRating = input('Enter rating ')
    # throw exception...
    totalTime = 0
    runTimeNum = 0
    if userRating in ratingList:
    for i in range(ratingList):
        if ratingList == userRating:
            totalTime += timeList[i]
            runTimeNum += 1
    aveRunTime = totalTime // runTimeNum
    return aveRunTime, userRating


# 6 Sort all list by year produced and write the results to a new file
# create a list of indexes that you sort based on the order of the runtime
def sixthOption():
    # use binary search to sort list by year
    sortedList = input('Enter name of output file ')
    # write new list into outfile
    return sortedList


def main():
    titleList, genreList, timeList, ratingList, studioList, yearList = getData
    print('Please choose one of the following options: ')
    print('1 -- Find all films produced by a certain studio')
    print('2 -- Find the longest film of a specific genre')
    print('3 -- Find all films made in a given year range with a specific rating')
    print('4 -- Search for a film by title ')
    print('5 -- Find average runtime of films with a certain rating')
    print('6 -- Sort all lists by year and write the results to a new file ')
    print('7 -- Quit ')
    choice = int(input('Choice ==> '))

    if choice == 1:
        userList1 = firstOption()
    if choice == 2:
        userList2 = secondOption()
    if choice == 3:
        userList3 = thirdOption()
    if choice == 4:
        userList4 = fourthOption()
    if choice == 5:
        aveRunTime, userRating = fifthOption()
        print('The average runtime for films with a', userRating, ' is' , str(aveRunTime))
    if choice == 6:
        sixthOption()
    else:
        print('You Quit')
