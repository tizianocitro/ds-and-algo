# !code: 162, !difficult: medium, !from: https://leetcode.com/problems/find-peak-element/

'''Problem:
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(logn) time.

Constraints:
- 1 <= nums.length <= 1000
- -231 <= nums[i] <= 231 - 1
- nums[i] != nums[i + 1] for all valid i

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
'''

# solution one using binary search
# Complexity:
# O(logn) time -  where n is the length of nums
# O(1) space
class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            # get the middle element and assign the correct values to
            # prev and next, i.e., left and right neighbors
            middle = (left + right) // 2
            prev = nums[middle - 1] if middle - 1 >= 0 else -float('inf')
            next = nums[middle + 1] if middle + 1 < len(nums) else -float('inf')

            # the element is a peak if it's greater than its left and right neighbors
            if prev < nums[middle] > next:
                return middle

            # no need for the '=' in 'if nums[middle] <= next:'
            # because the constraints say: 'nums[i] != nums[i + 1] for all valid i'
            if nums[middle] < next:
                # if the element is less than the right neighbor, then the peak is on the right
                left = middle + 1
            else:
                # if the element is less than the left neighbor, then the peak is on the left
                right = middle - 1

        # no peak found, this could be omitted in case the constraints are guaranteed
        return -1

# solution two using binary search and assuming there will always be a peak
# Complexity:
# O(logn) time -  where n is the length of nums
# O(1) space
class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while right <= right:
            middle = (left + right) // 2

            # if there is a previous element and the current element is less than the next
            if middle < len(nums) - 1 and nums[middle] < nums[middle + 1]:
                left = middle + 1
            # if therer is a next element and the current element is less than the previous
            elif middle > 0 and nums[middle] < nums[middle - 1]:
                right = middle - 1
            else:
                # we found the peak because the current element is greater than its left and right neighbors
                break

        return middle