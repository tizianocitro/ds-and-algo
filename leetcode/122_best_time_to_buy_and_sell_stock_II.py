# !code: 122, !difficulty: medium, !from: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/, https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii/

'''Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Constraints:
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation:
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
'''

# solution one using kadane's algorithm (dynamic programming)
# Complexity:
# O(n) time - where n is the length of the prices array
# O(1) space
class Solution:
    def maxProfit(self, prices) -> int:
        # we could start with prices[0] because it won't make any difference
        # as both price - inf and price - prices[0] will be so that profit < current_profit
        # and will use current_profit = 0 as a first profit to add to max_profit
        # min_price = prices[0]
        min_price = float('inf')
        current_profit = max_profit = 0

        for price in prices:
            profit = price - min_price

            # if the profit we would make by selling in this day is lower than
            # the profit we could make by selling in the previous day, we do so
            # by adding the current_profit to max_profit, resetting current_profit
            # and moving the min_price to sell to the current price
            if profit < current_profit:
                max_profit += current_profit
                current_profit = 0
                min_price = price
            else:
                # otherwise, we update the current_profit because the profit by selling
                # this day is higher than the day before and we want to check if we can
                # earn a better profit the day after
                current_profit = profit

        # this is for cases where the best day to sell is the last day,
        # so we end the loop and don't process the 'profit < current_profit' case
        # so we sell here to get the last profit
        max_profit += current_profit

        return max_profit

# solution two using the peak valley approach
# the idea is that the max profit will be the sum of all the times we can
# buy in a valley, which is the lowest price in a trend,
# and sell in a peak, which is the highest price in a trend.
# more at https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/editorial/#approach-2-peak-valley-approach
# Complexity:
# O(n) time - where n is the length of the prices array
# O(1) space
class Solution:
    def maxProfit(self, prices) -> int:
        i = 0

        # a valley is the lowest point in a downward trend
        valley = prices[0]
        # a peak is the highest point in an upward trend
        peak = prices[0]

        # the max profit will be the sum of all the times
        # we buy at valley and sell at peak
        max_profit = 0

        while i < len(prices) - 1:
            # reach the valley
            # if we are in a valley already, we don't do this
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            # we have reached a valley
            valley = prices[i]

            # reach the peak
            # if we are in a peak already, we don't do this
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            # we have reached a peak
            peak = prices[i]

            # we sell every time we reach a peak starting from a valley
            max_profit += peak - valley

        return max_profit

# solution three using a greedy approach
# Complexity:
# O(n) time - where n is the length of the prices array
# O(1) space
class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            # the idea is that if we sell every day that the price is
            # lower than the day before, we will make a profit
            # and summing all of them will give us the highest profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit