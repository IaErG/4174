
# Method that takes in a secret key and the english alphabet, returns a 5x5 key matrix for playfair cipher
def genSecretKeyMatrix(key, alphabet):
    # 1-D Array to hold the key split into letters along with the rest of the alphabet 
    keyMatrix = []

    # Loop through the letters in the key adding them to the matrix if it hasn't beed added yet
    for char in key:
        if char not in keyMatrix:
            keyMatrix.append(char)
    
    # Go through the rest of the alphabet and add each letter to the matrix if they haven't been added already
    for letter in alphabet:
        if letter not in keyMatrix:
            keyMatrix.append(letter)

    # Matrix to hold the final 5x5 secret key matrix
    matrix = []

    # Loop through the 1-D array until it's empty adding sub arrays of length 5 to the matrix
    while keyMatrix != []:
        matrix.append(keyMatrix[:5])
        keyMatrix = keyMatrix[5:]
        
    # Return the 5x5 key matrix
    return matrix

            
def plaintextEncrypt(plaintext, keyMatrix):
    plainTextPairs = splitPlainText(plaintext)


def splitPlainText(plaintext):
    plaintext = removeSpaces(plaintext)
    length = len(plaintext)
    if length % 2 == 0:
        checkDupeLetter(length, plaintext) 

    else:
        checkDupeLetter(length-1, plaintext) 

# Method to remove spaces from a given piece of text
def removeSpaces(text):
    retString = ''
    for i in text:
        if i == ' ':
            continue
        else:
            retString = retString + i

    return retString

def checkDupeLetter(length, text):
    textPairs = []
    for i in range(0, length, 2):
        if text[i] == text[i+1]:
            textPairs.append(text[i] + "Z")
            textPairs.append(text[i+1] )
        else:
            textPairs.append(text[i] + text[i+1])

    print(textPairs)

# def ciphertext():

splitPlainText("COME QUICKLY WE NEED HELP")
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N',
#              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# genSecretKeyMatrix("HELLO", alphabet)