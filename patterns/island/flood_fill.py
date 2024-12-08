# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6388e8887b259e5c9e8c0274

'''Problem:
Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of the image.

Flood fill algorithm takes a starting cell (i.e., a pixel) and a color.
The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell.
Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell.

Given a matrix, a starting cell, and a color, flood fill the matrix.

Input:
    matrix = [[0,1,1,1,0], [0,0,0,1,1], [0,1,1,1,0], [0,1,1,0,0], [0,0,0,0,0]]
    starting cell = (1, 3)
    new color = 2
Output: [[0,2,2,2,0], [0,0,0,2,2], [0,2,2,2,0], [0,2,2,0,0], [0,0,0,0,0]]
'''

# solution one using dfs
# O(n * m) time - where n is the number of lines and m is the number of columns
# This is due to the fact that, in the worst case, we might have to fill the whole matrix.
# O(n * m) space - where n is the number of lines and m is the number of columns
# DFS recursion stack can go n * m deep when the whole matrix is filled with the same color as the start cell.
class Solution:
    def floodFill(self, matrix, x, y, new_color):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return matrix

        cell_val = matrix[x][y]
        self.dfs(matrix, x, y, cell_val, new_color)

        return matrix

    def dfs(self, matrix, x, y, cell_val, new_color):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return matrix

        if matrix[x][y] != cell_val:
            return matrix

        matrix[x][y] = new_color

        self.dfs(matrix, x - 1, y, cell_val, new_color)
        self.dfs(matrix, x + 1, y, cell_val, new_color)
        self.dfs(matrix, x, y - 1, cell_val, new_color)
        self.dfs(matrix, x, y + 1, cell_val, new_color)
