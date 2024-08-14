# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64fd83859592e24ab8b03ab7

'''Problem:
Given a string, determine the length of the longest palindrome that can be constructed using the characters from the string.
You don't need to return the palindrome itself, just its maximum possible length.

Input: "aabbcc"
Output: 6
Explaination: We can form the palindrome "abccba" using the characters from the string, which has a length of 6.

Input: "bananas"
Output: 5
Explaination: The longest palindrome that can be constructed from the string is "anana", which has a length of 5.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string and the space taken by the hashmap is proportional to the number of unique characters in the string.
# In the worst case, this would be O(26) for the English alphabet, which is a constant space. However, in general terms, if we consider any possible character (not just English alphabet),
# this would be O(k), where k is the number of unique characters in the string. But since k <= n, this can also be considered O(n) in the worst case.
class Solution:
    def longestPalindrome(self, s: str) -> int:      
        odd_found, length = 0, False
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        # for each character in the hashmap, if it appears an even number of times,
        # add its count to the palindrome length. If it appears an odd number of times,
        # add its count minus one to the palindrome length.
        # Also, set a flag indicating that there's a character available for the center of the palindrome. 
        for v in freq.values():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1
                odd_found = True
        # if the center flag (odd_found) is set, add one to the palindrome length.
        return length + 1 if odd_found else length
