# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/636b1d083b22faa3e89b2458

'''Problem:
Given an array of positive numbers and a positive number k,
find the maximum sum of any contiguous subarray of size k.

Input: [2, 1, 5, 1, 3, 2], k = 3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findMaxSumSubArray(self, k, arr):
        maxSum, sum, start = 0, 0, 0
        for end in range(len(arr)):
            sum += arr[end]
            if end >= k - 1:
                maxSum = max(maxSum, sum)
                sum -= arr[start]
                start += 1
        return maxSum
    
