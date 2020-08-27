# the Sum of Products Algorithm for inequality Circuits

# construct truth table
# construct subexpressions using AND and NOT gates
# combine subexpressions using OR
# Build circuit diagram

# takes 5 logic gates, 2 NOT, 2 AND, and 1 OR
# expression:
# (not A AND not B) OR (A AND B)




# Majority Rules Circuit

# has three inputs
# if there is more 1s than 0s out of the three, 1 is returned
# if there is more 0s than 1s out of the three, 0 is returned

# takes 11 logic gates
# 3 NOT gates, 4 AND gates, 3 OR gates
# expression:
# (not A AND B AND C) OR (A AND not B AND C) OR (A AND B AND not C) OR (A AND B AND C)


# Majority Rules Function
# use 1s and 0s as true or false in placement of A, B, and C
def majority(A, B, C):
    x1 = int(not A and B and C)
    x2 = int(A and not B and C)
    x3 = int(A and B and not C)
    x4 = int(A and B and C)
    return int(x1 or x2 or x3 or x4)
