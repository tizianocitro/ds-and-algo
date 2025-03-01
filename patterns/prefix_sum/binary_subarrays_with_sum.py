# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/binary-subarrays-with-sum-medium

'''Problem:
Given a binary called nums and an integer called goal, return the number of subarrays that have a sum equal to goal.

A subarray is a part of the array that is continuous, meaning all its elements are next to each other.

Input: nums = [1, 1, 0, 1, 1], goal = 2
Output: 5
Explanation: The subarrays with a sum of 3 are: [1, 1] (from index 0 to 1), [1, 1, 0] (from index 0 to 2), [1, 0, 1] (from index 1 to 3), [0, 1, 1] (from index 2 to 5), and [1, 1] (from index 4 to 5).

Input: nums = [1, 1, 1, 1, 0, 0], goal = 3
Output: 4
Explanation: The subarrays with a sum of 3 are: [1, 1, 1] (from index 0 to 2), [1, 1, 1] (from index 1 to 3), [1, 1, 1, 0] (from index 1 to 4), and [1, 1, 1, 0, 0] (from index 1 to 5).

Input: nums = [0, 0, 0, 0, 1, 0, 1], goal = 1
Output: 12
Explanation: The subarrays with a sum of 1 are: [0, 0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 1], [0, 1], [1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0], [1, 0], [0, 1], and [1]`.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - for the prefix map
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        prefix_sum = 0
        count = 0

        # initialize hashmap for prefix sums with initial prefix sum of 0
        prefix_map = {}
        prefix_map[0] = 1

        for num in nums:
            prefix_sum += num

            # if (prefix_sum - goal) exists in hashmap, it means
            # we found a subarray with sum equals to goal
            if prefix_sum - goal in prefix_map:
                # update count with how many times we already found
                # the sum equals to (prefix_sum - goal)
                count += prefix_map[prefix_sum - goal]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count