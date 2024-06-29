# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a4810a4265331fa1ecf4aa

'''Problem:
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number S.

Input: {1, 2, 3, 7}, S=6
Output: True
Explanation: The given set has a subset whose sum is '6': {1, 2, 3}

Input: {1, 2, 7, 1, 5}, S=10
Output: True
Explanation: The given set has a subset whose sum is '10': {1, 2, 7}

Input: {1, 3, 4, 8}, S=6
Output: False
Explanation: The given set does not have any subset whose sum is equal to '6'
'''

# solution one using top-down dp (brute-force)
# Complexity:
# O(2^n) time - where n represents the total number of elements in the input array
# O(n) space - this space will be used to store the recursion stack (dfs-fashion)
class Solution:
    def canPartition(self, num, sum):
        # this can be added to avoid processing in case of sum > sum(num)
        # so it is not possible to find a subset whose sum is equal to sum
        # if sum(num) < sum:
        #     return False

        return self.recursiveCanPartition(num, sum, 0)

    def recursiveCanPartition(self, num, sum, current_index):
        # base check
        if sum == 0:
            return True

        # if sum < 0 we exceeded the sum, while current_index >= n
        # checks if we have reached the end of the array
        if sum < 0 or current_index >= len(num):
            return False

        # recursive call after choosing the number at the current_index
        # if the number at current_index exceeds the sum, we shouldn't process this
        if num[current_index] <= sum:
            if self.recursiveCanPartition(num, sum - num[current_index], current_index + 1):
                return True

        # recursive call after excluding the number at the current_index
        return self.recursiveCanPartition(num, sum, current_index + 1)

# solution two using top-down dp and memoization
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array and s is the input sum
# O(ns) space - this space will be used to store the memoization array
class Solution:
    def canPartition(self, num, sum):
        # this can be added to avoid processing in case of sum > sum(num)
        # so it is not possible to find a subset whose sum is equal to sum
        # if sum(num) < sum:
        #     return False

        # store prev results to avoid repeated work
        dp = [[-1 for _ in range(sum + 1)] for _ in range(len(num))]

        return True if self.recursiveCanPartition(num, sum, 0, dp) == 1 else False

    def recursiveCanPartition(self, num, sum, current_index, dp):
        # base check
        if sum == 0:
            return 1

        # if sum < 0 we exceeded the sum, while current_index >= n
        # checks if we have reached the end of the array
        if sum < 0 or current_index >= len(num):
            return 0

        # avoid repeated work
        if dp[current_index][sum] != -1:
            return dp[current_index][sum]

        # recursive call after choosing the number at the current_index
        # if the number at current_index exceeds the sum, we shouldn't process this
        if num[current_index] <= sum:
            if self.recursiveCanPartition(num, sum - num[current_index], current_index + 1, dp):
                # store the result to avoid repeated work later
                dp[current_index][sum] = 1
                return 1

        # recursive call after excluding the number at the current_index
        # store the result to avoid repeated work later
        dp[current_index][sum] = self.recursiveCanPartition(num, sum, current_index + 1, dp)
        return dp[current_index][sum]

# solution three using bottom-up dp
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array and s is the input sum
# O(ns) space - this space will be used to store the dp array
class Solution:
    def canPartition(self, num, s):
        if sum(num) < s:
            return False

        n = len(num)
        dp = [[False for _ in range(s + 1)] for _ in range(n)]

        # populate the sum = 0 columns, as we can always form '0' sum with an empty set
        for i in range(n):
            dp[i][0] = True

        # with only one number, we can form a subset only when
        # the required sum is equal to its value
        for j in range(1, s + 1):
            dp[0][j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, s + 1):
                # if we can get the sum 's' without the number at index 'i'
                # because if dp[i - 1][j] == True, it means the sum has already been reached
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif num[i] <= j:
                    # else include the number to see if we can find a subset to get the remaining sum
                    dp[i][j] = dp[i - 1][j - num[i]]

        # the bottom-right corner will have our answer
        return dp[n - 1][s]

# solution four using bottom-up dp optimized version of solution three
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array and s is the input sum
# O(s) space - this space will be used to store the dp array
class Solution:
    def canPartition(self, num, s):
        if sum(num) < s:
            return False

        n = len(num)
        dp = [[False for _ in range(s + 1)] for _ in range(2)]

        # populate the sum = 0 columns, as we can always form '0' sum with an empty set
        dp[0][0] = dp[1][0] = True

        # with only one number, we can form a subset only when
        # the required sum is equal to its value
        for j in range(1, s + 1):
            dp[0][j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, s + 1):
                # if we can get the sum 's' without the number at index 'i'
                # because if dp[i - 1][j] == True, it means the sum has already been reached
                if dp[(i - 1) % 2][j]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]
                elif num[i] <= j:
                # else include the number to see if we can find a subset to get the remaining sum
                    dp[i % 2][j] = dp[(i - 1) % 2][j - num[i]]

        # the bottom-right corner will have our answer
        return dp[(n - 1) % 2][s]

# solution five using bottom-up dp optimized version of solution four (only one array)
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array and s is the input sum
# O(s) space - this space will be used to store the dp array
class Solution:
    def canPartition(self, num, s):
        if sum(num) < s:
            return False

        n = len(num)
        # this solution uses a simple array to store the previous result
        dp = [False for _ in range(s + 1)]

        # handle sum=0, as we can always have '0' sum with an empty set
        dp[0] = True

        # with only one number, we can have a subset only when
        # the required sum is equal to its value
        for j in range(1, s + 1):
            dp[j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(s, -1, -1):
                # if dp[j] == True, this means we can get the sum 'j' without num[i], so we 
                # can move on to the next number else we can include num[i] and see if we 
                # can find a subset to get the remaining sum
                if not dp[j] and num[i] <= j:
                    dp[j] = dp[j - num[i]]

            return dp[s]