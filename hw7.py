# Brian Suggs
# 3/26/18
# CSC 110 Assignment 7-1 -----------------------------------------------
# This program will encrypt a message using a modified caesar cipher with one
# function and decrypt the cipher text with the other function

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 


# function encrypts plaintext using a modified ceaser cipher
def caesarMinus(plaintext, shift):
    ciphertext = ""
    
    # For every letter in the plaintext
    for i in range(len(plaintext)):
        letter = plaintext[i]

        # Find the position in the alphabet of the letter
        pos = alphabet.index(letter)

        # Add the shift minus the index to the position of the letter
        cipherNum = (pos + shift - i) % 26

        # Find the letter in the alphabet of the new value
        cipherLetter = alphabet[cipherNum]

        # Add that letter to the ciphertext
        ciphertext = ciphertext + cipherLetter
        
    return ciphertext


# function decrypts ciphertext that was encrypted by the modified ceaser cipher
def unCaesarMinus(ciphertext, shift):
    plaintext = ""
    
    # For every letter in the ciphertext
    for i in range(len(ciphertext)):
        letter = ciphertext[i]

        # Find the position in the alphabet of the letter
        pos = alphabet.index(letter)

        # Minus the shift to the position of the letter to undo encryption
        plainNum = (pos - (shift - i)) % 26

        # Find the letter in the alphabet of the new value
        plainLetter = alphabet[plainNum]

        # Add that letter to the plaintext
        plaintext = plaintext + plainLetter
        
    return plaintext



############################################################################################################################################################



# Brian Suggs
# 3/26/18
# CSC 110 Assignment 7-2 -----------------------------------------------
# This program will encrypt a message using the polyalphabetic cypher that
# encrypts with a modified keyword. This keyword it the user's keyword plus
# that same keyword but in reverse
# After the ciphertext is made with this modification in mind, this program will
# also decrypt the ciphertext to its original plaintext


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

# function will encrypt message using the modified version of the
# polyalphabetic cipher

def polyReverse(plaintext,keyword):
        ciphertext = ""
        
        # new keyword is original keyword plus the reverse of said keyword
        j = len(keyword)
        for i in range(len(keyword)):
            j -= 1
            keyword = keyword + keyword[j]

        # For every letter in the alphabet
        for i in range(len(plaintext)):
            
            letter = plaintext[i]
            
            # Find the position in the alphabet of the letter
            pos = alphabet.index(letter)
 
            # Find the position in the keyword with the letter to shift
            shiftIndex = i % len(keyword)
                
            # Find the letter in the keyword to shift
            shiftLetter = keyword[shiftIndex]
                
            # Find the number associated with the letter to be used as the shift
            shift = alphabet.index(shiftLetter)

            # Add the shift to the position of the letter
            cipherNum = (pos + shift) % len(alphabet)

            # Find the letter in the alphabet of the new value
            cipherLetter = alphabet[cipherNum]

            # Add that letter to the ciphertext
            ciphertext = ciphertext + cipherLetter
            
        return ciphertext


# function decrypts ciphertext to find the plaintext
def unPolyReverse(ciphertext, keyword):
    plaintext = ""
        
    # new keyword is original keyword plus the reverse of said keyword
    j = len(keyword)
    for i in range(len(keyword)):
        j -= 1
        keyword = keyword + keyword[j]

    # For every letter in the alphabet
    for i in range(len(ciphertext)):
        
        letter = ciphertext[i]
            
        # Find the position in the alphabet of the letter
        pos = alphabet.index(letter)
 
        # Find the position in the keyword with the letter to shift
        shiftIndex = i % len(keyword)
                
        # Find the letter in the keyword to shift
        shiftLetter = keyword[shiftIndex]
                
        # Find the number associated with the letter to be used as the shift
        shift = alphabet.index(shiftLetter)

        # Add the shift to the position of the letter
        plainNum = (pos - shift) % len(alphabet)

        # Find the letter in the alphabet of the new value
        plainLetter = alphabet[plainNum]

        # Add that letter to the plaintext
        plaintext = plaintext + plainLetter
            
    return plaintext
