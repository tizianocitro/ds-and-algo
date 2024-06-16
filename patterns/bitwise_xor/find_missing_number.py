# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a09d143fbc39976653e236

'''Problem:
Given an array of n-1 integers in the range from 1 to n, find the one number that is missing from the array.

Input: [1, 5, 2, 6, 4]
Output: 3
'''

# solution one
# Complexity:
# O(n) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def findMissingNumber(self, arr):
        n = len(arr) + 1

        # x1 represents XOR of all values from 1 to n
        x1 = 1
        for i in range(2, n + 1):
            x1 = x1 ^ i

        # x2 represents XOR of all values in arr
        x2 = arr[0]
        for i in range(1, n - 1):
            x2 = x2 ^ arr[i]
        
        # missing number is the xor of x1 and x2
        return x1 ^ x2