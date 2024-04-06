# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6388cbb0765bb2154037ce84

'''Problem:
Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it.
Write a function to return the area of the biggest island. 

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
Each cell is considered connected to other cells horizontally or vertically (not diagonally).

Input: [[0, 1, 1, 1, 0],[0, 0, 0, 1, 1],[0, 1, 1, 1, 0],[0, 1, 1, 0, 0],[0, 0, 0, 0, 0]]
Output: 1

Input: [[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
Output: 3

Input: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Output: 0
'''

# solution one using dfs
# Complexity:
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with 1s.
class Solution:
    def countIslands(self, matrix):
        totalIslands = 0
        rows = len(matrix)
        if rows < 1:
            return matrix
        cols = len(matrix[0])

        # traverse the matrix
        for row in range(rows):
            for col in range(cols):
                # if we find an island, we start a dfs to visit all the neighbors
                # we find an island when we find a cell with a vale of 1
                if matrix[row][col] == 1:
                    self.dfs(row, col, matrix)
                    totalIslands += 1

        return totalIslands

    def dfs(self, row, col, matrix):
        # check for borders of the matrix, to ensure we don't go out of bounds
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return

        # check if the current cell has already been visited
        if matrix[row][col] == 0:
            return

        # mark the current cell as visited
        matrix[row][col] = 0

        # visit all the neighbors
        self.dfs(row + 1, col, matrix)
        self.dfs(row - 1, col, matrix)
        self.dfs(row, col + 1, matrix)
        self.dfs(row, col - 1, matrix)

# solution two using bfs
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(min(n, m)) space - where n is the number of lines and m is the number of columns
# BFS queue can go up to min(n, m) when the whole matrix is filled with 1s.
from collections import deque

class Solution:
    def countIslands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0

        for i in range(rows):
            for j in range(cols):
                if (matrix[i][j] == 1):
                    self.bfs(matrix, i, j)
                    totalIslands += 1
        return totalIslands

    def bfs(self, matrix,  x,  y):
        neighbors = deque([(x, y)])

        while neighbors:
            row, col = neighbors.popleft()

            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                continue
            if matrix[row][col] == 0:
                continue

            # mark the cell as visited
            matrix[row][col] = 0

            # insert all neighboring cells to the queue for BFS
            neighbors.extend([(row + 1, col)])
            neighbors.extend([(row - 1, col)])
            neighbors.extend([(row, col + 1)])
            neighbors.extend([(row, col - 1)])

# solution three using bfs with visisted matrix
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# We need to keep track of the visited cells in the matrix, so we need an additional matrix to store this information.
from collections import deque

class Solution:
    def count_is_lands_BFS(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0
        visited = [[False for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if (matrix[i][j] == 1 and not visited[i][j]):
                    totalIslands += 1
                    self.bfs(matrix, visited, i, j)
        return totalIslands

    def bfs(self, matrix, visited, x,  y):
        neighbors = deque([(x, y)])

        while neighbors:
            row, col = neighbors.popleft()

            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                continue
            if matrix[row][col] == 0 or visited[row][col]:
                continue\

            visited[row][col] = True

            neighbors.extend([(row + 1, col)])
            neighbors.extend([(row - 1, col)])
            neighbors.extend([(row, col + 1)])
            neighbors.extend([(row, col - 1)])
