# Lab 8 Part 5 Digital Forensics Algorithms

# Program to compute an MD5 digital signature of the contents of a file

# Import hashlib, which contains several digital signature functions
import hashlib

# Function to get the name of the file to be hashed
def getHashFile():  
    fname = input("Enter name of file to be hashed: ")

    # Open the file to be hashed - use the utf-8 encoding because the hash function
    # assumes that the file it is hasing is encoded
    hashfile = open(fname,"r",1,'utf-8')
    
    return hashfile


# Function to compute the MD5 digital signature
def computeMD5(hashfile):
    
    # Create an object that will compute the MD5
    dig_sig = hashlib.md5()
    
    # Read the data file into a string
    data = hashfile.read()

    # Compute the digital signature using the update function
    # Because the data is encoded, we make sure to use the same encoding that
    # was used when we opened the file
    dig_sig.update(data.encode(hashfile.encoding))

    # Compute the hex digest - the hexidecimal representation of the digital signature
    # and return it
    return dig_sig.hexdigest()


# Main Function
def main():
    # Get the file to be hashed
    hashfile = getHashFile()

    # Create the MD5 signagure
    MD5_sig = computeMD5(hashfile)

    # Print the result
    print("MD5 Digital Signature is: ", MD5_sig)
