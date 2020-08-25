# Special things you can do with strings

a = 'Hi! How are you?'
b = "    Hello World!    "
c = 'WE ARE HIRING LOL'
d = "You are hired!"

# get the length of a string
print(len(a))


# removes any whitespace from the beginning or the end
print(b.strip())


# returns the string in lower case
print(c.lower())


# returns the string in upper case
print(d.upper())


# replaces a string with another string
print(b.replace("H", "J"))
print(b.replace(" ", "*"))


# splits the string into substrings if it finds instances of the separator
print(a.split('!'))


# format() method can insert numbers into string
age = 24
txt = "My name is Brian, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# \n is newline (enter key)
# \t is tab     (indent key)


#################################################################################################################################################

# STRING FORMATTING
# The format() method allows you to format selected parts of a string.
# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Format the price to be displayed as a number with two decimals
txt = "The price is {:.2f} dollars"

# Multiple Values
# If you want to use more values, just add more values to the format() method
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, 
# but then you must use names when you pass the parameter values txt.format(carname = "Ford")


"""

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

"""

