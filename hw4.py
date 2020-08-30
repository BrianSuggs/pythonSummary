# Brian Suggs
# 2/20/18
# CSC 110 Assignment 4-1 -----------------------------------------------
# This program address a real world application in which members of the
# census bureau collects data on the states
# program creats two list that correspond with one another, one being the state
# and another being the population of the state


# Get two lists from the user
def getStates():
    # Ask user how many states will be in the list
    numStates = int(input("How many states are in your list? "))

    # List one contains a list of abbreviated states
    abbrevStates = []

    # List two contains the list of state populations
    statePopulation = []

    # Initialize counter
    i = 0
    while i < numStates:
        states = input("Enter state abbreviation: ")
        population = int(input("Enter state population: "))

        # Add users values into the lists
        abbrevStates.append(states)
        statePopulation.append(population)
        
        i = i + 1
    # List are now created and ready for assignment in main function
    return abbrevStates, statePopulation


# Returns a single value representing the population of the requested state
def searchState(abbrevStates, statePopulation, searchS):
    if searchS in abbrevStates:
        for j in range(len(abbrevStates)):
            if searchS == abbrevStates[j]:
                popOfSearchedState = statePopulation[j]
                return popOfSearchedState

    # Incase the user searches for an unlisted state, these lines are
    # necessary to avoid an error
    else:
        return -1


# Function prints the states whose population is higher than the specified value
def highPopulationStates(abbrevStates, statePopulation, maxPop):
    highPopStates = []
    for j in range(len(statePopulation)):

        # if value from the list of integers is larger than the max amount
        # find the state with the corresponding value and add it to a new list
        if maxPop < statePopulation[j]:
            highPopStates.append(abbrevStates[j])
       
    print("The following states have population greater than ", maxPop)
    if len(highPopStates) > 0:
        for i in highPopStates:
            
            # prints the abbreviated states in list highPopStates with
            # population over maxPop at place i in the list
            print(i)

    # incase there is no states that have population values over maxPop
    # these lines are necessary to avoid an error
    else:
        print("None")


# main function calls all functions
def main():
    
    # Initialize list
    abbrevStates = []
    statePopulation = []

    # List is ready to be passed as arguments to other functions that call it
    abbrevStates, statePopulation = getStates()

    # new line
    print("")

    # call function that searches for an abbreviated state in the first list
    searchS = input("Enter a state to find population of: ")

    # if list contains the state the user is looking for, it will print out
    # its population to the user
    if searchS in abbrevStates:
        population = searchState(abbrevStates, statePopulation, searchS)
        print("The population of ", searchS, " is " + str(population))
        
    # incase the user entered a state that is not on the list, print out
    # a message saying so to avoid an error
    else:
        print("That is not a valid state abbreviation")

    # new line
    print("")

    # prompt user for max population
    maxPop = int(input("Find all states with population higher than: "))

    # call function to find all states that have populations higher than
    # maxPop and prints them
    highPopulationStates(abbrevStates, statePopulation, maxPop)

    
    
#################################################################################################################################################



# Brian Suggs
# 2/20/18
# CSC 110 Assignment 4-2 -----------------------------------------------
# This program will prompt the user for a number (n). The program will then
# find and return the number of the fibonacci sequence at the nth place

def fib(n):
    # initialize List
    sequence = [0,1]
    i = 0

    # specify invalid inputs
    if n < 0:
        return -1
    else:
        while i < (n):
            # nth is the sum of two list items
            # this expresses the formula to the fibonacci's sequence
            nth = sequence[i] + sequence[i + 1]
            sequence.append(nth)
            i = i + 1

        # returns the value of the fibonacci number at the nth place
        # of the sequence
        return sequence[n-1]

def main():
    # test variables
    test1 = fib(4)
    test2 = fib(10)
    test3 = fib(-4)

    # print test runs from main
    print("The 4th Fibonacci number is ", test1)
    print("The 10th Fibonacci number is ", test2)
    print("fib(-4) = ", test3)

    
