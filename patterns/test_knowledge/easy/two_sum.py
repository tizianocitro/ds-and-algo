# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/two-sum-easy

'''Problem:
Given an array of integers nums and an integer target, return two distinct indices i and j such that the sum of nums[i] and nums[j] is equal to the target.
You can assume that each input will have exactly one solution, and you may not use the same element twice.

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] gives 2 + 4 which equals 6.

Input: nums = [-1, -2, -3, -4, -5], target = -8
Output: [2, 4]
Explanation: nums[2] + nums[4] yields -3 + (-5) which equals -8.

Input: nums = [10, 15, 21, 25, 30], target = 45
Output: [1, 4]
Explanation: nums[1] + nums[4] gives 15 + 30 which equals 45.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input list
# O(n) space - where n is the length of the input list
class Solution:
    def twoSum(self, nums, target):
        complements = {}

        for i, num in enumerate(nums):
            if num in complements:
                return [complements[num], i]
            complements[target - num] = i

        return [-1, -1]

# solution two
# Complexity:
# O(n) time - where n is the length of the input list
# O(n) space - where n is the length of the input list
class Solution:
    def twoSum(self, nums, target):
        nums_ixs = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_ixs:
                return [nums_ixs[complement], i]
            nums_ixs[num] = i

        return [-1, -1]