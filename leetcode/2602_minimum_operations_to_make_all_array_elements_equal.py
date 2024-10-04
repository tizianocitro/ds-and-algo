# !code: 2602, !difficulty: medium, !from: https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

'''Problem:
You are given an array nums consisting of positive integers.

You are also given an integer array queries of size m. For the ith query, you want to make all of the elements of nums equal to queries[i].
You can perform the following operation on the array any number of times:
- Increase or decrease an element of the array by 1.

Return an array answer of size m where answer[i] is the minimum number of operations to make all elements of nums equal to queries[i].

Note that after each query the array is reset to its original state.

Input: nums = [3,1,6,8], queries = [1,5]
Output: [14,10]
Explanation:
    For the first query we can do the following operations:
    - Decrease nums[0] 2 times, so that nums = [1,1,6,8].
    - Decrease nums[2] 5 times, so that nums = [1,1,1,8].
    - Decrease nums[3] 7 times, so that nums = [1,1,1,1].
    So the total number of operations for the first query is 2 + 5 + 7 = 14.
    For the second query we can do the following operations:
    - Increase nums[0] 2 times, so that nums = [5,1,6,8].
    - Increase nums[1] 4 times, so that nums = [5,5,6,8].
    - Decrease nums[2] 1 time, so that nums = [5,5,5,8].
    - Decrease nums[3] 3 times, so that nums = [5,5,5,5].
    So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.

Input: nums = [2,9,6,3], queries = [10]
Output: [20]
Explanation: We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20.
'''

# solution one using prefix sum and binary search
# Complexity:
# O(nlogn + mlogn) time - where n is the length of nums and m is the length of queries
# nlogn is for sorting nums and mlogn is for binary search in the query loop
# O(n) space - for the prefix sum list and the answer list
from bisect import *
from  itertools import accumulate

class Solution:
    def minOperations(self, nums, queries):
        answer = []

        # sort for binary search using bisect_left()
        nums.sort()

        # prefix sum for calculating the number of increments and decrements required
        # the initial=0 handles the case where the query would be added in position i=0
        # so the prefix sum would be 0, and the number of elements less than the query would be 0
        # also because we access prefix[n] which would be out of bounds if not for the 0 added at the start
        prefix = list(accumulate(nums, initial=0))

        n = len(nums)
        for query in queries:
            # find the index where the query would be inserted,
            # so i indicates the number of elements less than the query
            # consequently, n - i indicates the number of elements greater than the query
            i = bisect_left(nums, query)

            # if there are i numbers in nums that are smaller than query, you need to find
            # 'query * i - sum(i numbers smaller than query)' to find increments required in nums
            # sum(i numbers smaller than query) = prefix[i]
            increments_required = (i * query) - prefix[i]

            # If there are (n - i) numbers in nums that are greater than query, you need to find
            # sum(n - i numbers larger than query) - ((n - i) * query) to find decrements required in nums
            # sum(n - i numbers larger than query) = prefix[n] - prefix[i]
            decrements_required = (prefix[n] - prefix[i]) - ((n - i) * query)

            # the sum of increments and decrements is the total number of operations required
            answer.append(increments_required + decrements_required)

        return answer
