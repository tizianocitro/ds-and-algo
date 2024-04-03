# !difficulty: easy

'''
You're given a string of available characters and a string representing a document that you need to generate.
Write a function that determines if you can generate the document using the available characters.
If you can generate the document, your function should return true; otherwise, false.

You're only able to generate the document if the frequency of unique characters
in the characters string is greater than or equal to the frequency of unique characters in the document string.
For example, if you're given characters = "abcabc" and document = "aabbccc" you cannot generate the document because you're missing one "c".
The document that you need to create may contain any characters, including special characters, capital letters, numbers, and spaces.

Note: you can always generate the empty string.

Input:
characters = "&*&you^a%^&8766 _=-09docanCMakemthisdocument"
document = "Can you make this document"
Output: true
'''

# solution one
# Complexity:
# O(n + m) time - where n is the number of characters and m is the length of the document
# O(c) space - where c is the number of unique characters in the characters string
def generateDocument(characters, document):
    if document == "":
        return True
    if len(document) > len(characters):
        return False

    avChars = dict()
    
    for c in characters:
        avChars[c] = avChars.get(c, 0) + 1
    for c in document:
        if c not in avChars or avChars[c] == 0:
            return False
        avChars[c] -= 1

    return True

# solution two
# Complexity:
# O(n + m) time - where n is the number of characters and m is the length of the document
# O(c + d) space - where c is the number of unique characters in the characters string
# and d is the number of unique characters in the document string
def generateDocument(characters, document):
    if document == "":
        return True
    if len(document) > len(characters):
        return False

    avChars = dict()
    dChars = dict()
    
    for c in characters:
        avChars[c] = avChars.get(c, 0) + 1
    for c in document:
        dChars[c] = dChars.get(c, 0) + 1

    for k, v in dChars.items():
        avCount = avChars.get(k, 0)
        if avCount < v:
            return False

    return True

# solution three which reduces space complexity but increases time complexity
# Complexity:
# O(m * (n + m)) time - where n is the number of characters and m is the length of the document
# O(1) space
def generateDocument (characters, document):
    for character in document:
        documentFrequency = countCharacterFrequency(character, document)
        charactersFrequency = countCharacterFrequency(character, characters)
        if documentFrequency > charactersFrequency:
            return False
    return True

def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency