# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638c9a7688f1e1c16f41bb3c

'''Problem:
You are given a 2D matrix containing different characters, you need to find if there exists any cycle consisting of the same character in the matrix.
A cycle is a path in the matrix that starts and ends at the same cell and has four or more cells.
From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same character value of the current cell.

Write a function to find if the matrix has a cycle.

Input: [["a", "a", "a", "a"], ["b", "a", "c", "a"], ["b", "a", "c", "a"], ["b", "a", "a", "a"]]
Output: True
'''

# solution one using dfs
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that, in the worst case, we have to traverse the whole matrix to find the islands.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with the same char.
# and for the visited matrix, we have to store the visited status of each cell in the matrix.
class Solution:
    def hasCycle(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False for i in range(cols)] for j in range(rows)]

        for row in range(rows):
            for col in range(cols):
                # only if the cell is not visited
                if not visited[row][col]:
                    if self.dfs(matrix, row, col, (-1, -1), matrix[row][col], visited):
                        # a cycle has been found
                        return True

        return False

    def dfs(self, matrix, row, col, parent, char, visited):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return False

        # different character which means a different island
        if matrix[row][col] != char:
            return False

        if visited[row][col]:
            # found a cycle, as we are visiting an already visited valid cell
            return True

        # mark the cell visited
        visited[row][col] = True

        parent_row, parent_col = parent
        has_cycle = False

        # recursively visit all neighboring cells (horizontally & vertically)
        # however, we have to avoid visiting the parent again, so we have to check
        # that the changing row or col does not make the pair (row, col) == (parent_row, parent_col)
        # we have to check onlt for the changing one because
        # the other one will always be equal to the one of the parent
        if row - 1 != parent_row:
            has_cycle |= self.dfs(matrix, row - 1, col, (row, col), char, visited)
        if row + 1 != parent_row:
            has_cycle |= self.dfs(matrix, row + 1, col, (row, col), char, visited)
        if col - 1 != parent_col:
            has_cycle |= self.dfs(matrix, row, col - 1, (row, col), char, visited)
        if col + 1 != parent_col:
            has_cycle |= self.dfs(matrix, row, col + 1, (row, col), char, visited)

        return has_cycle
