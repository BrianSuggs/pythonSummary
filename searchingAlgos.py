# SEARCHING ALGORITHMS IN PYTHON

'''
1 Linear search
2 Binary search
3 
4 
5 
6 
'''

########################################################################################################################################

# SEQUENTIAL SEARCH

# Get the lists
phoneList = []
nameList = []

num = int(input("How many numbers in the list? "))

for i in range(num):
    phone = input("Enter phone number: ")
    name = input("Enter name: ")
    phoneList.append(phone)
    nameList.append(name)

# Get phone number to search for
searchNum = input("Enter phone number to search for: ")

# Search the phone list for the number
found = False
i = 0

while found == False and i < len(phoneList):
    if phoneList[i] == searchNum:
        found = True
    else:
        i = i + 1

# Print name
if not found:
    print("The number is not in the list")
else:
    print("The name is: ", nameList[i])

