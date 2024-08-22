# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/maximum-size-subarray-sum-equals-k-medium

'''Problem:
Given an array of integers nums and an integer k, find the length of the longest subarray that sums to k. If no such subarray exists, return 0.

Input: nums = [1, 2, 3, -2, 5], k = 5
Output: 2
Explanation: The longest subarray with a sum of 5 is [2, 3], which has a length of 2.

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The longest subarray with a sum of 1 is [-1, 2], which has a length of 2.

Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
Output: 4
Explanation: The longest subarray with a sum of 7 is [7, 2, -3, 1], which has a length of 4.
'''

# solution one
# Complexity:
# O(n) time - where n is the number of elements in the input array
# O(n) space - for the cumulative sum dictionary
class Solution:
    def maxSubArrayLen(self, nums, k):
        # a dictionary to store cumulative sums and their earliest indices
        # it is of the form {cumulative_sum: index}
        cum_map = {}

        cum_sum = 0
        max_len = 0

        for i in range(len(nums)):
            # update cumulative sum
            cum_sum += nums[i]

            # check if cumulative sum equals k, then we have found a subarray
            # and it is the longest subarray so far because it includes all elements
            if cum_sum == k:
                max_len = i + 1

            # check if there is a subarray with sum k because if there is,
            # then it means that we can subtruck that number and get k as sum
            if cum_sum - k in cum_map:
                max_len = max(max_len, i - cum_map[cum_sum - k])

            # store the cumulative sum and its earliest index because
            # by using the earliest index we get the longest subarray
            if cum_sum not in cum_map:
                cum_map[cum_sum] = i

        return max_len