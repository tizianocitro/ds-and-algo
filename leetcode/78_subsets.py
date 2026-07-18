# !code: 78, !difficulty: medium, !from: https://leetcode.com/problems/subsets, https://neetcode.io/problems/subsets

"""Problem
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
"""

# solution one using backtracking
# Complexity:
# O(n * 2^n) time - where n is the number of elements in nums,
# because there are 2^n subsets and we need to copy each subset to the result list
# O(n * 2^n) space - where n is the number of elements in nums
class Solution:
    def subsets(self, nums):
        subsets = []
        self.buildSubsets(nums, 0, [], subsets)
        return subsets

    def buildSubsets(self, nums, i, subset, subsets):
        if i == len(nums):
            # copy takes O(n) time, where n is the number of elements in the current subset
            subsets.append(subset[:])
            return

        subset.append(nums[i])
        self.buildSubsets(nums, i + 1, subset, subsets)
        subset.pop()
        self.buildSubsets(nums, i + 1, subset, subsets)
