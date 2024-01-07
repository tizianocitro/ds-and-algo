# !difficulty: easy

'''
Given a non-empty string of lowercase letters and a non-negative integer representing a key,
write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.
Note that letters should "wrap" around the alphabet;
in other words, the letter z shifted by one returns the letter a.

Input: "xyz", 2
Output: "zab"
'''

# solution one with array
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string for the cypherChars array
def caesarCipherEncryptor(string, key):
    # Need to fix the key because with high numbers,
    # we could get the same string in output
    # To solve we need to wrap the key around the alphabet,
    # and 26 is the number of letters in the alphabet
    fixedKey = key % 26
    cypherChars = []
    z = ord('z')
    a = ord('a') - 1 # We need the letter before 'a' to wrap around the alphabet
    
    for i in range(len(string)):
        char = ord(string[i])
        shiftedChar = char + fixedKey
        if shiftedChar > z:
            shiftedChar = a + shiftedChar % z
        cypherChars.append(chr(shiftedChar))

    return "".join(cypherChars)


# solution two with f-string
# Complexity:
# O(n^2) time - where n is the length of the input string because of string slicing
# O(n) space - because strings are immutable in python, we need to create a new string for every character we change
def caesarCipherEncryptor(string, key):
    fixedKey = key % 26
    z = ord('z')
    a = ord('a') - 1

    for i in range(len(string)):
        char = ord(string[i])
        shiftedChar = char + fixedKey
        if shiftedChar > z:
            shiftedChar = a + shiftedChar % z
        string = f'{string[:i]}{chr(shiftedChar)}{string[i + 1:]}'

    return string
