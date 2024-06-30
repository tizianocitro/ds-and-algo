# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a4860bf76b432f5b473dea

'''Problem:
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number S.

Input: {1, 1, 2, 3}, S=4
Output: 3
Explanation: The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.

Input: {1, 2, 7, 1, 5}, S=9
Output: 3
Explanation: The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
'''

# solution one using top-down dp (brute-force)
# Complexity:
# O(2^n) time - where n represents the total number of elements in the input array.
# O(n) space - this space will be used to store the recursion stack (dfs-fashion)
class Solution:
    def countSubsets(self, num, sum1):
        return self.recursiveCountSubsets(num, sum1, 0)

    def recursiveCountSubsets(self, num, s, current_index):
        # base check: a new subset with sum equals to sum1 was found
        if s == 0:
            return 1

        if s < 0 or current_index >= len(num):
            return 0

        # recursive call after choosing the number at the current_index
        # if the number at current_Index exceeds the sum,
        # we shouldn't process the number so sum1 remains to 0
        sum1 = 0
        if num[current_index] <= s:
            sum1 = self.recursiveCountSubsets(num, s - num[current_index], current_index + 1)

        # recursive call after excluding the number at the currentIndex
        sum2 = self.recursiveCountSubsets(num, s, current_index + 1)

        # return the sum of the number of subsets with subset sum
        # equal to the input from both recursive calls
        return sum1 + sum2

# solution two using top-down dp and memoization
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array
# and s is the sum that we are trying to achieve, provided in input
# O(ns) space - due to the memoization array
class Solution:
    def countSubsets(self, num, sum1):
        # create a two dimensional array for Memoization,
        # each element is initialized to '-1'
        dp = [[-1 for _ in range(sum1 + 1)] for _ in num]
        return self.recursiveCountSubsets(num, sum1, 0, dp)

    def recursiveCountSubsets(self, num, s, current_index, dp):
        # base check: a new subset with sum equals to sum1 was found
        if s == 0:
            return 1

        if s < 0 or current_index >= len(num):
            return 0

        # check if we have already processed a similar problem
        if dp[current_index][s] != -1:
            return dp[current_index][s]

        # recursive call after choosing the number at the current_index
        # if the number at current_Index exceeds the sum,
        # we shouldn't process the number so sum1 remains to 0
        sum1 = 0
        if num[current_index] <= s:
            sum1 = self.recursiveCountSubsets(
                num, s - num[current_index], current_index + 1, dp)

        # recursive call after excluding the number at the currentIndex
        sum2 = self.recursiveCountSubsets(num, s, current_index + 1, dp)

        # store result in dp to avoid re-calculation
        # it is the sum of the number of subsets with subset sum
        # equal to the input from both recursive calls
        dp[current_index][s] = sum1 + sum2
        return dp[current_index][s]

'''Solution:
We will try to find if we can make all possible sums with every subset to populate the array dp[TotalNumbers][S+1].

So, at every step we have two options:
- Exclude the number. Count all the subsets without the given number up to the given sum => dp[index-1][sum]
- Include the number if its value is not more than the sum. In this case, we will count all the subsets to get the remaining sum => dp[index-1][sum-num[index]]

To find the total sets, we will add both of the above two values:
    dp[index][sum] = dp[index-1][sum] + dp[index-1][sum-num[index]])
'''

# solution three using bottom-up dp
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array
# and s is the sum that we are trying to achieve, provided in input
# O(ns) space - due to the two-dimensional array dp
class Solution:
    def countSubsets(self, num, sum1):
        n = len(num)
        dp = [[0 for _ in range(sum1 + 1)] for _ in range(n)]

        # populate the sum = 0 columns, as we will always have an empty set for zero sum
        for i in range(n):
            dp[i][0] = 1

        # with only one number, we can form a subset only
        # when the required sum is equal to its value
        for j in range(1, sum1 + 1):
            dp[0][j] = 1 if num[0] == j else 0

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, sum1 + 1):
                # exclude the number, so we just sum the subsets
                # that we already found for the current sum
                dp[i][j] = dp[i - 1][j]
                # include the number if it does not exceed the sum
                # so we need to sum all the subsets already found
                # for the sum remaining by including the number
                if num[i] <= j:
                    dp[i][j] += dp[i - 1][j - num[i]]

        # the bottom-right corner will have our answer
        return dp[n - 1][sum1]

# solution four using bottom-up dp optimized version of solution three
# this solution uses a single-dimensional array to store the count of subsets
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array
# and s is the sum that we are trying to achieve, provided in input
# O(s) space - due to the one-dimensional array dp
class Solution:
    def countSubsets(self, num, sum1):
        n = len(num)
        dp = [0 for _ in range(sum1 + 1)]

        # populate the sum = 0 index, as we will always have an empty set for zero sum
        dp[0] = 1

        # with only one number, we can form a subset only
        # when the required sum is equal to its value
        for j in range(1, sum1 + 1):
            dp[j] = 1 if num[0] == j else 0

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(sum1, -1, -1):
                # include the number if it does not exceed the sum
                # so we need to sum all the subsets already found
                if num[i] <= j:
                    dp[j] += dp[j - num[i]]

        return dp[sum1]

# solution five using bottom-up dp optimized version of solution three
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array
# and s is the sum that we are trying to achieve, provided in input
# O(s) space - due to the twp-dimensional array dp with always two alternating rows
class Solution:
    def countSubsets(self, num, sum1):
        n = len(num)
        dp = [[0 for _ in range(sum1 + 1)] for _ in range(2)]

        # populate the sum = 0 columns, as we will always have an empty set for zero sum
        dp[0][0] = dp[1][0] = 1

        # with only one number, we can form a subset only
        # when the required sum is equal to its value
        for j in range(1, sum1 + 1):
            dp[0][j] = 1 if num[0] == j else 0

        # process all subsets for all sums
        '''Important:
        In this case, the order of the two operation within the loop is important.
        We need to first exclude th number and then include it.
        So, we cannot change the order in contrast to solution three.
        '''
        for i in range(1, n):
            for j in range(1, sum1 + 1):
                # exclude the number, so we just sum the subsets
                # that we already found for the current sum
                dp[i % 2][j] = dp[(i - 1) % 2][j]
                # include the number if it does not exceed the sum
                # so we need to sum all the subsets already found
                # for the sum remaining by including the number
                if num[i] <= j:
                    dp[i % 2][j] += dp[(i - 1) % 2][j - num[i]]

        # the bottom-right corner will have our answer
        return dp[(n - 1) % 2][sum1]