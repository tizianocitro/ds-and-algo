# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638ca0aa5b41522e8a2e3395

''' Problem:
Given an array of numbers sorted in ascending order and a target sum,
find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
If no such pair exists return [-1, -1].

Input: [1, 2, 3, 4, 6], target = 6
Output: [1, 3] (The numbers at index 1 and 3 add up to 6: 2 + 4 = 6)
'''

# solution one using two pointers and binary search
# Complexity:
# O(n) time - where n is the size of the array
# O(1) space
class Solution:
    def search(self, arr, target_sum):
        left = 0
        right = len(arr) - 1
        while left <= right:
            sum = arr[left] + arr[right]
            if sum == target_sum:
                return [left, right]
            if sum < target_sum:
                left += 1
            else:
                right -=1
        return [-1, -1]

# solution two using hash map to store numbers and their indices
# Complexity:
# O(n) time - where n is the size of the array
# O(n) space - where n is the size of the array
class Solution:
    def pair_with_targetsum(self, arr, target_sum):
        nums = {}
        for i, num in enumerate(arr):
            complement = target_sum - num
            if complement in nums:
                return [nums[complement], i]
            else:
                nums[num] = i
        return [-1, -1]