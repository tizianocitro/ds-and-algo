# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a48397f76b432f5b473bd5

'''Problem:
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
'''

# solution one using top-down dp
# Complexity:
# O(2^n) time - where n represents the total number of elements in the input array
# O(n) space - this space will be used to store the recursion stack (dfs-fashion)
class Solution:
    def canPartition(self, num):
        return self.recursiveCanPartition(num, 0, 0, 0)

    def recursiveCanPartition(self, num, current_index, sum1, sum2):
        # base check, we have a full subset
        if current_index == len(num):
            return abs(sum1 - sum2)

        # recursive call after including the number at the current_index in the first set
        diff1 = self.recursiveCanPartition(
            num, current_index + 1, sum1 + num[current_index], sum2)

        # recursive call after including the number at the current_index in the second set
        diff2 = self.recursiveCanPartition(
            num, current_index + 1, sum1, sum2 + num[current_index])

        return min(diff1, diff2)

# solution two using top-down dp and memoization
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array and s is the sum of all the numbers
# O(ns) space - where n represents the total number of elements in the input array and s is the sum of all the numbers
# for the memoization array
class Solution:
    def canPartition(self, num):
        # the maximum sum possible is the sum of all the numbers
        num_sum = sum(num)
        dp = [[-1 for _ in range(num_sum + 1)] for _ in num]

        return self.recursiveCanPartition(num, 0, 0, 0, dp)

    def recursiveCanPartition(self, num, current_index, sum1, sum2, dp):
        # base check, we have a full subset
        if current_index == len(num):
            return abs(sum1 - sum2)

        # check if we have already processed similar problem
        if dp[current_index][sum1] != -1:
            return dp[current_index][sum1]

        # recursive call after including the number at the current_index in the first set
        diff1 = self.recursiveCanPartition(
            num, current_index + 1, sum1 + num[current_index], sum2, dp)

        # recursive call after including the number at the current_index in the second set
        diff2 = self.recursiveCanPartition(
            num, current_index + 1, sum1, sum2 + num[current_index], dp)

        # store the result in the memoization array
        dp[current_index][sum1] = min(diff1, diff2)
        return dp[current_index][sum1]

'''Bottom-up Dynamic Programming Solution:
Let’s assume S represents the total sum of all the numbers. So, in this problem,
we are trying to find a subset whose sum is as close to S/2 as possible, because if we
can partition the given set into two subsets of an equal sum, we get the minimum difference, i.e. zero.
This transforms our problem to Subset Sum, where we try to find a subset whose sum is equal to a given number-- S/2 in our case.
If we can’t find such a subset, then we will take the subset which has the sum closest to S/2.
This is easily possible, as we will be calculating all possible sums with every subset.

So what is the closest subset sum to S/2 we can find? We can find the subset if we start moving backwards
in the last row from the bottom right corner to find the first T in the memoization array. The first T indicates the closest sum to S/2.
Suppose the first T corresponds to the sum '6'. This means the other set will have a sum of '9' and the minimum difference will be '3'.
'''

# solution three using bottom-up dp
# this solution can be easily improved to use only O(s) space using two rows only in the dp array
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array and s is half the sum of all the numbers
# O(ns) space - where n represents the total number of elements in the input array and s is half the sum of all the numbers
class Solution:
    def canPartition(self, num):
        num_sum = sum(num)
        half_sum = int(num_sum / 2)
        n = len(num)
        dp = [[False for _ in range(half_sum + 1)] for _ in range(n)]

        # populate the s=0 columns, as we can always form '0' sum with an empty set
        for i in range(n):
            dp[i][0] = True

        # with only one number, we can form a subset only when
        # the required sum is equal to that number
        for j in range(1, half_sum + 1):
            dp[0][j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, half_sum + 1):
                # if we can get the sum 's' without the number at index 'i'
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif num[i] <= j:
                    # else include the number and see if we can find a subset to get remaining sum
                    dp[i][j] = dp[i - 1][j - num[i]]

        # find the largest index in the last row which is true
        # meaning that we can get a subset with a subset sum equal
        # to the value of j at that index, because j will be the
        # current value of the subset sum
        sum1, sum2 = 0, 0
        for j in range(half_sum, -1, -1):
            if dp[n - 1][j]:
                sum1 = j
                sum2 = num_sum - sum1
                break

        return abs(sum1 - sum2)

# solution four using bottom-up dp optimized version of solution three
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array and s is half the sum of all the numbers
# O(s) space - where s is half the sum of all the numbers
class Solution:
    def canPartition(self, num):
        num_sum = sum(num)
        half_sum = int(num_sum / 2)
        n = len(num)
        dp = [[False for _ in range(half_sum + 1)] for _ in range(2)]

        # populate the s=0 columns, as we can always form '0' sum with an empty set:
        dp[0][0] = dp[1][0] = True

        # with only one number, we can form a subset only when
        # the required sum is equal to that number
        for j in range(1, half_sum + 1):
            dp[0][j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, half_sum + 1):
                # if we can get the sum 's' without the number at index 'i'
                if dp[(i - 1) % 2][j]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]
                elif num[i] <= j:
                    # else include the number and see if we can find a subset to get remaining sum
                    dp[i % 2][j] = dp[(i - 1) % 2][j - num[i]]

        # find the largest index in the last row which is true
        # meaning that we can get a subset with a subset sum equal
        # to the value of j at that index, because j will be the
        # current value of the subset sum
        sum1, sum2 = 0, 0
        for j in range(half_sum, -1, -1):
            if dp[(n - 1) % 2][j]:
                sum1 = j
                sum2 = num_sum - sum1
                break

        return abs(sum1 - sum2)

# solution five using bottom-up dp optimized version of solution four
# this solution uses a single-dimensional array
# Complexity:
# O(ns) time - where n represents the total number of elements in the input array and s is half the sum of all the numbers
# O(s) space - where s is half the sum of all the numbers
class Solution:
    def canPartition(self, num):
        num_sum = sum(num)
        half_sum = int(num_sum / 2)
        n = len(num)
        dp = [False for _ in range(half_sum + 1)]

        # populate the s=0 index, as we can always form '0' sum with an empty set:
        dp[0] = True

        # with only one number, we can form a subset only when
        # the required sum is equal to that number
        for j in range(1, half_sum + 1):
            dp[j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(half_sum, -1, -1):
                if not dp[j] and num[i] <= j:
                    # include the number and see if we can find a subset to get remaining sum
                    dp[j] = dp[j - num[i]]

        # find the largest index in the array which is true
        # meaning that we can get a subset with a subset sum equal
        # to the value of j at that index, because j will be the
        # current value of the subset sum
        sum1, sum2 = 0, 0
        for j in range(half_sum, -1, -1):
            if dp[j]:
                sum1 = j
                sum2 = num_sum - sum1
                break

        return abs(sum1 - sum2)