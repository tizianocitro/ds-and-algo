# !difficulty: easy

'''
Given an array of strings words and two different strings that already exist in the array word1 and word2,
return the shortest distance between these two words in the list.

Input:
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

Output: 3 // "coding" is the 0th index, "practice" is the 3nd index, so the distance is 3 - 0 = 3
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array words
# O(1) space
class Solution:
    def shortestDistance(self, words, word1, word2):
        pos1, pos2, = -1, -1
        distance = len(words) # Could also use float('inf')
        for i, w in enumerate(words):
            if w == word1:
                pos1 = i
            if w == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                distance = min(distance, abs(pos1 - pos2))
        return distance