# !code: 844, !difficulty: easy, !from: https://leetcode.com/problems/backspace-string-compare/

'''Problem:
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters

Follow-Up Questions:
Can you solve it in O(n) time and O(1) space?

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''

# solution one using generator
# Complexity:
# O(n + m) time - where n is the length of s and m is the length of t
# O(1) space
from itertools import zip_longest

class Solution:
    def backspaceCompare(self, s, t):
        # get s and t but with the backspaces removed
        # as well as the characters before them
        cleaned_s = self.cleanBackspaces(s)
        cleaned_t = self.cleanBackspaces(t)
        # check if the cleaned strings are equal using the two generators
        # zip_longest is used to handle the case where the strings are of different lengths
        # until they both have characters, it returns the characters,
        # when one of the strings is exhausted, it returns None for the remaining characters of that string
        return all(ch_s == ch_t for ch_s, ch_t in zip_longest(cleaned_s, cleaned_t))

    def cleanBackspaces(self, s):
        skip = 0
        # iterate over the string in reverse because we want to know how many backspaces
        # we have encountered, so that we can can the count of characters to skip
        for ch in reversed(s):
            # if we encounter a backspace, we increment the count of characters to skip
            # but we do not include the current character in the output
            if ch == '#':
                skip += 1
            # if the character is not a backspace and we have characters to skip, we decrement the count
            # but we do not include the current character in the output
            elif skip > 0:
                skip -= 1
            # if the character is not a backspace and we do not have characters to skip,
            # we include the character in the output
            else:
                yield ch

# solution two using stack
# Complexity:
# O(n + m) time - where n is the length of s and m is the length of t
# O(n + m) space - to store the cleaned strings
class Solution:
    def backspaceCompare(self, s, t):
        # check if the cleaned strings are equal
        return self.build(s) == self.build(t)

    def build(self, s):
        # stack to store the cleaned string where we remove
        # the backspaces and the characters before them
        cleaned_s = []
        for ch in s:
            # if the character is not a backspace, we add it to the stack
            if ch != '#':
                cleaned_s.append(ch)
            # if the character is a backspace, we remove the last character
            # if we have characters in the stack
            elif cleaned_s:
                cleaned_s.pop()

        return ''.join(cleaned_s)