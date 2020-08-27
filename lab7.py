# Lab 7 Encoding and decoding messages

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

def relPrime (a, m):
    #establishes that everything starts true
    f = True
    
    #lists for both numbers
    aFactors = []
    mFactors = []
    
    #analyze a for factors
    i = 2
    while i <= a:
        c = a % i
        if c == 0:
            aFactors.append(i)
        i = i + 1
    print(aFactors)
    
    #analyze m for factors
    j = 2
    while j <= m:
        c = m % j
        if c == 0:
            mFactors.append(j)
        j = j + 1
    print(mFactors)
    
    #compare to each other
    k  = 0
    l = 0
    for k in range(len(aFactors)):
        for l in range(len(mFactors)):
            if aFactors[k] is mFactors[l]:
                f = False
    return f


def alffine (a, b, m, plaintext):
    ciphertext = ''
    test = relPrime(a, m)
    if test == True:
        for i in range(len(plaintext)):
            letter = plaintext[i]
            pos = alphabet.index(letter)
            shift = (a * pos + b) % m
            cipherNum = int(shift) % m
            cipherLetter = alphabet[cipherNum]
            ciphertext = ciphertext + cipherLetter
    else:
        ciphertext = ''
    return ciphertext


def inverse(a, m):
    found = False
    x = 0
    if (a*x % 26) == 1:
        found = True
    else:
        while found == False:
            x = x + 1
            if (a*x % 26) == 1:
                found = True
    return x


def decode(a, b, m, ciphertext):
    plaintext = ''
    x = inverse(a, m)
    
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        
        pos = alphabet.index(letter)
        
        shift = (x * (pos - b) % m)
        
        plainLetter = alphabet[shift]
        
        plaintext = plaintext + plainLetter
        
    return plaintext


def caesar(ciphertext):  
    # initialize ciphertext as blank string
    plaintext = ""
    shift = 0

    # loop through the length of the plaintext
    while shift < 26:
        plaintext = ''
        
        for i in range(len(ciphertext)):
            # get the ith letter from the plaintext
            letter = ciphertext[i]
            
            # find the number position of the ith letter
            num_in_alphabet = alphabet.index(letter)
            
            # find the number position of the cipher by adding the shift 
            plain_num = (num_in_alphabet + shift) % len(alphabet)
            
            # find the cipher letter for the cipher number you computed
            plain_letter = alphabet[plain_num]
            
            # add the cipher letter to the ciphertext
            plaintext = plaintext + plain_letter
            
        shift += 1
