# !code: 322, !difficulty: medium, !from: https://leetcode.com/problems/coin-change/

'''Problem:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 231 - 1
- 0 <= amount <= 104

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0 
'''

# solution one using bottom-up dynamic programming
# Complexity:
# O(an) time - where a represents the amount and n is the number of coins
# O(a) space - to store the dp array
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # initialize a dp array with size amount + 1,
        # filled with inf (assuming all amounts are unreacheable)
        dp = [float('inf')] * (amount + 1)

        # base case: to make amount 0, we need 0 coins
        dp[0] = 0

        # iterate through each coin in the given coins list
        # for each coin, we try to compute the minimum number of coins required for all
        # possible amounts starting from the coin value up to the target amount
        for coin in coins:
            # for each amount x, we check if using the current coin gives
            # a smaller number of coins to make that amount
            for x in range(coin, amount + 1):
                # we update dp[x] by checking if using the current coin
                # gives us a smaller number of coins, considering that:
                # - dp[x - coin] is the number of coins needed to make amount (x - coin)
                # - dp[x] is the current number of used coins
                # - dp[x - coin] + 1 is the number of used coins if we add the current coin to the used coins
                dp[x] = min(dp[x], dp[x - coin] + 1)

        # if dp[amount] is still inf, it means we couldn't make up that amount, return -1
        # otherwise, return dp[amount], which represents the minimum number of coins needed
        return dp[amount] if dp[amount] != float('inf') else -1
