# take binary string and convert it to the corresponding integer

# incomplete###########################
def binaryToDeci():
    bin = input('Enter binary number: ')
    i = 0
    decimal = 0
    while i < len(bin):
        if bin[i] == '1':
            decimal = decimal + 2**(len(bin)-i-1)
    print(decimal)
    return decimal


# Function to convert a binary number (input as a string) into a decimal number
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
