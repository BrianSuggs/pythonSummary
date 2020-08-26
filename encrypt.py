# Cryptography program

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

def caesar(plaintext,shift):  
    # Fill in code to compute the ciphertext from the plaintext and the shift

    # For every letter in the plaintext
    for i in range(len(plaintext)):
        letter = plaintext[i]

        # Find the position in the alphabet of the letter
        pos = alphabet.index(letter)

        # Add the shift to the position of the letter
        cipherNum = (pos + shift) % 26

        # Find the letter in the alphabet of the new value
        cipherLetter = alphabet[cipherNum]

        # Add that letter to the ciphertext
        ciphertext = ciphertext + cipherLetter
        
    return ciphertext



def poly(plaintext,keyword):
        ciphertext = ""
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
                cipher_num = (pos + shift) % len(alphabet)

                # Find the letter in the alphabet of the new value
                cipher_letter = alphabet[cipher_num]

                # Add that letter to the ciphertext
                ciphertext = ciphertext + cipher_letter
        return ciphertext



alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
def caesar(plaintext,shift):  
    # initialize ciphertext as blank string
    ciphertext = ""
    # loop through the length of the plaintext
    for i in range(len(plaintext)):         
        # get the ith letter from the plaintext
        letter = plaintext[i] 
        # find the number position of the ith letter
        num_in_alphabet = alphabet.index(letter) 
        # find the number position of the cipher by adding the shift 
        cipher_num = (num_in_alphabet + shift) % len(alphabet) 
        # find the cipher letter for the cipher number you computed
        cipher_letter = alphabet[cipher_num] 
        # add the cipher letter to the ciphertext
        ciphertext = ciphertext + cipher_letter 
 
    # return the computed ciphertext
    return ciphertext
