# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/find-the-middle-index-in-array-easy

'''Problem:
Given an integer array nums, return the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
A middleIndex is an index where the sum of the numbers to the left of this index is equal to the sum of the numbers to the right of this index.
You can consider the left sum 0 for middleIndex == 0, and right sum 0 for middleIndex == nums.length - 1.
If no middleIndex exists in nums, return -1.

Input: nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of the numbers to the right of index 3 (5 + 6 = 11).

Input: nums = [2, 1, -1]
Output: 0
Explanation: The sum of the numbers to the left of index 0 is considered to be 0. The sum of the numbers to the right of index 0 (1 + -1 = 0) is also 0.

Input: nums = [2, 3, 5, 5, 3, 2]
Output: -1
Explanation: There is no middleIndex exists in the array.
'''

# solution one without using prefix sum array
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findMiddleIndex(self, nums) -> int:
        # calculate the total sum of all elements in the array
        total_sum = sum(nums)

        left_sum = 0
        for i, num in enumerate(nums):
            # calculate the sum of elements to the right by subtracting
            # the current element and the left sum from the total sum
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num

        return -1

# solution two using prefix sum array
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - to store the prefix sum array
class Solution:
    def findMiddleIndex(self, nums) -> int:
        prefix = self.computerPrefixSums(nums)

        for i in range(len(nums)):
            left_sum = 0 if i == 0 else prefix[i - 1]
            # the right sum is 0 if i is the last index or the sum at
            # the last index minus the sum at the index i, because
            # we need to include the element at index i + 1
            right_sum = 0 if i == len(nums) - 1 else prefix[len(nums) - 1] - prefix[i]
            if left_sum == right_sum:
                return i

        return -1

    def computerPrefixSums(self, nums):
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        return prefix
