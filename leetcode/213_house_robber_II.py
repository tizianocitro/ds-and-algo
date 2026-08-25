# !code: 213, !difficulty: medium, !from: https://leetcode.com/problems/house-robber-ii/, https://neetcode.io/problems/house-robber-ii

'''Problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.

Input: nums = [1,2,3]
Output: 3
'''

# solution one using dynamic programming
# Complexity:
# O(n) time - where n is the number of houses
# O(1) space
class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        # if n is 1, we can only rob that one house, so we return the amount in that house
        # we don't check for n == 0 because the constraints say there will be at least one house to rob
        if n == 1:
            return nums[0]

        # we need to exclude the first and last houses one at a time
        # and get the max of the two sums for the rest of the houses
        # in this way it works identically to leetcode/198_house_robber problem
        return max(
            self.robHouse(nums, 0, n - 1),
            self.robHouse(nums, 1, n)
        )

    def robHouse(self, nums, start, end):
        # rob2 is the last house we robbed
        # rob1 is the house before the last house we robbed
        rob1, rob2 = 0, 0

        # for each house we could rob
        for house in range(start, end):
            # the maximum we can rob is:
            # - the current house (nums[house]) + the house before the last house we robbed (rob1)
            # - or just the last house we robbed (rob2)
            rob_house = max(nums[house] + rob1, rob2)
            # update rob1 to point to which will now be the prev of the last house we robbed
            rob1 = rob2
            # update rob2 to the maximum we can rob up to this last house
            rob2 = rob_house

        return rob2
