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


########################################################################################################################################


# DICTIONAIRES


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


