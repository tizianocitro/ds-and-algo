# !code: 994, !difficulty: medium, !from: https://leetcode.com/problems/rotting-oranges/

'''Problem:
You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell
- 1 representing a fresh orange
- 2 representing a rotten orange
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

# solution one using multi-source bfs
# Complexity:
# O(n * m) time - where n is the number of lines and m is the number of columns
# O(n * m) space - where n is the number of lines and m is the number of columns
# the queue will go up to n * m when the whole matrix is filled with rotten oranges
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])

        q = deque()

        # fresh: number of fresh oranges in the grid
        # time: number of minutes passed
        fresh = time = 0

        # add rotten oranges to the queue and count fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        #             right   left     down    up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # while there are rotten oranges in the queue
        # and there are fresh oranges in the grid
        while q and fresh > 0:
            # visit all the rotten oranges in the queue (a minute passes)
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()

                # visit all the neighbors
                for dr, dc in directions:
                    # calculate the neighbor position:
                    # row = neighbor row, col = neighbor column
                    row, col = r + dr, c + dc

                    if row < 0 or row >= rows or col < 0 or col >= cols:
                        continue

                    # if the neighbor is not a fresh orange, we skip it
                    if grid[row][col] != 1:
                        continue

                    # mark the neighbor as rotten
                    grid[row][col] = 2
                    # add the neighbor to the queue
                    q.append((row, col))
                    # decrease the number of fresh oranges
                    fresh -= 1

            # a minute passes for each level we visit
            time += 1

        # if all the fresh oranges have been rotten, we return the time
        # otherwise, it is impossible to rot all the fresh oranges
        return time if fresh == 0 else -1