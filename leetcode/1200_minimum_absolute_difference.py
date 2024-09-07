# !code: 1200, !difficulty: easy, !from: https://leetcode.com/problems/minimum-absolute-difference/

'''Problem:
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order (with respect to pairs), each pair [a, b] follows
- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr

Constraints:
- 2 <= arr.length <= 105
- -106 <= arr[i] <= 106

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
'''

# solution one using sorting
# Complexity:
# O(nlogn) time - where n is the length of the input array for sorting
# O(n) space - for the result array
class Solution:
    def minimumAbsDifference(self, arr):
        # no need to check if arr is empty because it is guaranteed to have at least 2 elements
        # sort elements in ascending order
        arr.sort()

        n = len(arr)

        # compute the minimum difference among all pairs
        # there is also a one-liner for this using the min function
        # min_diff = min(arr[i] - arr[i - 1] for i in range(1, n))
        min_diff = float('inf')
        for i in range(1, n):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        # find all pairs with minimum difference
        # we are calculating the difference between adjacent elements again
        # after having already calculated them in the previous loop, so
        # we could have stored them in a list and used them here since
        # we already need O(n) space for the result array
        # there is also a one-liner for this using list comprehension
        # result = [[arr[i - 1], arr[i]] for i in range(1, n) if arr[i] - arr[i - 1] == min_diff]
        result = []
        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result