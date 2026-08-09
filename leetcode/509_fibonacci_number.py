# !code: 509, !difficult: easy, !from: https://leetcode.com/problems/fibonacci-number/

'''Problem:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Constraints:
- 0 <= n <= 30

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
'''

# solution one using bottom up dynamic programming with tabulation but space optimization
# as we store only the two previous numbers in the sequence to achieve O(1) space complexity
# Complexity:
# O(n) time - where n is the input number, since we calculate the fibonacci number for each number from 2 to n
# O(1) space - since we only store the fibonacci numbers for the two previous numbers
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # in the top-down approach and bottom-up approach, we only needed to look at the results of
        # fib(n-1) and fib(n-2) to determine the result of fib(n), therefore, we can achieve O(1) space complexity
        # by only storing the value of the two previous numbers and updating them as we iterate to n
        # dp0 is the fibonacci number for n - 2 and dp1 is the fibonacci number for n - 1
        # they are initialized to 0 and 1 respectively for the base cases as the first number we check is 2,
        # which is the third number in the sequence and is the sum of the first two numbers in the sequence
        dp0, dp1 = 0, 1
        for _ in range(2, n + 1):
            dpi = dp0 + dp1
            dp0 = dp1
            dp1 = dpi

        return dp1

# solution two using bottom up dynamic programming with tabulation
# Complexity:
# O(n) time - where n is the input number, since we calculate the fibonacci number for each number from 0 to n
# O(n) space - where n is the input number, since we store the fibonacci number for each number from 0 to n
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # store the fibonacci number for each number from 0 to n
        dp = [-1 for _ in range(n + 1)]
        # the base cases are 0 for dp[0] and 1 for dp[1] which is set here
        # we could also initialize the dp array with the base case for 0 in it:
        # dp = [0 for _ in range(n + 1)], then we would only need to set dp[1] = 1 here
        dp[0] = 0
        dp[1] = 1

        # for each number from 2 to n, calculate the fibonacci number
        # as the sum of the fibonacci numbers for the two previous numbers
        for num in range(2, n + 1):
            dp[num] = dp[num - 1] + dp[num - 2]

        # return the fibonacci number for n
        return dp[n]

# solution three using top down dynamic programming with memoization
# Complexity:
# O(n) time - where n is the input number, since we calculate the fibonacci number for each number from 0 to n
# O(n) space - where n is the input number, since we use a dictionary to store the fibonacci number for each number from 0 to n
class Solution:
    def fib(self, n: int) -> int:
        # we could also use a dictionary to store the fibonacci numbers
        # dp = {}
        dp = [-1 for _ in range(n + 1)] # or also dp = [-1] * (n + 1)
        return self.memoizedFib(n, dp)

    def memoizedFib(self, n, dp):
        # base cases
        # in alternative:
        # if n <= 1:
        #     return n
        if n == 0:
            return 0
        if n == 1:
            return 1

        # this is to avoid recalculating the fibonacci number for a number that we already calculated
        # if using dictionary:
        # if n in dp:
        if dp[n] != -1:
            return dp[n]

        # calculate the fibonacci number for n and store it for future use
        dp[n] = self.memoizedFib(n - 1, dp) + self.memoizedFib(n - 2, dp)
        return dp[n]

# solution four using brute force
# Complexity:
# O(2^n) time - where n is the input number, since each call branches into two recursive calls
# O(n) space - where n is the input number, since the depth of the recursion tree can go up to n
class Solution:
    def fib(self, n: int) -> int:
        # base cases
        # can also do:
        # if n <= 1:
        #     return n
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)