# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dc978916c4e8a379f59942

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
# O(2^n) time - where n represents the total number of elements in the input array
# O(n) space - this space will be used to store the recursion stack (dfs-fashion)
class Solution:
    def findTargetSubsets(self, num, s):
        # if the sum of the numbers is less than the target sum,
        # it is not possible to find a subset with the target sum
        total = sum(num)
        if total < s:
            return 0

        return self.recursiveFindTargetSubsets(num, s, 0, 0)

    def recursiveFindTargetSubsets(self, num, s, target, current_index):
        # base check, a new subset with sum equals to s was found
        # we need the subset to be of length equal to the input array
        # because all the numbers in the input array need to be part of the subset
        if current_index == len(num) and target == s:
            return 1

        # if we have reached the end of the array but the target sum is not reached
        if current_index >= len(num):
            return 0

        # recursive call after choosing the number at the current_index with +
        count1 = self.recursiveFindTargetSubsets(
            num, s, target + num[current_index], current_index + 1)

        # recursive call after choosing the number at the current_index with -
        count2 = self.recursiveFindTargetSubsets(
            num, s, target - num[current_index], current_index + 1)

        # return the sum of the number of subsets with target sum from both recursive calls
        return count1 + count2

'''Solution:
The problem can be converted into Count of Subset Sum.

We are asked to find two subsets of the given numbers whose difference is equal to the given target S.
Take the example {1, 1, 2, 3}, S=4. One solution is {+1-1-2+3}. One subset is made of the numbers that need to have assigned '+',
while the other subset contains the numbers that need to have the '-' sign.
So, the two subsets we are asked to find are {1, 3} & {1, 2} because:
    (1 + 3) - (1 + 2 ) = 1

Now, suppose 'Sum(s1)' denotes the total sum of set 's1', and 'Sum(s2)' denotes the total sum of set 's2'. 
So the required equation is:
    Sum(s1) - Sum(s2) = S

This equation can be reduced to the subset sum problem. Let’s assume that 'Sum(num)' denotes the total sum of all the numbers, therefore:
    Sum(s1) + Sum(s2) = Sum(num)

Let’s add the above two equations:
    => Sum(s1) - Sum(s2) + Sum(s1) + Sum(s2) = S + Sum(num)
    => 2 * Sum(s1) =  S + Sum(num)
    => Sum(s1) = (S + Sum(num)) / 2

Which means that one of the sets, 's1', has a sum equal to (S + Sum(num)) / 2.
This essentially converts our problem to:
    "Find the count of subsets of the given numbers whose sum is equal to (S + Sum(num)) / 2."
'''

# solution two using bottom-up dp
# Complexity:
# O(ns)) time - where n represents the total number of elements in the input array and s is the desired sum
# O(ns) space - this space will be used for the dp array
class Solution:
    def findTargetSubsets(self, num, s):
        total = sum(num)

        # if s + total is odd, we cannot find a subset
        # with the sum equal to (s + total) / 2
        # in the same way, if total < s, we cannot find a subset
        if total < s or (s + total) % 2 == 1:
            return 0

        target = (s + total) // 2
        return self.count_subsets(num, target)

    def count_subsets(self, num, s):
        n = len(num)
        dp = [[0 for _ in range(s + 1)] for _ in range(n)]

        # populate the sum = 0 columns, as we will always have an empty set for zero sum
        for i in range(0, n):
            dp[i][0] = 1

        # with only one number, we can form a subset only
        # when the required sum is equal to the number
        for s in range(1, s + 1):
            dp[0][s] = 1 if num[0] == s else 0

        # process all subsets for all sums
        for i in range(1, n):
            for s in range(1, s + 1):
                dp[i][s] = dp[i - 1][s]
                if s >= num[i]:
                    dp[i][s] += dp[i - 1][s - num[i]]

        # the bottom-right corner will have our answer
        return dp[n - 1][s]

# solution three using bottom-up dp optimized version of solution two
# Complexity:
# O(ns)) time - where n represents the total number of elements in the input array and s is the desired sum
# O(s) space - this space will be used for the dp array
class Solution:
    def findTargetSubsets(self, num, s):
        total = sum(num)

        # if s + total is odd, we cannot find a subset
        # with the sum equal to (s + total) / 2
        # in the same way, if total < s, we cannot find a subset
        if total < s or (s + total) % 2 == 1:
            return 0

        target = (s + total) // 2
        return self.count_subsets(num, target)    

    def count_subsets(self, num, s):
        n = len(num)
        dp = [0 for _ in range(s + 1)]
        dp[0] = 1

        # with only one number, we can form a subset only
        # when the required sum is equal to the number
        for j in range(1, s + 1):
            dp[j] = 1 if num[0] == j else 0

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(s, -1, -1):
                if j >= num[i]:
                    dp[j] += dp[j - num[i]]

        return dp[s]