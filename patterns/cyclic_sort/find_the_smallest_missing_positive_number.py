# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63948c59c549a12fb2181118

'''Problem:
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Note: Positive numbers start from 1.

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

Input: [33, 37, 5]
Output: 1

Input: [3, 2, 0, 1]
Output: 4
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findNumber(self, nums):
        n = len(nums)
        i = 0
        while i < len(nums):
            num = nums[i]
            if num <= 0 or num > n:
                i += 1
                continue

            j = num - 1
            if num != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                continue

            i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

# solution two with cleaner code
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findNumber(self, nums):
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                continue

            i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1