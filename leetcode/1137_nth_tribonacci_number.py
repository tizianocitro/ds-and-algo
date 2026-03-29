# !code: 1137, !difficulty: easy, !from: https://leetcode.com/problems/n-th-tribonacci-number, https://neetcode.io/problems/n-th-tribonacci-number

"""Problem:
The Tribonacci sequence Tn is defined as follows: T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Constraints:
- 0 <= n <= 37
- The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Input: n = 25
Output: 1389537
"""

# solution one using bottom up approach with optimal space complexity
# Complexity:
# O(n) time - where n is the input number
# O(1) space
class Solution:
    def tribonacci(self, n: int) -> int:
        values = [0, 1, 1]
        if n < 3:
            return values[n]

        dp0 = 0
        dp1 = dp2 = 1
        for _ in range(3, n + 1):
            dpstep = dp0 + dp1 + dp2
            dp0 = dp1
            dp1 = dp2
            dp2 = dpstep

        return dp2

# solution two using bottom up approach with tabulation
# Complexity:
# O(n) time - where n is the input number because each number from 0 to n is computed once and stored in the dp array
# O(n) space - where n is the input number because of the dp array used for tabulation
class Solution:
    def tribonacci(self, n: int) -> int:
        values = [0, 1, 1]
        if n < 3:
            return values[n]

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for step in range(3, n + 1):
            dp[step] = dp[step - 1] + dp[step - 2] + dp[step - 3]

        return dp[n]

# solution three using top down approach with memoization
# Complexity:
# O(n) time - where n is the input number because each number from 0 to n is computed at most once and stored in the dp array
# O(n) space - where n is the input number because of the dp array used for memoization and the call stack used for recursion
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.memo_tribonacci(n, dp)

    def memo_tribonacci(self, n, dp):
        values = [0, 1, 1]
        if n < 3:
            return values[n]

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.memo_tribonacci(n - 1, dp) + \
            self.memo_tribonacci(n - 2, dp) + \
            self.memo_tribonacci(n - 3, dp)

        return dp[n]

# solution four using recursion
# Complexity:
# O(3^n) time - where n is the input number because each call to the function results in three more calls until the base case is reached
# O(n) space - where n is the input number because of the call stack used for recursion
class Solution:
    def tribonacci(self, n: int) -> int:
        values = [0, 1, 1]
        if n < 3:
            return values[n]

        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
