# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638c920fa19edaace544c805

'''Problem:
You are given a 2D matrix containing only 1s (land) and 0s (water).
An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).
Two islands are considered the same if and only if they can be translated (not rotated or reflected) to equal each other.

Write a function to find the number of distinct islands in the given matrix.

Input: [[1,1,0,1,1], [1,1,0,1,1], [0,0,0,0,0], [0,1,1,0,1], [0,1,1,0,1]]
Output: 2
'''

# solution one using positions as encoding of islands
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with 1s.
class Solution:
    def findDistinctIslandsDFS(self, matrix):
        distinct_islands = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    # start dfs from the current cell, which is the first of land, and encode the island
                    island = self.dfs(matrix, row, col, row, col)
                    distinct_islands.add(island)

        return len(distinct_islands)

    def dfs(self, matrix, row, col, start_row, start_col):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return ''

        if matrix[row][col] == 0:
            return ''

        matrix[row][col] = 0

        # encode the cell position relative to the starting cell
        island = str(row - start_row)
        island += str(col - start_col)

        island += self.dfs(matrix, row - 1, col, start_row, start_col)
        island += self.dfs(matrix, row + 1, col, start_row, start_col)
        island += self.dfs(matrix, row, col - 1, start_row, start_col)
        island += self.dfs(matrix, row, col + 1, start_row, start_col)

        return island

# solution two using directions as encoding of islands
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with 1s.
class Solution:
    def findDistinctIslandsDFS(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        islandsSet = set()

        for i in range(rows):
            for j in range(cols):
                # only if the cell is a land and not visited
                if (matrix[i][j] == 1 and not visited[i][j]):
                    # O -> origin
                    traversal = self.dfs(matrix, visited, i, j, 'O');
                    islandsSet.add(traversal)

        return len(islandsSet)

    def dfs(self, matrix, visited, x, y, direction):
        if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
            return ''

        if (matrix[x][y] == 0 or visited[x][y]):
            return ''

        visited[x][y] = True

        islandTraversal = direction

        # recursively visit all neighboring cells (horizontally & vertically)
        islandTraversal += self.dfs(matrix, visited, x + 1, y, 'D') # D -> down
        islandTraversal += self.dfs(matrix, visited, x - 1, y, 'U') # U -> up
        islandTraversal += self.dfs(matrix, visited, x, y + 1, 'R') # R -> right
        islandTraversal += self.dfs(matrix, visited, x, y - 1, 'L') # L -> left

        # B -> back
        islandTraversal += 'B'

        return islandTraversal