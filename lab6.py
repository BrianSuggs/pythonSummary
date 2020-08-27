# Lab 6 Binary Search
# Given: A list of names, a list of phone numbers and a phone number to search for

# Function to read the names and phones into lists
def getLists():
    fname = input("Enter name of data file: ")
    infile = open(fname,'r')
    line = infile.readline()

    names = []
    numbers = []

    while line != "":
        line = line.strip()
        name, number = line.split(',')
        names = names + [name]
        numbers = numbers + [number]
        line = infile.readline()

    infile.close()
    return names, numbers

# Function to find the name and return the associated phone number
def binarySearch(names, phones, name):
    # left side of list    
    left = 0	
    # right side of the list				
    right = len(names) - 1		
    found = 0
    while right >= left and found == 0:
	   # find the middle of the list
        m = (left + right) // 2	

        # Fill in the code that examines the middle
        # number and decides what to do next
        if names[m] == name:
            found = 1
        elif name > names[m]:
            left = m + 1
        else:
            right = m -1
	   # Recall that you are going to compare m to 
	   # the number you are searching for and decide how
	   # to search the part of the list where the name
	   # should be.  

	   # Hint:  Use left and right to specify the portion
	   # of the list to search next

    if found == 0:
        return ""

    else:
        return phones[m]
    
    
# Main Function
# use file names_phone.txt
def main():
    # Get the lists
    names, phones = getLists()
    # Get the name to search for
    theName = input("Enter the name to search for: ")

    # Find the phone number for the given name
    phoneNum = binarySearch(names, phones, theName)
    if phoneNum == "":
        print("Name not found")
    else:
        print("The phone number for ", theName, " is ", phoneNum)

        
