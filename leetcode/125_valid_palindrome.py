# !code: 125, !difficulty: easy, !from: https://leetcode.com/problems/valid-palindrome/

'''Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

# solution one using two pointers
# Complexity:
# O(n) time - where n is the length of the string
# O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        # if the string is empty or has only one character
        # it will always be a palindrome
        if n < 2:
            return True

        left, right = 0, n - 1

        # we do not cre to check for when left == right because
        # whatever it is the character in the middle of the string
        # it will always be equal to itself, so we can ignore it
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# solution two using two pointers but with ifs instead of whiles
# Complexity:
# O(n) time - where n is the length of the string
# O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True