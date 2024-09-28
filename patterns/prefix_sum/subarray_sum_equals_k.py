# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/subarray-sum-equals-k-medium

'''Problem:
Given an array nums containing n integers and integer k, return the total number of subarrays having sum equal to k.
A subarray is defined as a contiguous non-empty sequence of the array elements.

Input: nums = [1, 2, 3], k = 3
Output: 2
Explanation: There are two subarrays that sum to 3: [1, 2] and [3].

Input: nums = [10, 2, -2, -20, 10], k = -10
Output: 3
Explanation: Three subarrays sum up to -10: [10, 2, -2, -20], [2, -2, -20, 10], and [-20, 10].

Input: nums = [5, 1, 2, -3, 4, -2], k = 3
Output: 2
Explanation: There are two subarrays that sum to 3: [2, -3, 4], and [1, 2].
'''

'''Solution:
We will use a hashmap to efficiently track the cumulative sum of elements as we iterate through the array.
The core idea is that if the cumulative sum up to two indices, say i and j, differs by the target value k,
then the sum of the elements lying between i and j is k.

The algorithm will iterate through the array, calculating the cumulative sum at each step.
We then check if (cumulative sum - k) is present in the hashmap. If it is, it means there
exists a previous cumulative sum such that the difference between the current sum and that sum equals k,
indicating a valid subarray. We add the count of these occurrences to our total. Additionally,
we keep updating the hashmap with the count of each cumulative sum encountered. This approach is
effective as it allows us to find the required subarrays in a single pass through the array.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - for the prefix map
class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        # 0 is needed because if the cumulative sum up to two indices is k,
        # then we will need a 0 to keep track of it
        prefix_map = {0: 1}
        for num in nums:
            prefix_sum += num

            # if the cumulative sum up to two indices, say i and j, differs by the
            # target value k, then the sum of the elements lying between i and j is k
            diff = prefix_sum - k
            if diff in prefix_map:
                count += prefix_map[diff]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count