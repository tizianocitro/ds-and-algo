# !code: 55, !difficulty: medium, !from: https://leetcode.com/problems/jump-game/

'''Problem:
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Constraints:
- 1 <= nums.length <= 104
- 0 <= nums[i] <= 105

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''

# solution one using a greedy approach
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(1) space - we only use a variable to store the available jumps
class Solution:
    def canJump(self, nums) -> bool:
        # for less than 2 elements, it is always possible to reach the end
        n = len(nums)
        if n <= 1:
            return True

        # start with the available jumps from the first position
        available_jumps = nums[0]

        for i in range(1, n):
            # if at each position we have 0 available jumps, we cannot reach the end
            # this can happen if we have a 0 in the middle of the array and we can't jump over it
            # or if we start with 0 available jumps (when the first position has 0 jumps)
            if available_jumps < 1:
                return False

            # if we can reach the last index, return True, this is just to save
            # some computation time because the solution works also without this check
            if available_jumps >= n - 1:
                return True

            # available_jumps is the maximum number of jumps we can make from the current position
            # either the available_jumps from the previous position - 1 (because we used one jump to
            # arrive at the current position) or the number of jumps at the current position
            available_jumps = max(available_jumps - 1, nums[i])

        # if we reach the end, return True
        return True

# solution two using bottom-up dynamic programming
# Complexity:
# O(nk) time - where n is the number of elements in the array and k is the longest jump we can make
# we iterate through all the n positions and for each position we iterate through
# at most k next positions, where k is the longest jump we can make
# O(n) space - we use an array of size n to indicate all the reachable positions
class Solution:
    def canJump(self, nums) -> bool:
        # for less than 2 elements, it is always possible to reach the end
        n = len(nums)
        if n <= 1:
            return True

        # can be removed because it is handled by the loop
        # if the first position is 0, than starting from the next position
        # the 'if not dp[i]:' will always be True, so we will always 'continue'
        # until the last position where we will leave False as value
        # if nums[0] == 0:
        #     return False

        # set all positions to False, except the first one which is always reachable
        dp = [False for _ in range(n)]
        dp[0] = True

        for i in range(n):
            # if the position is not reachable, skip it
            if not dp[i]:
                continue

            # this can be removed because if the prev number
            # has at least 1 jump, then this has already
            # been marked as reachable, so dp[i] == True already
            # dp[i] = dp[i] or dp[i - 1] > 0

            # calculate all the next reachable positions
            # and if the last position (or beyond) is reachable, return True
            jump_ix = i + nums[i]
            if jump_ix >= n - 1:
                return True

            # otherwise, mark all the positions as reachable
            # i + 1 because this position is already reachable,
            # otherwise we would have skipped it
            for j in range(i + 1, jump_ix + 1):
                dp[j] = True

        # the result is in the last position, but it will always be False
        # otherwise we would have returned True in the loop
        return False

# solution three using bottom-up dynamic programming (just some minor changes from solution two but it is the same)
# Complexity:
# O(nk) time - where n is the number of elements in the array and k is the longest jump we can make
# we iterate through all the n positions and for each position we iterate through
# at most k next positions, where k is the longest jump we can make
# O(n) space - we use an array of size n to indicate all the reachable positions
class Solution:
    def canJump(self, nums) -> bool:
        # for less than 2 elements, it is always possible to reach the end
        n = len(nums)
        if n <= 1:
            return True

        # set all positions to False, except the first one which is always reachable
        dp = [False for _ in range(n)]
        dp[0] = True

        for i in range(n):
            # if the position is not reachable, skip it
            if not dp[i]:
                continue

            # calculate all the next reachable positions and mark all of them as reachable
            jump_ix = i + nums[i]
            # i + 1 because this position is already reachable,
            # otherwise we would have skipped it
            for j in range(i + 1, min(jump_ix + 1, n)):
                dp[j] = True

        # in this case we cannot return True in the loop if we reach
        # the last position, so the result is in the last position
        return dp[n - 1]