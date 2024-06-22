# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a47de13f028e60d7da5a88

'''Problem:
Given a set of positive numbers, find if we can partition it into two subsets
such that the sum of elements in both subsets is equal.

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}

Input: {2, 3, 4, 6
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.
'''

# solution one using top-down dp
# Complexity:
# O(2^n) time - where n represents the total number of elements in the input array
# O(n) space - this space will be used to store the recursion stack (dfs-fashion)
class Solution:
    def canPartition(self, num):
        s = sum(num)
        # if 's' is a an odd number, we can't have two subsets with equal sum
        if s % 2 != 0:
            return False

        return self.recursiveCanPartition(num, s / 2, 0)

    def recursiveCanPartition(self, num, s, current_index):
        # base check
        if s == 0:
            return True

        n = len(num)
        # if s < 0 we exceeded the s / 2, while current_index >= n
        # checks if we have reached the end of the array
        if s < 0 or current_index >= n:
            return False

        # recursive call after choosing the number at the current_index
        # if the number at current_index exceeds the sum, we shouldn't process this
        if num[current_index] <= s:
            if self.recursiveCanPartition(num, s - num[current_index], current_index + 1):
                return True

        # recursive call after excluding the number at the current_index
        return self.recursiveCanPartition(num, s, current_index + 1)

# solution two using top-down dp and memoization
# Complexity:
# O(ns) time - where n represents the total number of elements in the
# input array and s is the total sum of all the numbers
# O(ns) space - this space will be used to store the memoization array
# and for the recursion stack (dfs-fashion)
class Solution:
    def canPartition(self, num):
        s = sum(num)
        # if 's' is a an odd number, we can't have two subsets with equal sum
        if s % 2 != 0:
            return False

        half_s = int(s / 2)

        # store prev results to avoid repeated work
        dp = [[-1 for _ in range(half_s + 1)] for _ in num]

        return True if self.recursiveCanPartition(num, half_s, 0, dp) == 1 else False

    def recursiveCanPartition(self, num, s, current_index, dp):
        # base check
        if s == 0:
            return 1

        n = len(num)
        # if s < 0 we exceeded the s / 2, while current_index >= n
        # checks if we have reached the end of the array
        if s < 0 or current_index >= n:
            return 0

        # avoid repeated work
        if dp[current_index][s] != -1:
            return dp[current_index][s]

        # recursive call after choosing the number at the current_index
        # if the number at current_index exceeds the sum, we shouldn't process this
        if num[current_index] <= s:
            if self.recursiveCanPartition(num, s - num[current_index], current_index + 1, dp) == 1:
                # store the result to avoid repeated work later
                dp[current_index][s] = 1
                return 1

        # recursive call after excluding the number at the current_index
        # store the result to avoid repeated work later
        dp[current_index][s] = self.recursiveCanPartition(num, s, current_index + 1, dp)
        return dp[current_index][s]

# solution three using bottom-up dp
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array
# and s is the total sum of all the numbers
# O(ns) space - this space will be used to store the dp matrix
class Solution:
    def canPartition(self, num):
        s = sum(num)
        # if 's' is a an odd number, we can't have two subsets with same total
        if s % 2 != 0:
            return False

        n = len(num)
        # we are trying to find a subset of given numbers that has a total sum of 's/2'.
        half_s = int(s / 2)
        dp = [[False for _ in range(half_s + 1)] for _ in range(n)]

        # populate the s=0 columns, as we can always for '0' sum with an empty set
        for i in range(n):
            dp[i][0] = True

        # with only one number, we can form a subset only
        # when the required sum is equal to its value
        for j in range(1, half_s + 1):
            dp[0][j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, half_s + 1):
                # if we can get the sum 'j' without the number at index 'i',
                # there is no use in considering it, so we can just reuse the prev value
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif num[i] <= j:
                    # else if we check if we can find a subset to get the remaining sum,
                    # e.g., if we we have half_s = 3 and we subtrack 2, we need to check
                    # if there is a 1 that we can use
                    dp[i][j] = dp[i - 1][j - num[i]]

        # the bottom-right corner will have our answer
        return dp[n - 1][half_s]

# solution four using bottom-up dp optimized version of solution three
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array
# and s is the total sum of all the numbers
# O(s) space - this space will be used to store the dp array
class Solution:
    def canPartition(self, num):
        s = sum(num)
        # if 's' is a an odd number, we can't have two subsets with same total
        if s % 2 != 0:
            return False

        n = len(num)
        # we are trying to find a subset of given numbers that has a total sum of 's/2'.
        half_s = int(s / 2)
        dp = [[False for _ in range(half_s + 1)] for _ in range(2)]

        # populate the s=0 columns, as we can always for '0' sum with an empty set
        for i in range(n):
            dp[0][0] = dp[1][0] = True

        # with only one number, we can form a subset only
        # when the required sum is equal to its value
        for j in range(1, half_s + 1):
            dp[0][j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, half_s + 1):
                # if we can get the sum 'j' without the number at index 'i',
                # there is no use in considering it, so we can just reuse the prev value
                if dp[(i - 1) % 2][j]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]
                elif num[i] <= j:
                    # else if we check if we can find a subset to get the remaining sum,
                    # e.g., if we we have half_s = 3 and we subtrack 2, we need to check
                    # if there is a 1 that we can use
                    dp[i % 2][j] = dp[(i - 1) % 2][j - num[i]]

        # the bottom-right corner will have our answer
        return dp[(n - 1) % 2][half_s]
