# !code: 3, !difficulty: medium, !from: https://leetcode.com/problems/longest-substring-without-repeating-characters, https://neetcode.io/problems/longest-substring-without-duplicates

'''Problem:
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
- s consists of English letters, digits, symbols and spaces.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# solution one using sliding window
# Complexity:
# O(n) time - where n is the length of the input string because each character is visited at most twice:
# - when the end pointer expands the window
# - when the start pointer shrinks the window
# so it would be O(2n) which simplifies to O(n)
# O(m) space - where m is the length of the longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keeps track of the characters in the current window
        chars = set()
        longest = 0

        start = 0
        for end in range(len(s)):
            # remove all characters from the set until the
            # current character is no longer in the set
            # and shrink the window at the same time
            while s[end] in chars:
                chars.remove(s[start])
                start += 1

            # add the current character to the set of
            # characters in the current window
            chars.add(s[end])

            # update the longest substring length
            # this can be done both using the length of the set
            # longest = max(longest, len(chars))
            # or using the start and end pointers of the window:
            longest = max(longest, end - start + 1)

        return longest