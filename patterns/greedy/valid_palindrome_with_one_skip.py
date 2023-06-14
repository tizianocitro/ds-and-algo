# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/65704e706d13707a5c68da41

'''Problem:
Given string s, determine whether it's possible to make a given string palindrome by removing at most one character.

A palindrome is a word or phrase that reads the same backward as forward.

The string s consists of lowercase English letters.

Input: "racecar"
Output: true
Explanation: The string is already a palindrome, so no removals are needed.

Input: "abccdba"
Output: true
Explanation: Removing the character 'd' forms the palindrome "abccba".

Input: "abcdef"
Output: false
Explanation: No single character removal will make this string a palindrome.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space
class Solution:
    def isPalindromePossible(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue

            # if it's different, we can skip one character,
            # so we check if the substring s[left+1:right] is a palindrome
            # and if it is, we can skip the left character, otherwise
            # we check if the substring s[left:right-1] is a palindrome, so
            # we can skip the right character, otherwise we return False because
            # we can't skip more than one character, so the string is not a palindrome
            if left < len(s) - 1 and s[left + 1] == s[right]:
                left += 1
            elif right > 0 and s[right - 1] == s[left]:
                right -=1
            else:
                return False
        return True

# solution two
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space
class Solution:
    def isPalindromePossible(self, s: str) -> bool:
        """Check if it's possible to form a palindrome by removing at most one character"""
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # check if either substring (after removing one char) is a palindrome
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        """Helper function to check if a substring is a palindrome"""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True