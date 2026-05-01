# !code: 18, !difficulty: medium, !from: https://leetcode.com/problems/4sum, https://neetcode.io/problems/4sum

'''Problem:
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n
- a, b, c, and d are distinct
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Constraints:
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

# solution one using k pointers (k = 4)
# Complexity:
# O(n^3) time - where n is the length of the input array
# O(n) space - for sorting or O(m) where m is the number of quadruplets found
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()

        n = len(nums)
        quadruplets = []
        for i in range(n):
            # do not start the search from duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                # do not start the search from duplicates, we do j > i + 1
                # because j starts from i + 1, if we do j > 0/i it would skip the first valid j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                self.findQuadruplet(nums, quadruplets, target, i, j)

        return quadruplets

    def findQuadruplet(self, nums, quadruplets, target, i, j):
        left = j + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[j] + nums[left] + nums[right]
            if total == target:
                quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1