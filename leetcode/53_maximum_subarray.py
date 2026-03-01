# !code: 53, !difficulty: medium, !from: https://leetcode.com/problems/maximum-subarray, https://neetcode.io/problems/maximum-subarray

'''Problem:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

# solution one using Kadane's algorithm but cleaner
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def maxSubArray(self, nums) -> int:
        # -inf as nums might contain only negative numbers,
        # e.g., nums = [-1] and max_sum should be -1 in that case
        max_sum = float("-inf")

        current_sum = 0
        for num in nums:
            # this could also be done at the end of the loop, right after updating the max_sum
            # it's the same as we do it the next iteration
            # - first iteration: current_sum = 0, so it remains 0
            # - last iteration: even if current_sum becomes negative, we don't care
            if current_sum < 0:
                current_sum = 0

            current_sum += num
            max_sum = max(max_sum, current_sum)

            # if current_sum < 0:
            #     current_sum = 0

        return max_sum

# solution two using Kadane's algorithm
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        current_max = max_sum = nums[0]

        for i in range(1, n):
            num = nums[i]
            # current_max is the maximum between the previous current_max + num and num
            # because we want to understand which one is the most convenient to keep,
            # so basically we are deciding if we should keep the previous sum of numbers (i.e., current_max + num)
            # or if we should just start a new sum from the current number (i.e., num)
            current_max = max(num, current_max + num)

            # just alwats keep track of the maximum sum so far
            max_sum = max(max_sum, current_max)

        return max_sum
