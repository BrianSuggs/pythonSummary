# Lab 8 Part 2 Digital Forensics Algorithms
# 16 bits and rotate right

# Given: String consisting of upper-case letters
# Compute: 8-bit checksum of the string

# Function to convert a binary number (input as a string)
# into a decimal number
def bin_to_decimal(binary):
    # Initialize accumulator
    decimal = 0
    # Loop for the length of the string
    for i in range(len(binary)):
        # Compute the power of 2 for the position in the binary number
        power = len(binary) - i - 1
        # Add the power of 2 to the decimal if there is a 1 in the position
        if binary[i] == '1':
            decimal = decimal + 2**power
    return decimal

 

# Function to look up the ASCII representation of a capital letter
# Note: This function only considers capital letters and a space character
def ascii_lookup(ch):
    if ch == 'A':
        return "01000001"
    elif ch == 'B':
        return "01000010"
    elif ch == 'C':
        return "01000011"
    elif ch == 'D':
        return "01000100"
    elif ch == 'E':
        return "01000101"
    elif ch == 'F':
        return "01000110"
    elif ch == 'G':
        return "01000111"
    elif ch == 'H':
        return "01001000"
    elif ch == 'I':
        return "01001001"
    elif ch == 'J':
        return "01001010"
    elif ch == 'K':
        return "01001011"
    elif ch == 'L':
        return "01001100"
    elif ch == 'M':
        return "01001101"
    elif ch == 'N':
        return "01001110"
    elif ch == 'O':
        return "01001111"
    elif ch == 'P':
        return "01010000"
    elif ch == 'Q':
        return "01010001"
    elif ch == 'R':
        return "01010010"
    elif ch == 'S':
        return "01010011"
    elif ch == 'T':
        return "01010100"
    elif ch == 'U':
        return "01010101"
    elif ch == 'V':
        return "01010110"
    elif ch == 'W':
        return "01010111"
    elif ch == 'X':
        return "01011000"
    elif ch == 'Y':
        return "01011001"
    elif ch == 'Z':
        return "01011010"
    elif ch == ' ':
        return "00100000"

# Function to compute the 8-bit checksum of a string
def checksum(inString):
    # Initialize accumulator
    chksm = 0
    i = 0
    # For each character in the string
    while i < len(inString)-1:
        # Look up the ASCII value
        ch = inString[i]
        
        print("ch: ", ch)
        if i+1 < len(inString):
            ascii = ascii_lookup(inString[i]) + ascii_lookup(inString[i+1])
        else:
            ascii = ascii_lookup(inString[i]) + ascii_lookup(' ')
        # rotate right
        #ascii = rotateRight(ascii)
        #print(ascii)
        print("ascii: ", ascii)
        # Convert the binary to decimal
        dec = bin_to_decimal(ascii)
        print("decimal: ", dec)
        # Add the decimal to the checksum accumulator
        chksm = chksm + dec
        print("chksm: ",chksm)
        i = i +1
    # Make sure the checksum fits into 16 bits 
    chksm = chksm % 2**16
    return chksm

def rotateRight(inString):
    # takes last character and brings it to the front
    inString = inString[len(inString)-1] + inString
    # new string cuts off last character
    inString = inString[:len(inString)-1]
    return inString
