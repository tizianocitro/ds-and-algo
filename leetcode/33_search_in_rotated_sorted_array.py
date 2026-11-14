# !code: 33, !difficulty: medium, !from: https://leetcode.com/problems/search-in-rotated-sorted-array/

'''Problem:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
'''

# solution one
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def search(self, nums: int, target: int) -> int:
        peak_index = self.findPeakIndex(nums)
        left_index = self.binarySearch(nums, target, 0, peak_index)
        if left_index != -1:
            return left_index
        return self.binarySearch(nums, target, peak_index + 1, len(nums) - 1)

    def findPeakIndex(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1]:
                return middle
            # if the middle is bigger than the right,
            # then we are ascending side of the array
            if nums[middle] > nums[right]:
                left = middle + 1
            else: # we are in the descending side of the array
                right = middle

        # if we exit the loop, then the peak will be at the left
        # or right index because left == right
        return left

    def binarySearch(self, nums, target, left, right):
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1