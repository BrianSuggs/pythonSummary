# Brian Suggs
# 4/9/18
# CSC 110 Assignment 9-1 -----------------------------------------------
# This program will run a scheduling algorithm that allows processes that
# have more than 50% of their execution time left to compute to have two
# time slices, while processes that have 50% or less of their execution
# time left will have one time slice


# Given: A list of processes with execution times
# Find: A schedule of the processes using time slices
 
import queue
import random
 
# Function to open the file using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename, please try again ... ")
    return inFile
 
# Function to get the time slice value and the processes from the file into the queue
# Queue will contain a string with process ID and exec time separated by a comma
 
def getProcs(cpuQ):
    infile = openFile()
    
    # Get the first line in the file containing the time slice value
    line = infile.readline()
    
    # Strip the \n from the line and convert to an integer
    tslice = int(line.strip())
    #print('tslic is: ', tslice)
    
    # Loop through the file inserting processes into the queue
    for line in infile:                             
        proc = line.strip()
        pname,exectime = line.split(',')
        proc = proc + ',' + exectime 
        cpuQ.put(proc)

    infile.close()
    return tslice, cpuQ

 
# Function to print the contents of the queue
def printQueue(tslice, cpuQ):
    for i in range(cpuQ.qsize()):
        proc = cpuQ.get()
        cpuQ.put(proc)
 
 
# Function to execute the processes in the queue
def scheduleProcs(tslice, cpuQ):
    # While the queue is not empty
    while (cpuQ.empty() != True):
        
        # Get next process from queue
        proc = cpuQ.get()
        
        # Separate the process ID and the execution time from the process info
        PID, exectime, intime = proc.split(",")
        
        
        # Convert exectime to an integer
        exectime = int(exectime)
        intime = int(intime)
        
        print("Getting next process - Process ", PID," has ", exectime,
              " instructions out of ", intime, " to execute")
        
        # Initialize the timer
        timer = 0

        # initilize slice
        tslice = 3
        
        # While proc still has time in slice and still has code to execute
        while (timer < tslice) and (exectime > 0):

            # condition for 2 time slices
            if exectime > (round(intime / 2)) and tslice == 3:
                tslice = 6 

            if 3 >= (round(intime / 2)) and tslice == 6:
                tslice = 3
            
            # In a real computer, the OS would take an instruction from process out of memory and execute it
            # Execute an instruction of process
            exectime = exectime - 1
            
            # Count one tick of the timer
            timer = timer + 1                       
            print("Executing instruction ", exectime," of process ", PID,".  Timer = ", timer)   
            
        # If proc still has instructions to execute put it back in the queue
        if (exectime > 0):
            
            # Create string with new exec time and process ID
            proc = PID + "," + str(exectime) + ',' + str(intime)
            
            # Put the process back in the queue
            cpuQ.put(proc)
            
            print("Put process ", PID," back in queue with ", exectime," instructions left to execute")
        else:
            print("*** Process ", PID, " Complete ***")
    return
 
 
# Main function
 
def main():
    # Create the scheduling queue
    cpuQ = queue.Queue()
 
    # Get the processes from the data file
    tslice, cpuQ = getProcs(cpuQ)
 
    # Print the queue
    printQueue(tslice, cpuQ)
 
    # Schedule the processes
    scheduleProcs(tslice, cpuQ)
