# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638fa28f5844e928cbefff88

''' Problem:
Given two strings containing backspaces (identified by the character #), check if the two strings are equal.

If there are enough # to erase all characters in the string, the final string after processing the backspaces will be equal.

Input: str1 = "xy#z", str2 = "xzz#"
Output: true // After applying backspaces the strings become "xz" and "xz" respectively.

Input: str1 = "xp#", str2 = "xyz##"
Output: true // After applying backspaces the strings become "x" and "x" respectively.
// In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
'''

# solution one
# Complexity:
# O(n + m) time - where n and m are the lengths of the strings
# O(1) space
class Solution:
    def compare(self, str1, str2):
        i, j = len(str1) - 1, len(str2) - 1
        while i >= 0 and j >= 0: # while there are chars in both strings
            # this will iterate all characters in str1 in the worst case
            next_i = self.findNextIndex(str1, i)
            # this will iterate all characters in str2 in the worst case,
            # so the complexity is O(n + m) because we iterate all chars in both strings
            next_j = self.findNextIndex(str2, j)
            if next_i < 0 and next_j < 0:
                return True
            if next_i < 0 or next_j < 0:
                return False
            if str1[next_i] != str2[next_j]:
                return False
            i = next_i - 1
            j = next_j - 1

        return True

    def findNextIndex(self, s, index):
        backspaces = 0
        while index >= 0:
            if s[index] == '#':
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                break
            index -= 1
        return index