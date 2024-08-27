# !difficulty: easy

'''
Write a function that takes in a non-empty list of non-empty strings
and returns a list of characters that are common to all strings in the list, ignoring multiplicity.
Note that the strings are not guaranteed to only contain alphanumeric characters.
The list you return can be in any order.

Input: ["abc", "bcd", "cbaccd"]
Output: ["b", "c"] // The characters could be returned in any other order
'''

# solution one
# Complexity:
# O(nm) time - where n is the number of strings and m is the length of the longest string
# O(c) space - where c is the number of common characters among all strings
def commonCharacters(strings):
    commons = set([])
    current = set(strings[0]) # Reduce iterations
    for c in current:
        keep = True
        for i in range(1, len(strings)):
            if c not in strings[i]:
                keep = False
                break
        if keep:
            commons.add(c)
    return commons
