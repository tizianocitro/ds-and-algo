# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a0a26aef4e913a2e2bf245

'''Problem:
In a non-empty array of integers, every number appears twice except for one, find that single number.

Input: [1, 4, 2, 1, 3, 2, 3]
Output: 4

Input: [7, 9, 7]
Output: 9
'''

# solution one
# Complexity:
# O(n) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    # we can XOR all the numbers in the input;
    # duplicate numbers will zero out each other
    # and we will be left with the single number
    def findSingleNumber(self, arr):
        x = arr[0]
        for i in range(1, len(arr)):
            x ^= arr[i]
        return x

# solution two
# Complexity:
# O(n) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    # we can XOR all the numbers in the input;
    # duplicate numbers will zero out each other
    # and we will be left with the single number
    def findSingleNumber(self, arr):
        num = 0
        for n in arr:
            num ^= n 
        return num