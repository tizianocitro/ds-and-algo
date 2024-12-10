# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6388d8940cc1849dcbc27fe3

'''Problem:
Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it.
Write a function to return the area of the biggest island. 

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
Each cell is considered connected to other cells horizontally or vertically (not diagonally).

Input: [[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]
Output: 5
'''

# solution one using bfs
# Complexity:
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(min(n, m)) space - where n is the number of lines and m is the number of columns
# BFS queue can go up to min(n, m) when the whole matrix is filled with 1s.
from collections import deque

class Solution:
    def maxAreaOfIsland(self, matrix):
        biggest_ssland_area = 0
        rows = len(matrix)
        if rows < 1:
            return biggest_ssland_area
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                # only if the cell is a land we proceed with bfs
                if matrix[row][col] == 1:
                    island_area = self.bfs(row, col, matrix)
                    biggest_ssland_area = max(biggest_ssland_area, island_area)

        return biggest_ssland_area

    def bfs(self, x, y, matrix):
        island_area = 0
        neighbors = deque()
        neighbors.extend([(x, y)])

        while neighbors:
            row, col = neighbors.popleft()
            
            # skip, if it is not a valid cell
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                continue

            # skip, if it is a water, not island, cell
            if matrix[row][col] == 0:
                continue
            
            # mark cell as visited
            matrix[row][col] = 0

            # counting the current cell
            island_area += 1

            # add all neighboring cells (horizontally & vertically) to visit them
            neighbors.extend([(row - 1, col)])
            neighbors.extend([(row + 1, col)])
            neighbors.extend([(row, col - 1)])
            neighbors.extend([(row, col + 1)])

        return island_area

# solution one using bfs with append instead of extend
# Complexity:
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(min(n, m)) space - where n is the number of lines and m is the number of columns
# BFS queue can go up to min(n, m) when the whole matrix is filled with 1s.
from collections import deque

class Solution:
    def maxAreaOfIsland(self, matrix):
        biggestIslandArea = 0
        rows = len(matrix)
        if rows < 1:
            return biggestIslandArea
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    island_area = self.bfs(row, col, matrix)
                    biggestIslandArea = max(biggestIslandArea, island_area)

        return biggestIslandArea

    def bfs(self, row, col, matrix):
        island_area = 0
        neighbors = deque()
        neighbors.append((row, col))

        while neighbors:
            r, c = neighbors.popleft()
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                continue
            if matrix[r][c] == 0:
                continue

            matrix[r][c] = 0
            island_area += 1

            neighbors.append((r - 1, c))
            neighbors.append((r + 1, c))
            neighbors.append((r, c - 1))
            neighbors.append((r, c + 1))

        return island_area

# solution one using dfs
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with 1s.
class Solution:
    def maxAreaOfIsland(self, matrix):
        biggestIslandArea = 0
        rows = len(matrix)
        if rows < 1:
            return biggestIslandArea
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                # only if the cell is a land we proceed with dfs
                if matrix[row][col] == 1:
                    island_area = self.dfs(row, col, matrix)
                    biggestIslandArea = max(biggestIslandArea, island_area)

        return biggestIslandArea

    def dfs(self, row, col, matrix):
        # return, if it is not a valid cell
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return 0
        
        # return, if it is a water, not island, cell
        if matrix[row][col] == 0:
            return 0

        # mark cell as visited
        matrix[row][col] = 0

        # counting the current cell
        island_area = 1

        # recursively visit all neighboring cells (horizontally & vertically)
        island_area += self.dfs(row - 1, col, matrix)
        island_area += self.dfs(row + 1, col, matrix)
        island_area += self.dfs(row, col - 1, matrix)
        island_area += self.dfs(row, col + 1, matrix)

        return island_area