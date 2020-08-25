# FILE HANDLEING

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file

"""

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"""

# In addition you can specify if the file should be handled as binary or text mode

"""

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""


# Syntax
# To open a file for reading it is enough to specify the name of the file
f = open("demofile.txt")

# The code above is the same as
# Because "r" for read, and "t" for text are the default values, you do not need to specify them
f = open("demofile.txt", "rt")


######################################################################################################################################################

# READ FILES

# Open a File on the Server
# Assume we have the following file, located in the same folder as Python
# The open() function returns a file object, which has a read() method for reading the content of the file
f = open("demofile.txt", "r")
print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return
# Return the 5 first characters of the file
f = open("demofile.txt", "r")
print(f.read(5))

# Read Lines
# You can return one line by using the readline() method
# Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line
f = open("demofile.txt", "r")
for x in f:
  print(x)
  
# Close Files
# It is a good practice to always close the file when you are done with it
f = open("demofile.txt", "r")
print(f.readline())
f.close()


######################################################################################################################################################

# Write to an Existing File


















