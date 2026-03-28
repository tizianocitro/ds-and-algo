# !code: 198, !difficulty; medium, !from: https://leetcode.com/problems/house-robber, https://neetcode.io/problems/house-robber

'''Problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it
will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.
'''

'''Related problems:
Also have a look at leetcode/213_house_robber_II.py and patterns/test_knowledge/medium/house_robber_II.py
'''

# solution one using bottom-up dyamic programming with space optimization
# Complexity:
# O(n) time - where n is the number of houses
# O(1) space
class Solution:
    def rob(self, nums):
        # rob2 is the last house we robbed
        # rob1 is the house before the last house we robbed
        # we haven't robbed any house yet, so they are both 0
        rob1, rob2 = 0, 0

        # for each house we could rob
        for house in nums:
            # the maximum we can rob is:
            # - the current house + the house before the last house we robbed (rob1)
            # - or just the last house we robbed (rob2)
            rob_house = max(house + rob1, rob2)
            # update rob1 to point to which will now be the prev of the last house we robbed
            rob1 = rob2
            # update rob2 to the maximum we can rob up to this house
            rob2 = rob_house

        return rob2

# solution two using bottom-up dyamic programming starting from the start of the array
# Complexity:
# O(n) time - where n is the number of houses
# O(n) space - where n is the number of houses
class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])

        for house in range(2, n):
            dp[house] = max(dp[house - 2] + nums[house], dp[house -1])

        return dp[n - 1]

# solution three using bottom-up dyamic programming starting from the end of the array
# Complexity:
# O(n) time - where n is the number of houses
# O(n) space - where n is the number of houses
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            # no houses to rob, so we return 0
            return 0
        if n == 1:
            # only one house to rob, so we return the amount in that house
            return nums[0]

        # initialize the dp array where dp[i] represents the
        # maximum amount of money that can be robbed up to house i
        dp = [0 for _ in range(n)]

        # when we are at the last house, the maximum we can rob is just the amount in that house
        dp[n - 1] = nums[n - 1]
        # in the second to last house, the maximum we can rob is the maximum between
        # the amount in that house and the amount in the last house
        # equivalent to: dp[n - 2] = max(dp[n - 1], nums[n - 2])
        dp[n - 2] = max(nums[n - 1], nums[n - 2])

        # fill the dp array from the end towards the start
        for house in range(n - 3, -1, -1):
            # maximum between the current + the previous of the previous and just the previous one
            dp[house] = max(nums[house] + dp[house + 2], dp[house + 1])

        # the result is at house 0 as we built the dp array from the end towards the start
        return dp[0]

# solution four using top-down dyamic programming with memoization
# Complexity:
# O(n) time - where n is the number of houses
# O(n) space - where n is the number of houses
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [-1 for _ in range(len(nums))]
        return self.robdp(nums, 0, dp)

    def robdp(self, nums, current_ix, dp):
        # if we exceed the length of the array, we return 0
        # because it must not be considered in the sum
        if current_ix >= len(nums):
            return 0

        if dp[current_ix] != -1:
            return dp[current_ix]

        # the sum considering the num at current_ix is basically summing
        # the current num with the sum that we get considering the number
        # at the index after the next (current_ix + 2)
        sum_with_num = nums[current_ix] + self.robdp(nums, current_ix + 2, dp)

        # if we skip the current num, we just move to the next index
        # without adding the current num to the sum
        sum_without_num = self.robdp(nums, current_ix + 1, dp)

        dp[current_ix] = max(sum_with_num, sum_without_num)
        return dp[current_ix]
