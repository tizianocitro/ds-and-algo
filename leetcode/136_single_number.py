# !code: 139, !difficulty: easy, !from: https://leetcode.com/problems/single-number/

'''Problem:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
- 1 <= nums.length <= 3 * 104
- -3 * 104 <= nums[i] <= 3 * 104
- Each element in the array appears twice except for one element which appears only once

Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
'''

# solution one using bitwise xor
# Complexity:
# O(n) time - where n is the length of the input list
# O(1) space
class Solution:
    def singleNumber(self, nums) -> int:
        # we start at 0 because 0 xor num = num, this is because
        # if we take xor of zero and some bit, it will return that bit
        non_duplicated_num = 0
        for num in nums:
            # duplicated num will cancell themselves when xor is applied
            # because if we take xor of two same bits, it will return 0
            non_duplicated_num ^= num
        return non_duplicated_num
