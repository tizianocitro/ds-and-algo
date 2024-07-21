# !difficulty: easy

'''
Write a function that takes in a string of lowercase English-alphabet letters
and returns the index of the string's first non-repeating character.
The first non-repeating character is the first character in a string that occurs only once.
If the input string doesn't have any non-repeating characters, your function should return -1.

Input: string = "abcdcaf"
Output: 1 // The first non-repeating character is "b" and is found at index 1.
'''

# solution one with only character frequencies map
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space - because the input string contains only lowercase English-alphabet letters;
# thus, the map will never have more than 26 character frequencies
def firstNonRepeatingCharacter(string):
    frequencies = dict()
    for c in string:
        frequencies[c] = frequencies.get(c, 0) + 1
    for i in range(len(string)):
        if frequencies[string[i]] == 1:
            return i
    return -1

# solution two with indexes map as well
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space - because the input string contains only lowercase English-alphabet letters;
# thus, the maps will never have more than 26 character frequencies or indexes
def firstNonRepeatingCharacter(string):
    frequencies = dict()
    indexes = dict()
    for i in range(len(string)):
        c = string[i]
        frequencies[c] = frequencies.get(c, 0) + 1
        indexes[c] = indexes.get(c, i)
    for k, v in frequencies.items():
        if v == 1:
            return indexes[k]
    return -1
