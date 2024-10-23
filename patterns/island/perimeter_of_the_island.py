# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638c857a34bb69a286c79f30

'''Problem:
You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
Each cell is considered connected to other cells horizontally or vertically (not diagonally).

There are no lakes on the island, so the water inside the island is not connected to the water around it.
A cell is a square with a side length of 1..

The given matrix has only one island, write a function to find the perimeter of that island.

Input: [[1,1,0,0,0], [0,1,0,0,0], [0,1,0,0,0], [0,1,1,0,0], [0,0,0,0,0]]
Output: 14
'''

# solution using dfs
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with 1s
# and the visited matrix thath has the same dimensions as the matrix.
class Solution:
    def findIslandPerimeter(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # we need the visited array because if we were to set the cell value as 0
        # to mark it as visited, then the neighbors would see it as water
        # and count it again in the borders
        visited = [[False for i in range(cols)] for j in range(rows)]

        # searching the starting cell because the given matrix has only one island
        for row in range(rows):
            for col in range(cols):
                # if we find a 1, we have found the starting cell, our first land
                if matrix[row][col] == 1:
                    return self.dfs(matrix, row, col, visited)

        return 0

    def dfs(self, matrix, row, col, visited):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return 1

        if matrix[row][col] == 0:
            return 1

        # we can do that after the previous if because we mark as visisted only cells
        # that have a value of 1, so they are lands
        if visited[row][col]:
            return 0

        visited[row][col] = True

        borders = 0

        borders += self.dfs(matrix, row - 1, col, visited)
        borders += self.dfs(matrix, row + 1, col, visited)
        borders += self.dfs(matrix, row, col - 1, visited)
        borders += self.dfs(matrix, row, col + 1, visited)

        return borders

