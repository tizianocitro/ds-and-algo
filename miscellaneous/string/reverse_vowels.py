# !difficulty: easy

'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Input: s = "hello"
Output: "holle"
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the string
# O(n) space - where n is the length of the string,
# because we are creating the chars array and a new string
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        chars = [c for c in s]
        left = 0
        right = len(chars) - 1
        while left <= right:
            if chars[left].lower() in vowels and chars[right].lower() in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -=1
            if chars[left].lower() not in vowels:
                left += 1
            if chars[right].lower() not in vowels:
                right -= 1
        return ''.join(chars)

# solution two with improved readability
# Complexity:
# O(n) time - where n is the length of the string
# O(n) space - where n is the length of the string,
# because we are creating the chars array and a new string
class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = 'aeiouAEIOU' is the same as the list below
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        chars = list(s)
        left = 0
        right = len(chars) - 1
        while left <= right:
            if chars[left] in vowels and chars[right] in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -=1
            if chars[left] not in vowels:
                left += 1
            if chars[right] not in vowels:
                right -= 1
        return ''.join(chars)