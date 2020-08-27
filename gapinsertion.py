# Program to find all possible alignments of a pair of strings when adding
# gaps to the shorter string

# Given:  Two strings of nucleotides
# Find:  All possible alignments when adding gaps to the shorter string


# Function to create a list of all ways one gap can be inserted into
# a string.  The input is a string, the output is a list of strings
# with a gap inserted into all positions of the input string

def insertOneGap(strng):
    alignments = []
    for i in range(len(strng)):
        newStrng = strng[0:i] + '-' + strng[i:len(strng)]
        alignments = alignments + [newStrng]
    alignments = alignments + [strng + '-']
    return alignments
            
# Function to take a set union of a pair of lists
# This is used to eliminate any duplicates in the list when they are combined
def Union(list1, list2):
    for a in list2:
        if a not in list1:
            list1 = list1 + [a]
    return list1


# Function to create all possible alignments of a string with a certain number
# of gaps inserted
def insertAllGaps(strng, gaps):
    # List of alignments starts with the initial string
    alignments = [strng]

    # Loop to insert one gap at a time
    for i in range(gaps):

        # Initialize list of new alignments with i gaps in the string
        newAlignments = []

        # For every string in the list of alignments
        for st in alignments:
            # Insert one gap in each alignment in the list
            al = insertOneGap(st)

            # Add the new alignment to the list of new alignments being created
            newAlignments = Union(newAlignments,al)

        # The alignments list now becomes the new alignments list to now
        # add another gap to each of the alignments in the new list
        alignments = newAlignments
    return alignments


# Function to print all of the alignments 

def printResults(st, alignments):
    print("There are ", len(alignments), " alignments")
    for i in range(len(alignments)):
        print(st)
        print(alignments[i])
        print(" ")
        
# Main function
def main():
    # Get the two strings to align
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")

    # Compute alignments adding gaps to the shorter string
    if len(str1) > len(str2):
        longStr = str1
        shortStr = str2
    else:
        longStr = str2
        shortStr = str1

    alignments = insertAllGaps(shortStr,len(longStr)-len(shortStr))
    printResults(longStr,alignments)
