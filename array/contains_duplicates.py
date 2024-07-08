# !difficulty: easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# solution one
# Complexity:
# O(n) time - where n is the length of the array
# O(n) space - where n is the length of the array
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dict = { n : n for n in nums }
        return len(num_dict) != len(nums)

# solution two
# Complexity:
# O(n) time - where n is the length of the array
# O(n) space - where n is the length of the array
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

# solution three for better space complexity
# Complexity:
# O(nlogn) time - where n is the length of the array (sorting)
# O(1) space
class Solution:
    def contains_duplicate(self, nums) -> bool:
        nums.sort() # sort the array
        # use a loop to compare each element with its next element
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]: # if any two elements are the same, return true
                return True
        return False # if no duplicates are found, return false