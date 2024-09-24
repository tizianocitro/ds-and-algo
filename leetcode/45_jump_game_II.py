# !code: 45, !difficulty: medium, !from: https://leetcode.com/problems/jump-game-ii/

'''Problem:
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].

Constraints:
- 1 <= nums.length <= 104
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1]

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [2,3,0,1,4]
Output: 2
'''

# solution one using greedy algorithm (monodimensional bfs-like approach)
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(1) space
class Solution:
    # nums indicates the number of jumps we can make from each position
    # nums[i] is the number of jumps we can make from i-th position
    def jump(self, nums) -> int:
        # the total number of jumps needed to reach the last index
        jumps = 0

        # the window in the array that represents the current bfs level,
        # at each iteration we will process one bfs level
        start = end = 0
        while end < len(nums) - 1:
            # farthest is the farthest index we can reach from
            # any of the position in the current window
            farthest = 0
            for i in range(start, end + 1):
                # nums[i] is the number of jumps we can make from i-th position
                farthest = max(farthest, i + nums[i])

            # we move the start of the window to the end of the current window + 1
            # because it is from that position that the next bfs level will start
            start = end + 1

            # end will be the farthest index we can reach from any of the positions
            # in the current window and will be the end of the next bfs level
            end = farthest

            # increase the number of jumps every level we go down
            jumps += 1

        return jumps
