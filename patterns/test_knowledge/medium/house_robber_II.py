# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/house-robber-ii-medium

'''Problem:
You are given an array representing the amount of money each house has.
This array models a circle of houses, meaning that the first and last houses are adjacent.
You are tasked with figuring out the maximum amount of money you can rob without alerting the neighbors.

The rule is: if you rob one house, you cannot rob its adjacent houses.

Input: [4, 2, 3, 1]
Output: 7
Explanation: Rob the 1st and 3rd house, which gives 4 + 3 = 7.

Input: [5, 1, 2, 5]
Output: 7
Explanation: Rob the 1st and 3rd house, which gives 5 + 2 = 7.

Input: [1, 2, 3, 4, 5]
Output: 8
Explanation: Rob the 3rd and 5th house, which gives 3 + 5 = 8.
'''

'''Related Problems:
Also have a look at leetcode/198_house_robber.py and leetcode/213_house_robber_II.py
'''

# solution one usin top-down dp
# Complexity:
# O(n) time - where n is the number of houses
# O(n) space - where n is the number of houses
class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        # it can also be removed because the below code handles it as well
        if n == 2:
            # just return the max of the two numbers
            return max(nums)

        # otherwise we just need to exclude the first and last houses one at a time
        # and get the max of the two sums for the rest of the houses
        # in this way it works identically to leetcode/198_house_robber problem
        dp1 = [-1 for _ in range(n)]
        dp2 = [-1 for _ in range(n)]
        return max(self.robdp(nums, 0, n - 1, dp1), self.robdp(nums, 1, n, dp2))

    def robdp(self, nums, current_ix, end_ix, dp):
        # if we exceed the max index when can reach into the array (end_ix)
        # we return 0 because it must not be considered in the sum
        if current_ix >= end_ix:
            return 0

        if dp[current_ix] != -1:
            return dp[current_ix]

        # the sum considering the num at current_ix is basically summing
        # the current num with the sum that we get considering the number
        # at the index after the next (current_ix + 2)
        sum_with_num = nums[current_ix] + self.robdp(nums, current_ix + 2, end_ix, dp)

        # if we skip the current num, we just move to the next index
        # without adding the current num to the sum
        sum_without_num = self.robdp(nums, current_ix + 1, end_ix, dp)

        dp[current_ix] = max(sum_with_num, sum_without_num)
        return dp[current_ix]

# solution two
# Complexity:
# O(n) time - where n is the number of houses
# O(1) space
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        # it can also be removed because the below code handles it as well
        if n == 2:
            # just return the max of the two numbers
            return max(nums)

        # otherwise we just need to exclude the first and last houses one at a time
        # and get the max of the two sums for the rest of the houses
        # in this way it works identically to leetcode/198_house_robber problem
        return max(self.robp(nums, 0, n - 1), self.robp(nums, 1, n))

    def robp(self, nums, start, end):
        # rob2 is the last house we robbed
        # rob1 is the house before the last house we robbed
        rob1, rob2 = 0, 0

        # for each house we could rob
        for i in range(start, end):
            # the maximum we can rob is:
            # - the current house (nums[i]) + the house before the last house we robbed (rob1)
            # - or just the last house we robbed (rob2)
            temp = max(nums[i] + rob1, rob2)
            # update rob1 to point to which will now be the prev of the last house we robbed
            rob1 = rob2
            # update rob2 to the maximum we can rob up to this last house
            rob2 = temp

        return rob2