# !code: 70, !difficulty: easy, !from: https://leetcode.com/problems/climbing-stairs/

'''Problem:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top:
    1. 1 step + 1 step
    2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top:
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
'''

# solution one using space optimized dynamic programming
# Complexity:
# O(n) time - where n is the number of steps
# O(1) space
class Solution:

    def climbStairs(self, n: int) -> int:
        # base case, there is only one way to reach 0 and 1
        # for n = 0 or n = 1, there’s only one way to reach the top,
        # as you can either stay at the start (0) or take one step (1)
        if n <= 1:
            return 1

        # the two previous steps are 1
        # prev is the number of ways to reach the prev of the prev step
        # curr is the number of ways to reach the prev step
        prev, curr = 1, 1

        # we start from two because we already know the result for n = 0 and n = 1
        # for i = 2, prev = 1, curr = 1 and after the loop, prev = 1, curr = 2
        # for i = 3, prev = 1, curr = 2 and after the loop, prev = 2, curr = 3
        # for i = 4, prev = 2, curr = 3 and after the loop, prev = 3, curr = 5
        # for i = 5, prev = 3, curr = 5 and after the loop, prev = 5, curr = 8
        # and so on
        for _ in range(2, n + 1):
            temp = prev + curr
            prev = curr
            curr = temp

        return curr

# solution two using fibonacci sequence
# Complexity:
# O(n) time - where n is the number of steps
# O(n) space - for the recursion stack and the memoization dictionary
class Solution:

    def climbStairs(self, n: int) -> int:
        # these other two option would allow to remove the base case
        # from the climbStairsMemo function:
        # dp = {0: 1, 1: 1}
        # dp = [-1] * (n + 1)
        # dp[0] = dp[1] = 1
        dp = {}
        return self.climbStairsMemo(n, dp)

    def climbStairsMemo(self, n: int, dp) -> int:
        # base case, there is only one way to reach 0 and 1
        if n == 0 or n == 1:
            return 1

        if n in dp:
            return dp[n]

        # recursive call to climbStairs as in fibonacci sequence
        dp[n] = self.climbStairsMemo(n - 1, dp) + self.climbStairsMemo(n - 2, dp)

        return dp[n]

# solution three using fibonacci sequence
# Complexity:
# O(2^n) time - where n is the number of steps
# O(n) space - for the recursion stack
class Solution:

    def climbStairs(self, n: int) -> int:
        # base case, there is only one way to reach 0 and 1
        if n == 0 or n == 1:
            return 1

        # recursive call to climbStairs as in fibonacci sequence
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)