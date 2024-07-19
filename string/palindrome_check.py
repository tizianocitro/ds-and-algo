# !difficulty: easy

'''
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
A palindrome is defined as a string that's written the same forward and backward.
Note that single-character strings are palindromes.

Input: "abcdcba"
Output: True
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space
def isPalindrome(string):
    length = len(string)
    l = 0
    r = length - 1
    while l <= r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

# solution two with reversed string
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string for the reversedChars array
def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)