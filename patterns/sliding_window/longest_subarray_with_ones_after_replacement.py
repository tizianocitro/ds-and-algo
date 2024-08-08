# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6385d6304a29c96532f7bcb2

'''Problem:
Given an array containing 0s and 1s, if you are allowed to replace no more than k 0s with 1s,
find the length of the longest contiguous subarray having all 1s.

Input: array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k = 2
Output: 6  
Explanation: Replace the 0 at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findLength(self, arr, k):
        max_length, ones = 0, 0
        start = 0

        for end in range(len(arr)):
            if arr[end] == 1:
                ones += 1

            # with while loop it would work the same but it would be less efficient
            # because it would process until the condition becomes less than k, which is not required here
            # while if end - start + 1 - ones > k:
            if end - start + 1 - ones > k:
                if arr[start] == 1:
                    ones -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
