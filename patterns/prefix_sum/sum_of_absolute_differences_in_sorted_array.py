# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/sum-of-absolute-differences-in-a-sorted-array-medium

'''Problem:
Given an integer array nums sorted in increasing order, return an array result of the same length,
where result[i] should be the sum of the absolute differences between nums[i] and every other element in nums.

Input: [1, 3, 6]
Output: [7, 5, 8]
Explanation:
    For result[0]: |1-3| + |1-6| = 2 + 5 = 7
    For result[1]: |3-1| + |3-6| = 2 + 3 = 5
    For result[2]: |6-1| + |6-3| = 5 + 3 = 8

Input: [2, 4, 7]
Output: [7, 5, 8]
Explanation:
    For result[0]: |2-4| + |2-7| = 2 + 5 = 7
    For result[1]: |4-2| + |4-7| = 2 + 3 = 5
    For result[2]: |7-2| + |7-4| = 5 + 3 = 8

Input: [1, 2, 4, 5]
Output: [8, 6, 6, 6]
Explanation:
    For result[0]: |1-2| + |1-4| + |1-5| = 1 + 3 + 4 = 8
    For result[1]: |2-1| + |2-4| + |2-5| = 1 + 2 + 3 = 6
    For result[2]: |4-1| + |4-2| + |4-5| = 3 + 2 + 1 = 6
    For result[3]: |5-1| + |5-2| + |5-4| = 4 + 3 + 1 = 8
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - to store the result array and the prefix sum array
class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        result = [0] * n

        # calculate the prefix sum array
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        for i in range(n):
            left_sum = prefix_sum[i - 1] if i > 0 else 0
            right_sum = prefix_sum[n - 1] - prefix_sum[i]

            # this is the formula for the sum of absolute differences, it can be derived by
            # subtracting the sum of the elements to the left of the current element from the
            # product of the current element and its index (i), and adding the difference between
            # the sum of the elements to the right of the current element and the product of the
            # difference between the length of the array (n - 1) and the current index (i) and the current element
            # (which corresponds to number of elements to the right of the current element)
            # notice that the forumla must be in that specifc order of the two differences in parentheses
            result[i] = (i * nums[i] - left_sum) + (right_sum - (n - 1 - i) * nums[i])

        return result