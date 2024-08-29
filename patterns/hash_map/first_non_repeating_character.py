# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64b7b876aab5a6129791011e

'''
Given a string, identify the position of the first character that appears only once in the string.
If no such character exists, return -1.

Input: "apple"
Output: 0
Explaination: The first character 'a' appears only once in the string and is the first character.
'''

# solution one with only character frequencies map
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space - because, in the worst case, every character in the string is unique.
# For a string with only lowercase English letters, the maximum number of unique characters is 26.
# However, if we consider all possible ASCII characters, the number is 128.
# If we consider extended ASCII, it's 256. In any case, this is a constant number.
# Therefore, the space complexity for the hashmap is O(1) because it doesn't grow proportionally with the size of the input string.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrencies = {}
        for c in s:
            occurrencies[c] = occurrencies.get(c, 0) + 1
        for i in range(len(s)):
            if occurrencies[s[i]] == 1:
                return i
        return -1
