# DATA STRUCTURES OF PYTHON

'''
1 Objects
2 Class
3 List
4 Array
5 Tuples
6 Dictionaires
7 Stack
8 Queues
9 Linked List
10 Trees
11 Matrix
'''

########################################################################################################################################


# OBJECTS


########################################################################################################################################


# CLASS


########################################################################################################################################


# LIST 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

# access the list items by referring to the index number. Remember to start at 0
print(thislist[0])

# Negative indexing means beginning from the end, -1 refers to the last item
print(thislist[-1])

# Range Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items

#This will return the items from position 2 to 5.
#and note that the item in position 5 is NOT included
print(thislist[2:5])

# prints first 4 items
print(thislist[:4])

# prints from index 2 to end
print(thislist)[2:])

# changing a value
thislist[1] = 'coconut'

# length of list
length = len(thislist)
print(length)

# add items to end of list
thislist.append(pineapple)

# add an item at the specified index
thislist.insert(1, "orange")
print(thislist)

# removes the specified item
thislist.remove("orange")
print(thislist)

# pop() method removes the specified index, (or the last item if index is not specified)
thislist.pop()
print(thislist)

# del keyword removes the specified index. can also delete the list completely
del thislist[0]
print(thislist)

# clear() method empties the list

#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.
# Make a copy of a list with the copy() method
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list()
mylist = list(thislist)
print(mylist)

# Joining two lists by concatenation
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# join two lists are by appending all the items from list2 into list1, one by one
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



########################################################################################################################################


# ARRAY


########################################################################################################################################


# TUPLES
# a collection which is ordered and unchangeable. In Python tuples are written with round brackets
# for the most part, it works like a list minus the methods except len()
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# access tuple items by referring to the index number, inside square brackets. negative indexing is legal
print(thistuple[1])

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# To join two or more tuples you can use the + operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)




########################################################################################################################################


# DICTIONAIRES
# a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Accessing items
x = thisdict["brand"]
y = thisdict["model"]
z = thisdict["year"]
print(z, y, x)

# The get() method will give you the same result
x = thisdict.get("model")

# Changing values
# You can change the value of a specific item by referring to its key name
thisdict["year"] = 2020
print(z, y, x)

# Looping 
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well
# Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])

# You can also use the values() method to return values of a dictionary
for x in thisdict.values():
  print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

# To determine how many items (key-value pairs) a dictionary has, use the len() function
print(len(thisdict))

# Adding items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict["color"] = "red"
print(thisdict)

# Removing items
# The pop() method removes the item with the specified key name
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The clear() method empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


# Copying a dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, 
# and changes made in dict1 will automatically also be made in dict2
# Make a copy of a dictionary with the copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function
mydict = dict(thisdict)
print(mydict)

# NESTED DICTIONARIES
myfamily = {
  "child1" : {
    "name" : "Roy",
    "year" : 2030
  },
  "child2" : {
    "name" : "Issac",
    "year" : 2032
  },
  "child3" : {
    "name" : "Brian the Third",
    "year" : 2034
  }
}

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {
  "name" : "Roy",
  "year" : 2030
}
child2 = {
  "name" : "Issac",
  "year" : 2032
}
child3 = {
  "name" : "Brian",
  "year" : 2034
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# DICT CONSTRUCTOR
# It is also possible to use the dict() constructor to make a new dictionary

# note that keywords are not string literals
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

########################################################################################################################################


# STACK


########################################################################################################################################


# QUEUES


########################################################################################################################################


# LINKED LIST


########################################################################################################################################


# TREES


########################################################################################################################################


# MATRIX


