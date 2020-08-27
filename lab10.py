# Lab 10 
# Program to compute and print a dot plot of two nucleotide sequences

# Function to find how many matches there are in two strings of equal length
def matchPct(seq1, seq2):
    if len(seq1) < len(seq2):
        shortest = len(seq1)
    else:
        shortest = len(seq2)

    match = 0
    # include if statement
    for i in range(shortest):
        if seq1[i] == seq2[i]:
            match += 1

    # Fill in code to compute percentage between sequences
    pct = match / shortest
    print(pct)
    return pct


# Function to initialize a dot plot of a certain size
def initDotPlot(rows, cols):
    # Initialize the dot_plot matrix
    empty_dot_plot = []
    # For each row in the matrix
    for i in range(rows):
        # Initialize the row
        row = []
        # For each col in the matrix
        for j in range(cols):
            # Insert a blank in the row
            row.append("-")
        empty_dot_plot.append(row)
    return empty_dot_plot          

            
# Function to compute the dot plot of two sequences using a sliding window of size winsize
def computeDotPlot(str1, str2, winsize, threshold, dot_plot):
    # Loop through all of the rows (characters in the side sequence)
    for i in range(len(str2)):
        
        # Loop through all of the columns (characters in the top sequence)
        for j in range(len(str1)):
            
            # Fill in the code to determine if we should insert
            # a "*" to the position in the dot plot

            # calculate percentage
            pct = matchPct(str1[j:j + winsize], str2[i:i + winsize])

            if (pct >= threshold):
                dot_plot[i][j] = '*'

    return dot_plot


# Function to print the dot plot of two sequences
def printDotPlot(str1, str2, dot_plot):
    row = ""
    for ch in str1:
        row = row + " " + ch + " "
    print(" ", row)
    row = ""
    for i in range(len(dot_plot)):
        row = row + str2[i] + " "
        for j in range(len(dot_plot[i])):
            row = row + " " + dot_plot[i][j] + " "
        print(row)
        row = ""


# Main function
def main():
    str1 = input("Enter top string: ")
    str2 = input("Enter side string: ")
    winsize = int(input("Enter size of window: "))
    threshold = float(input("Enter expected threshold: "))
    empty_dot_plot = initDotPlot(len(str2), len(str1))
    # Call the computeDotPlot function here
    dot_plot = computeDotPlot(str1, str2, winsize, threshold, empty_dot_plot)
    printDotPlot(str1, str2, dot_plot)

    
