# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/palindromic-substrings-medium

'''Problem:
Given a string, determine the number of palindromic substrings present in it.
A palindromic substring is a sequence of characters that reads the same forwards and backward.
The substring can be of any length, including 1.

Input: "racecar"
Output: 10
Explanation: The palindromic substrings are "r", "a", "c", "e", "c", "a", "r", "cec", "aceca", "racecar".

Input: "noon"
Output 6
Explanation: The palindromic substrings are "n", "o", "o", "n", "oo", "noon".

Input: "apple"
Output: 6
Explanation: The palindromic substrings are "a", "p", "p", "l", "e", "pp".
'''

# solution one
# Complexity:
# O(n^2) time - where n is the length of the input string
# O(1) space
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # count odd length palindromes
            count += self.expandFromCenter(s, i, i)
            # count even length palindromes
            count += self.expandFromCenter(s, i, i + 1)
        return count

    def expandFromCenter(self, s, left, right):
        count = 0
        # check for palindrome while staying within string boundaries
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    # equivalent to the above expandFromCenter() method
    # but I prefer the succinctness of the above
    # def expandFromCenter(self, s, left, right):
    #     count = 0
    #     # check for palindrome while staying within string boundaries
    #     while left >= 0 and right < len(s):
    #         if s[left] == s[right]:
    #             count += 1
    #             left -= 1
    #             right += 1
    #         else:
    #             break
    #     return count