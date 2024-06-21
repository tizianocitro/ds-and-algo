# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a388c3b7eef54e90110f88

'''Problem:
Given two integer arrays to represent weights and profits of N items,
we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number C.
Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
'''

# solution one using top-down dp and memoization
# Complexity:
# O(nc) time - where n is the number of items and c is the capacity of the knapsack
# O(nc) space - where n is the number of items and c is the capacity of the knapsack
# it is for the memoization array
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # create a two dimensional array for Memoization,
        # each element is initialized to '-1'
        dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]

        return self.knapsack_recursive(dp, profits, weights, capacity, 0)

    def knapsack_recursive(self, dp, profits, weights, capacity, current_index):
        # base checks
        if capacity <= 0 or current_index >= len(profits):
            return 0

        # if we have already solved a similar problem, return the result from memory
        if dp[current_index][capacity] != -1:
            return dp[current_index][capacity]

        # recursive call after choosing the element at the current_index
        # if the weight of the element at current_index exceeds the capacity, we
        # shouldn't process this
        profit1 = 0
        if weights[current_index] <= capacity:
            profit1 = profits[current_index] + self.knapsack_recursive(
                dp, profits, weights, capacity - weights[current_index], current_index + 1)

        # recursive call after excluding the element at the current_index
        profit2 = self.knapsack_recursive(
            dp, profits, weights, capacity, current_index + 1)

        # add the problem to the solved ones
        dp[current_index][capacity] = max(profit1, profit2)

        return dp[current_index][capacity]

# solution two using bottom-up dp
# Complexity:
# O(nc) time - where n is the number of items and c is the capacity of the knapsack
# O(nc) space - where n is the number of items and c is the capacity of the knapsack
# it is for the dp matrix
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [[0 for x in range(capacity + 1)] for y in range(n)]

        # populate the capacity = 0 columns, with '0' capacity we have '0' profit
        for i in range(0, n):
            dp[i][0] = 0

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, capacity + 1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[i - 1][c - weights[i]]
                # exclude the item
                profit2 = dp[i - 1][c]
                # take maximum
                dp[i][c] = max(profit1, profit2)

        # maximum profit will be at the bottom-right corner.
        return dp[n - 1][capacity]

# solution three using bottom-up dp improved version of solution two
# Complexity:
# O(nc) time - where n is the number of items and c is the capacity of the knapsack
# O(c) space - c is the capacity of the knapsack, it is for the dp matrix
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        # we only need one previous row to find the optimal solution, overall we need '2' rows
        # the above solution is similar to the previous solution, the only difference is that
        # we use `i % 2` instead if `i` and `(i-1) % 2` instead if `i-1`
        dp = [[0 for x in range(capacity + 1)] for y in range(2)]

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = dp[1][c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(0, capacity + 1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
                # exclude the item
                profit2 = dp[(i - 1) % 2][c]
                # take maximum
                dp[i % 2][c] = max(profit1, profit2)

        return dp[(n - 1) % 2][capacity]

# solution four using bottom-up dp improved version of solution three
# Complexity:
# O(nc) time - where n is the number of items and c is the capacity of the knapsack
# O(c) space - c is the capacity of the knapsack, it is for the dp array
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [0 for x in range(capacity + 1)]

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(capacity, -1, -1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[c - weights[i]]
                # exclude the item
                profit2 = dp[c]
                # take maximum
                dp[c] = max(profit1, profit2)

        return dp[capacity]