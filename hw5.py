# Brian Suggs
# 2/24/18
# CSC 110 Assignment 5-1 -----------------------------------------------
# This program will read the file and allows a user to find all summer
# Olympics that took place on a specified continent and write the
# results to a file.  

# The program will:
# Ask the user to enter the name of the data file.
# Read the data from the file into three lists - one for the years,
# one for the city and country, and one for the continent.
# Ask the user to enter the continent they are interested in.
# Write to an output file all of the Olympics that took place on the given
# continent.


# Use exception handleing for finding a data file
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        # Begin exception handling
        try:
            # Try to open the file using the name given
            olympicFile = open(fname, 'r')
            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("Invalid filename, please try again ... ")
    return olympicFile


# this function will use the information of a file and use it as data input for
# this program
# the data in this program are split between 3 lists
def getData():
    olympicFile = openFile()

    # Initialized lists
    yearList = []
    cityCountryList = []
    continentList = []

    # for loop reads each line in file
    for line in olympicFile:
        line = line.strip()
        
        # each line in file gets split at the ";" and assigned to variables
        year, cityCountry, continent = line.split(';')

        # add item from file to three lists
        yearList.append(year)
        cityCountryList.append(cityCountry)
        continentList.append(continent)
 
    olympicFile.close()

    return yearList, cityCountryList, continentList


# function finds the year, city and country the olympics took place in
# a continent the user specifies
def findContinent(yearList, cityCountryList, continentList, userContinent):
    userYearList = []
    userCityList = []
    

    if userContinent in continentList:
        for i in range(len(continentList)):
            if userContinent == continentList[i]:

                # add years and city/country from user continent to new lists
                userYearList.append(yearList[i])
                userCityList.append(cityCountryList[i])

        # print for troubleshooting
        #print(userYearList)
        #print(userCityList)
        return userYearList, userCityList


# write all olympic events that took place in the continent the user
# selected to a new file
def writeToFile(userYearList, userCityList):
    # create new file 
    outFile = open('newOlympics.txt', 'w')
    
    # initialize counter
    i = 0
    
    while i < len(userYearList):
        # writes the list of years and city/country  that took place at
        # the users continent
        outFile.write(userYearList[i] + ", " + userCityList[i] + "\n")
        i += 1
    outFile.close()
    return


# main function that calles all functions
def main():
    yearList = []
    cityCountryList = []
    continentList = []

    # call function getData and pass it into three list  varibales 
    yearList, cityCountryList, continentList = getData()

    # prompt user for continent
    userContinent = input("Enter the continent you are searching for: ")

    # This line of code serves as an alternative to the try exception handeling
    # I believe this way is easier to understand and code
    # the way it works is the program takes the user's input and see if it
    # matches with any of the items in the continentList, integers included
    while userContinent not in continentList:
        print("Invalid Entry -- please try again ")
        userContinent = input("Enter the continent you are searching for: ")

    # returns values from the findContinent function to two new lists
    userYearList, userCityList = findContinent(yearList, cityCountryList, continentList, userContinent)

    # writes new file using the two new lists
    writeToFile(userYearList, userCityList)

