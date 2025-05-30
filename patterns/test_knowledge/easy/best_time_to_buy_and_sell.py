# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/best-time-to-buy-and-sell-easy

'''Problem:
You are given an array prices where prices[i] is the price of a given stock on the  day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: [3, 2, 6, 5, 0, 3]
Output: 4
Explanation: Buy the stock on day 2 (price = 2) and sell it on day 3 (price = 6). Profit = 6 - 2 = 4.

Input: [8, 6, 5, 2, 1]
Output: 0
Explanation: Prices are continuously dropping, so no profit can be made.

Input: [1, 2]
Output: 1
Explanation: Buy on day 1 (price = 1) and sell on day 2 (price = 2). Profit = 2 - 1 = 1.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the prices
# O(1) space
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        cost = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            if price < cost:
                cost = price
            else:
                profit = max(profit, price - cost)

        return profit

# solution two
# Complexity:
# O(n) time - where n is the length of the prices
# O(1) space
class Solution:
    def maxProfit(self, prices):
        min_price, max_profit = float('inf'), 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
