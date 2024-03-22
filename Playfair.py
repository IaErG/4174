# Simple method to read in text from a file and return it as a single string with no spaces
def readFile(file):
    with open(file, "r") as f:
        text = ''.join(line.replace(' ', '') for line in f)

    return text

# Method that takes in a secret key and the english alphabet, returns a 5x5 key matrix for playfair cipher
def genSecretKeyMatrix(key, alphabet):
    # 1-D Array to hold the key split into letters along with the rest of the alphabet 
    keyMatrix = []

    # Replace instances of 'J' with 'I' to conform to the matrix
    key = key.replace("J", "I")

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


# Method that takes in a string and splits it into pairs of letters
def splitPlainText(plaintext):
    # Remove the spaces amd punctuation from the plaintext string 
    plaintext = plaintext.replace(",", "").replace(".", "").replace("\n", "").replace(" ", "")

    # Initialize variables to use for processing
    length = len(plaintext)
    textPairs = ""
    i = 0

    # While loop to run through the characters in the plaintext
    while i < length:

        # If we're at the end of the string then it contains an odd amount of characters
        if i == length-1:
            # Padd the ending with a 'Z' to make the length even and exit the loop
            textPairs += plaintext[i] + "Z"
            break

        # If two characters next to each other are the same
        if plaintext[i] == plaintext[i+1]:
            # Add the first one appended with the filler character 'X'
            textPairs += plaintext[i] + "X"
            # Increment the counter 'i' by 1 to ensure the second repeated character is hit next loop
            i += 1

        # If two characters next to each other are not the same
        else:
            # Add the 2 characters together as a pair to the array
            textPairs += plaintext[i] + plaintext[i+1]
            # Increment the counter to hit the next pair of characters
            i += 2

    # Return the array filled with pairs of characters from the plaintext string
    return textPairs


# Helper method to find the position of a character in a 2D array
def findPos(char, matrix):
    if char == 'J':
        char = "I"
    for i, row in enumerate(matrix):
        if char in row:
            # When the character is found return the row and column number of the character
            return (i, row.index(char))


# Method that takes in a plaintext string and a key matrix and returns the encrypted plaintext
def plaintextEncrypt(plaintext, keyMatrix):
    # Split the plaintext into a of pairs of characters following the playfair cipher rules
    plainTextPairs = splitPlainText(plaintext)
    encryptedString = ""

    # For loop to cycle thorugh the plaintext in loops of 2
    for i in range(0, len(plainTextPairs), 2):
        # Get a pair of characters and the positions of them in the key matrix
        pair = plainTextPairs[i: i+2]
        char1Pos = findPos(pair[0], keyMatrix)
        char2Pos = findPos(pair[1], keyMatrix)

        # If the 2 characters share the same row
        if char1Pos[0] == char2Pos[0]:
            # Swap the characters with the characters to their left in the matrix and add to the encryptedString
            encryptedString += keyMatrix[char1Pos[0]][(char1Pos[1]+1) % 5]
            encryptedString += keyMatrix[char2Pos[0]][(char2Pos[1]+1) % 5] + " "
        
        # If the 2 characters share the same column
        elif char1Pos[1] == char2Pos[1]:
            # Swap the characters with the characters above them in the matrix and add to the encryptedString
            encryptedString += keyMatrix[(char1Pos[0]+1) % 5][char1Pos[1]]
            encryptedString += keyMatrix[(char2Pos[0]+1) % 5][char2Pos[1]] + " "
        
        # Otherwise if they aren't in the same column or the same row
        else:
            # Swap the characters with the character in the other ends of the rectangle
            encryptedString += keyMatrix[char1Pos[0]][char2Pos[1]]
            encryptedString += keyMatrix[char2Pos[0]][char1Pos[1]] + " "

    # Return the encryptedString as a string of character pairs with spaces
    return encryptedString


# Method to decrypt a a ciphertext string into its plaintext given the string and they keymatrix used
def decryptCipherText(ciphertext, keyMatrix):
    # Condense the ciphertext by removing the spaces
    ciphertext = ciphertext.replace(" ", "")
    plaintext = ""

    # For loop to cycle thorugh the ciphertext in loops of 2
    for i in range(0, len(ciphertext), 2):
        # Get a pair of characters and the positions of them in the key matrix
        pair = ciphertext[i: i+2]
        char1Pos = findPos(pair[0], keyMatrix)
        char2Pos = findPos(pair[1], keyMatrix)

        # If the 2 characters share the same row
        if char1Pos[0] == char2Pos[0]:
            # Swap the characters with the characters to their left in the matrix and add to the plaintext string
            plaintext += matrix[char1Pos[0]][(char1Pos[1]-1) % 5]
            plaintext += matrix[char2Pos[0]][(char2Pos[1]-1) % 5]
        
        # If the 2 characters share the same column
        elif char1Pos[1] == char2Pos[1]:
            # Swap the characters with the characters above them in the matrix and add to the plaintext string
            plaintext += matrix[(char1Pos[0]-1) % 5][char1Pos[1]]
            plaintext += matrix[(char2Pos[0]-1) % 5][char2Pos[1]]
        
        # Otherwise if they aren't in the same column or the same row
        else:
            # Swap the characters with the character in the other ends of the rectangle
            plaintext += matrix[char1Pos[0]][char2Pos[1]]
            plaintext += matrix[char2Pos[0]][char1Pos[1]] 

    # Return the plaintext as a single string with no spaces
    return plaintext

# Constant variables to use for the cipher processing
filePath = "./IN.TXT"
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
secretKey = "RAYQUAZA"

# Generate the key matrix and get the plaintext from the given file
matrix = genSecretKeyMatrix(secretKey, alphabet)
plaintext = readFile(filePath)

# Generate the ciphertext given a plaintext and key matrix
ciphertext = plaintextEncrypt(plaintext, matrix)
print("Ciphertext:\n" + ciphertext + "\n") 

# Generate the plaintext given a ciphertext and key matrix
unencrypted = decryptCipherText(ciphertext, matrix)
print("Plaintext:\n" + unencrypted)