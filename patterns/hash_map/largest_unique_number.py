# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64fd56f417ec3ee519760638

'''Problem:
Given an array of integers, identify the highest value that appears only once in the array.
If no such number exists, return -1.

Input: [1, 2, 3, 2, 1, 4, 4]
Output: 3
Explaination: The number 3 is the highest value that appears only once in the array.

Input: [9, 9, 8, 8, 7, 7]
Output: -1
Explaination: There is no number in the array that appears only once.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input list
# O(n) space - because, in the worst case, every number in the list is unique
class Solution:
    def largestUniqueNumber(self, a):
        maxUnique = -1
        freq = {}
        for n in a:
            freq[n] = freq.get(n, 0) + 1
        for k, v in freq.items():
            if v == 1:
                maxUnique = max(maxUnique, k)
        return maxUnique