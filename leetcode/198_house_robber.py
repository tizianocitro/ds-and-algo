# !code: 198, !difficulty; medium, !from: https://leetcode.com/problems/house-robber/

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

# solution one usin top-down dp
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

# solution two using bottom-up dp
# Complexity:
# O(n) time - where n is the number of houses
# O(n) space - where n is the number of houses
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # initialize the dp array where dp[i] represents the
        # maximum amount of money that can be robbed up to house i
        dp = [0 for _ in range(n)]

        # base cases
        # if there's only one house, rob it
        dp[n - 1] = nums[n - 1]
        # if there are two houses, choose the maximum between them
        dp[n - 2] = max(nums[n - 1], nums[n - 2])

        # fill the dp array from the end towards the start
        for i in range(n - 3, -1, -1):
            # maximum between the current + the previous of the previous
            # and just the previous one
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        # at 0 will be the result
        return dp[0]

# solution three
# Complexity:
# O(n) time - where n is the number of houses
# O(1) space
class Solution:
    def rob(self, nums):
        # rob2 is the last house we robbed
        # rob1 is the house before the last house we robbed
        # we haven't robbed any house yet so they are both 0
        rob1, rob2 = 0, 0

        # for each house we could rob
        for n in nums:
            # the maximum we can rob is:
            # - the current house (n) + the house before the last house we robbed (rob1)
            # - or just the last house we robbed (rob2)
            temp = max(n + rob1, rob2)
            # update rob1 to point to which will now be the prev of the last house we robbed
            rob1 = rob2
            # update rob2 to the maximum we can rob up to this last house
            rob2 = temp

        return rob2