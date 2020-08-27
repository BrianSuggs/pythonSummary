# Lab on sorting 

def getList(fname):
    infile = open(fname,'r')
    lst = []
    for line in infile:
        lst = lst + [int(line)]
    infile.close()
    return lst


def bubbleSort(theList):
    for n in range(0,len(theList)): 
        temp = 0
        for i in range(1, len(theList)): 
            temp = theList[i]
	    # comparison
            if theList[i] < theList[i-1]:
	        # swap
                theList[i] = theList[i-1]
                theList[i-1] = temp
    return theList


def insertionSort(theList):
    workCompare = 0
    workSwap = 0
    for i in range(1, len(theList)):
        save = theList[i]
        j = i
        while j > 0 and theList[j - 1] > save:
            # comparison
            workCompare += 1
            theList[j] = theList[j - 1]
            j = j - 1
	    # swap
            workSwap += 1
        theList[j] = save
    print("Work done by comparison is ", workCompare)
    print("Work done by swap is ",workSwap)
    return theList


def selectionSort(theList):
    workCompare = 0
    workSwap = 0
    for i in range(0, len(theList)):            
        min = i
        for j in range(i + 1, len(theList)):
            # comparison
            workCompare += 1
            if theList[j] < theList[min]:
                min = j
        # swap
        workSwap += 1
        theList[i], theList[min] = theList[min], theList[i]
    print("Work done by comparison is ", workCompare)
    print("Work done by swap is ",workSwap)
    return theList


def main():
     fname = input("Enter the name of the data file: ")
     theList = getList(fname)
     print("Running Insertion Sort: ")
     insertionList = insertionSort(theList)
     theList = getList(fname)
     print("\nRunning SelectionSort: ")
     selectionList = selectionSort(theList)
     print("End of comparison")
     
