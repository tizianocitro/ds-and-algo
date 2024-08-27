# !difficulty: easy

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
'''

# solution one with one loop
# Complexity:
# O(n) time - where n is the length of the input strings
# O(1) space - because the size of the hash map is proportional to the number of unique characters in the strings.
# In the worst case, all characters in the strings are unique, so the size of the hash map would be 26 (the number of letters in the alphabet).
class Solution:
    def isAnagram(self, s, t):
        length = len(s)
        if length != len(t):
            return False

        frequencies = {}
        for i in range(length):
            sChar = s[i]
            frequencies[sChar] = frequencies.get(sChar, 0) + 1
            tChar = t[i]
            frequencies[tChar] = frequencies.get(tChar, 0) - 1
        
        for v in frequencies.values():
            if v != 0:
                return False

        return True

# solution two with multiple loops
# Complexity:
# O(n) time - where n is the length of the input strings
# O(1) space - because the size of the hash map is proportional to the number of unique characters in the strings.
# In the worst case, all characters in the strings are unique, so the size of the hash map would be 26 (the number of letters in the alphabet).
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        frequencies = {}
        for c in s:
            frequencies[c] = frequencies.get(c, 0) + 1

        for c in t:
            if c not in frequencies or frequencies[c] == 0:
                return False
            frequencies[c] -= 1
        
        for v in frequencies.values():
            if v != 0:
                return False

        return True