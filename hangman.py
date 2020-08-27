# Hangman Game

def fillBlanks(word):
    # Create the blank list the length of the word
    i = 0
    blanks = []
    while i < len(word):
        blanks.append("-")
        i = i + 1
    return blanks


def addLetter(letter,word,blanks):
    #Fill in the letter where it fits into the blanks list
    for i in range(len(word)):
        if letter == word[i]:
            blanks[i] = letter
    return blanks

        
def wordGuessed(word, blanks):
    if "-" in blanks:
        return 0
    else:
        return 1


def displayBlanks(blanks):
    print("The word you are guessing looks like this: ")
    print(" ")
    print(' '.join(blanks))
    print(" ")
    return


def main():
    word = input("Player 1 choose a word: ")

    #call the fill blanks function and store the result in a
    #variable (call it whatever you want)

    blanks = fillBlanks(word)

    maxGuesses = int(input("Enter the max number of guesses: "))
    guesses = 0
    found = 0
    
    while found == 0 and guesses < maxGuesses:

        #call the display blanks function with your list of blanks
        displayBlanks(blanks)
        
        letter = input("Enter a letter to guess: ")
        if letter in word:

            #call addLetter function and store the result in
            #your blanks list
            blanks = addLetter(letter,word,blanks)

            #call the wordGuessed function and store the result in
            #the variable found
            found = wordGuessed(word, blanks)

        else:
            guesses= guesses + 1

    if guesses >= maxGuesses:
        print("Too many Guesses. You lose, the word was ", word)

    else:
        print("Nice job! Good Guessing!")
        #Call the display blanks function one more time to show the guessed word
        displayBlanks(blanks)




