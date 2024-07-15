# !difficulty: easy

'''
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Input: nums = [1, 2, 3, 1, 1, 3]
Output: 4 // There are 4 good pairs and they're indexes are (0,3), (0,4), (3,4), (2,5).
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array nums
# O(n) space - where n is the length of the input array nums
class Solution:
    def numGoodPairs(self, nums):
        pairCount = 0
        frequencies = {}
        for n in nums:
            if n in frequencies:
                pairCount += frequencies[n]
            frequencies[n] = frequencies.get(n, 0) + 1
        return pairCount

# solution two that increments frequencies[n] before adding it to pairCount,
# so we have to subtract 1 from frequencies[n] before adding it to pairCount,
# but we can avoid the if statement
# Complexity:
# O(n) time - where n is the length of the input array nums
# O(n) space - where n is the length of the input array nums
class Solution:
    def numGoodPairs(self, nums):
        pairCount = 0
        frequencies = {}
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
            # every new occurrence of a number can be paired with every previous occurrence
            # so if a number has already appeared 'p' times, we will have 'p-1' new pairs
            pairCount += frequencies[n] - 1
        return pairCount