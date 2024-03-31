# !difficulty: medium

'''Problem:
Given a string, find the length of the longest substring in it with at most two distinct characters.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space - because k = 2, so at most k + 1 = 3 elements in the dictionary
class Solution:
    def findLength(self, str1, k):
        max_length = 0
        start = 0
        char_frequencies = {}

        for end in range(len(str1)):
            char = str1[end]
            char_frequencies[char] = char_frequencies.get(char, 0) + 1

            while len(char_frequencies) > 2:
                char = str1[start]
                char_frequencies[char] -= 1
                if char_frequencies[char] <= 0:
                    del char_frequencies[char]

                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length