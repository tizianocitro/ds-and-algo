# !code: 121, !difficulty: easy, !from: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

# solution one using kadane's algorithm (dynamic programming)
# Complexity:
# O(n) time - where n is the number of prices
# O(1) space
class Solution:
    def maxProfit(self, prices):
        # we could start with min_price = prices[0] because it won't make any difference
        # as both price - inf and price - prices[0] will be so that
        # min(min_price, price) will return the same value as min_price the first iteration
        # min_price = prices[0]
        min_price, max_profit = float('inf'), 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

# solution two using sliding window
# Complexity:
# O(n) time - where n is the number of prices
# O(1) space
class Solution:
    def maxProfit(self, prices):
        # left points to the minimum price
        # right points to the current price
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            min_price = prices[left]
            price = prices[right]

            if min_price < price:
                max_profit = max(max_profit, price - min_price)
            else:
                # we move the left pointer to point to the new minimum price
                left = right

            # always move the right pointer to next price
            right += 1
        
        return max_profit
