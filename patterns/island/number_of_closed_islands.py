# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638c7f5bb2790984e1934f98

'''Problem:
You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
Each cell is considered connected to other cells horizontally or vertically (not diagonally).

A closed island is an island that is totally surrounded by 0s (i.e., water).
This means all horizontally and vertically connected cells of a closed island are water.
This also means that, by definition, a closed island can't touch an edge (as then the edge cells are not connected to any water cell).

Write a function to find the number of closed islands in the given matrix.

Input: [[1,1,0,0,0],[0,1,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[0,0,0,0,0]]
Output: 1
'''

# solution one using dfs with number of edges
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with 1s.
class Solution:
    def countClosedIslands(self, matrix):
        count_closed_islands = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # start dfs from each land cell
                if matrix[row][col] == 1:
                    edges = self.dfs(matrix, row, col)

                    # increment count if island is closed, meaning we found no edges
                    if edges < 1:
                        count_closed_islands += 1

        return count_closed_islands

    def dfs(self, matrix, row, col):
        # if we are out of bounds, return 1 because we found an edge
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return 1

        # if we find a water cell, return 0 because it is not an edge
        if matrix[row][col] == 0:
            return 0

        # mark cell as visited
        matrix[row][col] = 0

        # each cell starts with 0 edges
        edges = 0

        # recursively check all neighbors add add their edges to the total of this cell's edges
        edges += self.dfs(matrix, row - 1, col)
        edges += self.dfs(matrix, row + 1, col)
        edges += self.dfs(matrix, row, col - 1)
        edges += self.dfs(matrix, row, col + 1)

        return edges

# solution two using dfs but boolean instead of number of edges
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with 1s.
class Solution:
    def countClosedIslands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        count_closed_islands = 0

        for i in range(rows):
            for j in range(cols):
                # only if the cell is a land and not visited
                if matrix[i][j] == 1:
                    if self.dfs(matrix, i, j):
                        count_closed_islands += 1

        return count_closed_islands

    def dfs(self, matrix, x,  y):
        # returning false since the island is touching an edge
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return False
        
        # returning true as the island is surrounded by water
        if matrix[x][y] == 0:
            return True

        # mark the cell visited
        matrix[x][y] = 0

        is_closed = True

        # recursively visit all neighboring cells (horizontally & vertically)
        is_closed &= self.dfs(matrix, x + 1, y)
        is_closed &= self.dfs(matrix, x - 1, y)
        is_closed &= self.dfs(matrix, x, y + 1)
        is_closed &= self.dfs(matrix, x, y - 1)

        return is_closed

# solution thee using dfs but boolean instead of number of edges with visited matrix
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with 1s.
class Solution:
    def countClosedIslands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        count_closed_islands = 0

        for i in range(rows):
            for j in range(cols):
                # only if the cell is a land and not visited
                if matrix[i][j] == 1 and not visited[i][j]:
                    if self.dfs(matrix, visited, i, j):
                        count_closed_islands += 1

        return count_closed_islands

    def dfs(self, matrix, visited, x,  y):
        # returning false since the island is touching an edge
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return False
        
        # returning true as the island is surrounded by water
        if matrix[x][y] == 0 or visited[x][y]:
            return True

        # mark the cell visited
        visited[x][y] = True

        is_closed = True

        # recursively visit all neighboring cells (horizontally & vertically)
        is_closed &= self.dfs(matrix, visited, x + 1, y)
        is_closed &= self.dfs(matrix, visited, x - 1, y)
        is_closed &= self.dfs(matrix, visited, x, y + 1)
        is_closed &= self.dfs(matrix, visited, x, y - 1)

        return is_closed

