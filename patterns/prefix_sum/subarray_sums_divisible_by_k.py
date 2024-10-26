# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/subarray-sums-divisible-by-k-medium

'''Problem:
Given an array of integers nums and an integer k, return the count of non-empty subarrays that have a sum that is divisible by k.
A subarray is a continuous part of an array.

Input: nums = [3, 1, 2, -2, 5, -1], k = 3
Output: 7
Explanation: The subarrays that sum to a multiple of 3 are [3], [1, 2], [3, 1, 2], [3, 1, 2, -2, 5], [1, 2, -2, 5], [-2, 5], and [2, -2].

Input: nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
Explanation: The subarrays that sum to a multiple of 5 are [5], [4, 5, 0, -2, -3, 1], [5, 0], [0], [5, 0, -2, -3], [0, -2, -3], and [-2, -3].

Input: nums = [-1, 2, 9], k = 2
Output: 2
Explanation: The subarrays that sum to a multiple of 2 are [2] and [-1, 2, 9].
'''

# solution one without explicitly adjusting the remainder
# Complexity:
# O(n) time - where n is the length of the input array
# O(k) space - where k is the number of different remainders,
# in the worst case, the hash map will store all possible remainders from 0 to k - 1
class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}

        for num in nums:
            prefix_sum += num

            # get the remainder of the prefix sum divided by k
            remainder = prefix_sum % k

            # if the remainder of the prefix sum is in the map,
            # then we have found a number of subarray divisible by k
            # equals to the number of times the remainder has been seen
            if remainder in prefix_map:
                count += prefix_map[remainder]

            prefix_map[remainder] = prefix_map.get(remainder, 0) + 1

        return count

# solution two with explicitly adjusting the remainder
# Complexity:
# O(n) time - where n is the length of the input array
# O(k) space - where k is the number of different remainders,
# in the worst case, the hash map will store all possible remainders from 0 to k - 1
class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0

        prefix_map = {0: 1}
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            # get the remainder of the prefix sum divided by k
            remainder = prefix_sum % k
            # if remainder is negative, adjust it by adding k
            if remainder < 0:
                remainder += k

            # if the remainder of the prefix sum is in the map,
            # then we have found a number of subarray divisible by k
            # equals to the number of times the remainder has been seen
            if remainder in prefix_map:
                count += prefix_map[remainder]

            prefix_map[remainder] = prefix_map.get(remainder, 0) + 1

        return count