# !code: 75, !difficulty: medium, !from: https://leetcode.com/problems/sort-colors/

'''Problem:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]
'''

# solution one with one pass
# Complexity:
# O(n) time - where n is the length of the input list
# O(1) space
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            # put 2s at the end of the list
            if nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1

                # when we swap the current element with the last element,
                # we don't know what the last element is, so we must check it again
                # and for this reason, we do not move i forward
                continue

            # put 0s at the beginning of the list
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            i += 1
