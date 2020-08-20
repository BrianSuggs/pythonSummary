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
