# Program to compute and print a dot plot of two nucleotide sequences

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


# Function to fill the dot plot 
def computeDotPlot(sideStr, topStr, dot_plot):
    # Fill in the code to compute the dot plot
    for i in range(len(sideStr)):
        for j in range(len(topStr)):
            if sideStr[i] == topStr[j]:
                dot_plot[i][j] = '*'
            else:
                dot_plot[i][j] = '-'
    return dot_plot
            
 
# Function to print the dot plot of two sequences
def printDotPlot(sideStr, topStr, dot_plot):
    row = ""
    for ch in topStr:
        row = row + " " + ch + " "
    print(" ", row)
    row = ""
    for i in range(len(dot_plot)):
        row = row + sideStr[i] + " "
        for j in range(len(dot_plot[i])):
            row = row + " " + dot_plot[i][j] + " "
        print(row)
        row = ""
 
# Main function
def main():
    topStr = input("Enter top string: ")
    sideStr = input("Enter side string: ")
    dot_plot = initDotPlot(len(sideStr), len(topStr))
    # Call the computeDotPlot function
    dot_plot = computeDotPlot(sideStr, topStr, dot_plot)
    printDotPlot(sideStr, topStr, dot_plot)
