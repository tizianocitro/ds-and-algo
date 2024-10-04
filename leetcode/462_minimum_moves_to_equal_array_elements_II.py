# !code: 462, !difficulty: medium, !from: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

'''Problem:
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.
Test cases are designed so that the answer will fit in a 32-bit integer.

Constraints:
- n == nums.length
- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element): [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Input: nums = [1,10,2,9]
Output: 16
'''

# solution one using sorting
# Complexity:
# O(nlogn) time - where n is the length of nums because of sorting
# O(1) space
class Solution:
    def minMoves2(self, nums):
        # sort the array so that we can calculate how much each number needs to move
        # relative to the other numbers to make all numbers equal
        nums.sort()

        min_moves = float('inf')
        total = sum(nums)

        # it is a running total of elements encountered so far in the loop
        sum_to_left = 0
        for i in range(len(nums)):
            # increments required to make all elements to the left of nums[i] equal to nums[i],
            # we multiply nums[i] by i because it needs to be added to i elements,
            # then subtract sum_so_far (which is the sum of all elements to the left of nums[i])
            increments_required = (nums[i] * i) - sum_to_left

            # decrements required to make all elements to the right of nums[i] equal to nums[i],
            # total - sum_so_far gives the sum of elements to the right of nums[i],
            # and we subtract the number of elements to the right multiplied by nums[i]
            sum_to_right = total - sum_to_left
            decrements_required = sum_to_right - (nums[i] * (len(nums) - i))

            # update sum_so_far to include the current element nums[i]
            sum_to_left += nums[i]

            # calculate the total moves (increments + decrements) required if we make
            # all elements equal to nums[i], then, we update min_moves to be the minimum
            # of the current min_moves and the newly calculated number of moves
            min_moves = min(min_moves, increments_required + decrements_required)

        return min_moves

# solution two using sorting and two pointers
# Complexity:
# O(nlogn) time - where n is the length of nums because of sorting
# O(1) space
class Solution:
    def minMoves2(self, nums):
        min_moves = 0

        # sort the array so that we can process the smallest and largest elements in pairs
        nums.sort()

        left, right = 0, len(nums) - 1
        while left < right:
            # calculate the difference between the largest and smallest element
            # in the current window, this is the number of moves required to make
            # nums[l] and nums[r] equal and is the minimum change that we need to
            # actually make them equal
            min_moves += nums[right] - nums[left]

            left += 1
            right -= 1

        return min_moves

# solution three using prefix sum and binary search
# Complexity:
# O(nlogn) time - where n is the length of nums because of sorting and bisect_left() in the loop
# O(n) space - for the prefix sum list
from bisect import *
from  itertools import accumulate

class Solution:
    def minMoves2(self, nums):
        min_moves = float('inf')
        queries = list(nums)

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

            min_moves = min(min_moves, increments_required + decrements_required)

        return min_moves