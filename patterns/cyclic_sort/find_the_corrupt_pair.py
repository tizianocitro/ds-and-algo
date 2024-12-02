# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63948b3326086d487e96e4b3

'''Problem:

We are given an unsorted array containing n numbers taken from the range 1 to n.
The array originally contained all the numbers from 1 to n, but due to a data error,
one of the numbers got duplicated which also resulted in one number going missing.
Find both these numbers.

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findNumbers(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                continue
            i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]

        return [-1, -1]