# Brian Suggs
# 4/16/18
# CSC 110 Assignment 10-1 -----------------------------------------------
# This program will computes the score for each alignment using the
# match = 1, mismatch = -1, gap = 0 scoring system
# The program should also find the optimal alignment


# Function to create a list of all ways one gap can be inserted into
# a string.  The input is a string, the output is a list of strings
# with a gap inserted into all positions of the input string
def insertOneGap(strng):
    alignments = []
    global gap_work
    for i in range(len(strng)):
        gap_work += 1
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
def printResults(st, alignments, highScore, scoreList):
    global gap_work
    global compare_work
    
    print("There are ", len(alignments), " alignments")
    print('The following alignments are optimal: ')
    
    for j in range(len(alignments)):
        if scoreList[j] == highScore:
            
            print(st)
            print(alignments[j])
            print('score: ', highScore)
            print(" ")

    print('Amount of work done (gaps): ', gap_work)
    print('Amount of work done (comparisons): ', compare_work)


# Calculate score, gaps, and comparisons
def alignScore(st, alignments):
    global compare_work
    highScore = -100
    scoreList = []
    
    for k in range(len(alignments)):
        match = 0
        mismatch = 0
        str2 = alignments[k]
        for j in range(len(st)):
            compare_work += 1
            if st[j] == str2[j]:
                match += 1

            # find mismatch, excluding gaps
            if st[j] != str2[j] and st[j] != '-' and str2[j] != '-':
                mismatch += 1

        # get highest score which will be the optimal alignment
        score = match - mismatch
        scoreList.append(score)
        if score > highScore:
            highScore = score

    return highScore, scoreList 


# Main function
def main():
    global gap_work
    global compare_work
    
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

    gap_work = 0
    compare_work = 0

    alignments = insertAllGaps(shortStr, len(longStr)-len(shortStr))
    highScore, scoreList = alignScore(longStr, alignments)
    printResults(longStr, alignments, highScore, scoreList)
    
