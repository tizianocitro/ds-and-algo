# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64fd6a77826e0e8c47b7f345

'''Problem:
Given two strings, one representing a ransom note and the other representing the available letters from a magazine,
determine if it's possible to construct the ransom note using only the letters from the magazine.
Each letter from the magazine can be used only once.

Input: ransomNote = "notes", magazine = "stoned"
Output: true
Explaination: The word "notes" can be fully constructed from "stoned" from its first 5 letters.

Input: ransomNote = "apple", magazine = "pale"
Output: false
Explaination: The word "apple" cannot be constructed from "pale" as we are missing one 'p'.
'''

# solution one
# Complexity:
# O(n + m) time - where n is the length of the magazine and m is the length of the ransom note
# The time complexity is O(n + m) because we iterate through both strings once and we do not know which one is longer.
# O(1) space - because, in the worst case, every character in the magazine is unique.
# For a string with only lowercase English letters, the maximum number of unique characters is 26.
# However, if we consider all possible ASCII characters, the number is 128.
# If we consider extended ASCII, it's 256. In any case, this is a constant number.
# Therefore, the space complexity for the hashmap is O(1) because it doesn't grow proportionally with the size of the input string.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for c in magazine:
            freq[c] = freq.get(c, 0) + 1
        for c in ransomNote:
            if c not in freq or freq[c] < 1:
                return False
            freq[c] -= 1
        return True