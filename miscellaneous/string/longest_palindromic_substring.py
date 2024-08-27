# !difficulty: medium

'''
Write a function that, given a string, returns its longest palindromic substring.
A palindrome is defined as a string that's written the same forward and backward.
Note that single-character strings are palindromes.
You can assume that there will only be one longest palindromic substring.

Input: "abaxyzzyxf"
Output: "xyzzyx"
'''

# Complexity:
# O(n^2) time - where n is the length of the input string
# O(n) space - where n is the length of the input string,
# because we are storing the longest palindrome substringa and in the worst case it will be the same length as the input string

# solution one
# This is identical to the solution two, but it uses the right element in the longest array to signal the end of the substring.
def longestPalindromicSubstring(string):
    longest = [0, 1]
    for i in range(1, len(string)):
        odd = longestPalindromicSubstringFromTo(string, i - 1, i + 1)
        # even = longestPalindromicSubstringFromTo(string, i, i + 1) // this is the same
        even = longestPalindromicSubstringFromTo(string, i - 1, i)
        currentLongest = max(odd, even, key=lambda x: x[1] - x[0])
        longest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    # Here we use longest[1] and not longest[1] + 1,
    # because the right element in longest points to the first element not in the substring.
    return string[longest[0] : longest[1]]

def longestPalindromicSubstringFromTo(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    # Here we return right and not right - 1, because the right element is not included in the substring.
    return [left + 1, right]

# solution two
def longestPalindromicSubstring(string):
    longest = [0, 0]
    for i in range(len(string)):
        odd = longestPalindromicSubstringFromTo(string, i - 1, i + 1)
        # even = longestPalindromicSubstringFromTo(string, i, i + 1) // this is the same
        even = longestPalindromicSubstringFromTo(string, i - 1, i)
        currentLongest = max(odd, even, key=lambda x: x[1] - x[0])
        longest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[longest[0] : longest[1] + 1]

def longestPalindromicSubstringFromTo(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    return [left + 1, right - 1]
