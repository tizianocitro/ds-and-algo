# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/unique-paths-medium

'''Problem:
Given a 2-dimensional grid of size m x n (where m is the number of rows and n is the number of columns),
you need to find out the number of unique paths from the top-left corner to the bottom-right corner.
The constraints are that you can only move either right or down at any point in time.

Constraints:
- 1 <= m, n <= 100

Input: 3, 3
Output: 6
Explanation: The six possible paths are:
    Right, Right, Down, Down
    Right, Down, Right, Down
    Right, Down, Down, Right
    Down, Right, Right, Down
    Down, Right, Down, Right
    Down, Down, Right, Right

Input: 3, 2
Output: 3
Explanation: The three possible paths are:
    Right, right, down
    Right, down, right
    Down, right, right

Input: 2, 3
Output: 3
Explanation: The three possible paths are:
    Down, right, right
    Right, down, right
    Right, right, down
'''

# solution one using dynamic programming
# Complexity:
# O(n * m) time - where m is the number of rows and n is the number of columns
# because we have to traverse all the cells in the grid
# O(n * m) space - to store the number of times each cell can be reached
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # store the number of time each cell can be reached
        # so that the result will be in the right-bottom cell
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # each cell in the first column can be reached only
        # from the cells at its top
        for row in range(m):
            dp[row][0] = 1

        # each cell in the first row can be reached only
        # from the cells at its left
        for col in range(n):
            dp[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                # each cell can be reached a number of time that is equal to the sum of
                # the number of times the cell at its left can be reached
                # and the number of times the cell at its top can be reached
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        # alternatively:
        # return dp[-1][-1]
        return dp[m - 1][n - 1]

# solution two using dfs
# Complexity:
# O(2^(n + m)) time - where m is the number of rows and n is the number of columns
# it is 2^(n + m) because at each cell we have two choices to move right or down
# and for each path we have to traverse at most n - 1 cells in a row and m - 1 cells in a column
# O(n + m) space - because of the recursion stack as we can ahve at most all the cells
# in a row and all the cells in a column in the recursion stack
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # start traversing from the top-left corner
        return self.dfs(m, n, 0, 0)

    def dfs(self, m, n, row, col):
        # if we exceed the right or bottom boundary
        # we only check those because we can only move right or down
        if row >= m or col >= n:
            return 0

        # if we reach the bottom-right corner
        # we increment the count of unique paths
        # because we have found a path to the right-bottom corner
        if row == m - 1 and col == n - 1:
            return 1

        # return the sum of unique paths from the right and bottom cell
        return self.dfs(m, n, row, col + 1) + self.dfs(m, n, row + 1, col)