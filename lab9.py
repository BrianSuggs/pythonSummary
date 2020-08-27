# Lab 9 Part 1-3

# Given: A list of processes with execution times
# Find: A schedule of the processes using time slices

import queue
import random

# Function to get the time slice value and the processes from the file into the queue
# Queue will contain a string with process ID and exec time separated by a comma


def getProcs():
    fname = input("Enter the name of the data file: ")
    infile = open(fname, 'r')
    tslice = []
    cpuQ = []
# Loop through the file inserting processes into the list
    for line in infile:
        line = line.strip()
        proc, eTime = line.split(',')
        tslice = tslice + [proc]
        cpuQ = cpuQ + [int(eTime)]
    infile.close()
    return tslice, cpuQ


# Function to print the contents of the queue

def printQueue(tslice, cpuQ):
    print("The time slice is ",tslice, " \n The contents of the queue are: ")
    for i in range(cpuQ.qsize()):
        proc = cpuQ.get()
        cpuQ.put(proc)
        print(proc)


# Function to execute the processes in the queue
def scheduleProcs(procList, execList):
    for i in range(len(procList)):
        position = findShortestProcess(execList)
        
        proc = procList[position]
        exec1 = execList[position]
        
        procList.pop(position)
        execList.pop(position)

        print ('Running proccess ', proc)
        print ('Takes this many ', exec1)
        
    return

def findShortestProcess(execList):

    min = 0
    for i in range(len(execList)):
        for j in range(i + 1, len(execList)):
            if execList[j] < execList[min]:
                min = j

    return min


# Main function
# use file proc.txt
def main():

    # Get the processes from the data file
    procList, execList = getProcs()
    print (procList, execList)

    pos = findShortestProcess(execList)
    print (procList[pos])

    scheduleProcs(procList, execList)
