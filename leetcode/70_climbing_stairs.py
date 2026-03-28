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
        # this is not really needed, as if n = 1, we return dp1 = 1
        # base case, there is only one way to reach 0 and 1
        # for n = 0 or n = 1, there’s only one way to reach the top,
        # as you can either stay at the start (0) or take one step (1)
        if n <= 1:
            return 1

        # the two previous steps are 1
        # dp0 is the number of ways to reach the prev of the prev step
        # dp1 is the number of ways to reach the prev step
        dp0, dp1 = 1, 1

        # we start from two because we already know the result for n = 0 and n = 1
        # for i = 2, dp0 = 1, dp1 = 1 and after the loop, dp0 = 1, dp1 = 2
        # for i = 3, dp0 = 1, dp1 = 2 and after the loop, dp0 = 2, dp1 = 3
        # for i = 4, dp0 = 2, dp1 = 3 and after the loop, dp0 = 3, dp1 = 5
        # for i = 5, dp0 = 3, dp1 = 5 and after the loop, dp0 = 5, dp1 = 8
        # and so on
        for _ in range(2, n + 1):
            dpstep = dp0 + dp1
            dp0 = dp1
            dp1 = dpstep

        return dp1

# solution two using bottom up dynamic programming with tabulation
# Complexity:
# O(n) time - where n is the number of steps
# O(n) space - where n is the number of steps
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = dp[1] = 1

        for step in range(2, n + 1):
            dp[step] = dp[step - 1] + dp[step - 2]

        return dp[n]


# solution three using top down dynamic programming with memoization
# Complexity:
# O(n) time - where n is the number of steps as we are storing the result of each step in the dp array and we are only calculating each step once
# O(n) space - for the recursion stack and the memoization dictionary
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.climb(n, dp)

    def climb(self, n, dp):
        if n < 2:
            # - 0 -> 1: in combinatorics, doing nothing is considered 1
            #           also considering that climb(2) = 2, so we need climb(0) = 1
            # - 1 -> 1: 1 way to reach 1 from 0 (taking 1 step)
            return 1

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.climb(n - 1, dp) + self.climb(n - 2, dp)
        return dp[n]

# solution four using recursion
# Complexity:
# O(2^n) time - where n is the number of steps
# O(n) space - for the recursion stack
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb(n)

    def climb(self, n):
        if n < 2:
            # - 0 -> 1: in combinatorics, doing nothing is considered 1
            #           also considering that climb(2) = 2, so we need climb(0) = 1
            # - 1 -> 1: 1 way to reach 1 from 0 (taking 1 step)
            return 1
        return self.climb(n - 1) + self.climb(n - 2)

# solution five using bottom up dynamic programming with tabulation but space optimization
# Complexity:
# O(n) time - where n is the number of steps
# O(1) space - since we only store the number of ways to reach the previous two steps
class Solution:
    def climbStairs(self, n: int) -> int:
        # intially, it stores the number of ways to reach the step n + 1,
        # which is 0 as we cannot go beyond n
        dpn1 = 0
        # initially, it stores the number of ways to reach the step n,
        # which is 1 as there is only one way to reach n from n - 1
        dpn = 1

        for _ in range(n - 1, -1, -1):
            dpstep = dpn1 + dpn
            dpn1 = dpn
            dpn = dpstep

        return dpn

# solution six using bottom up dynamic programming with tabulation
# Complexity:
# O(n) time - where n is the number of steps
# O(n) space - where n is the number of steps
class Solution:
    def climbStairs(self, n: int) -> int:
        # we store n + 1 as well because we need the next two steps
        # to calculate the number of ways to reach the current step
        dp = [-1] * (n + 2)
        dp[n + 1] = 0
        dp[n] = 1

        # start from the step before n and go down to 0, calculating the number of ways to reach each step
        for step in range(n - 1, -1, -1):
            dp[step] = dp[step + 1] + dp[step + 2]

        return dp[0]

# solution seven using top down dynamic programming with memoization
# Complexity:
# O(n) time - where n is the number of steps as we are storing the result of each step in the dp array and we are only calculating each step once
# O(n) space - for the recursion stack and the dp array
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.climb(0, n, dp)

    def climb(self, step, n, dp):
        if step == n:
            return 1
        if step > n:
            return 0

        if dp[step] != -1:
            return dp[step]

        dp[step] = self.climb(step + 1, n, dp) + self.climb(step + 2, n, dp)
        return dp[step]

# solution eight using recursion
# Complexity:
# O(2^n) time - where n is the number of steps
# O(n) space - for the recursion stack
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb(0, n)

    def climb(self, step, n):
        if step == n:
            return 1
        # cannot go more than n
        if step > n:
            return 0

        return self.climb(step + 1, n) + self.climb(step + 2, n)