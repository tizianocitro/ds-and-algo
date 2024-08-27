# !difficulty: easy

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: sentence = "A man, a plan, a canal, Panama!"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

# solution one with better space complexity
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            while left < right and not s[left].isalnum():
                left+=1
            while right > left and not s[right].isalnum():
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# solution two
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string because of the chars array
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]
        left = 0
        right = len(chars) - 1
        while left <= right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        return True
