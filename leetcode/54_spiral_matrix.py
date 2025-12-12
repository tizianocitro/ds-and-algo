# !code: 54, !difficulty: medium, !from: https://leetcode.com/problems/spiral-matrix

'''Problem:
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
'''

# solution one with directions moving clockwise
# Complexity:
# O(n*m) time - where n is the number of rows and m is the number of columns
# O(n*m) space - to store the visited elements
class Solution:
    def __init__(self):
        #            right,   down,   left,    up
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def spiralOrder(self, matrix):
        # this will store the result so it will take O(n*m) space
        res = []

        # start going right (0)
        self.dfs(matrix, 0, 0, res, 0)

        return res

    # returning False means we cannot proceed in the current direction
    # so we need to change the direction to next clockwise direction
    def dfs(self, matrix, row, col, res, dir):
        # if we are out of bounds
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return False

        # do not visit if we have already visited
        if matrix[row][col] == float('inf'):
            return False

        # append the current element to the result and mark it as visited
        res.append(matrix[row][col])
        matrix[row][col] = float('inf')

        # try to go in the same direction, otherwise change the direction
        # until you find a valid direction or all directions are tried
        tried = 0
        while tried < len(self.dirs):
            out = self.dfs(matrix, row + self.dirs[dir][0], col + self.dirs[dir][1], res, dir)
            if out:
                break
            # change the direction to next clockwise direction
            # remaining directions are (1, 2, 3) for dir = 0
            # for 3, we have (0, 1, 2), so if dir = 3, we need to change it back to 0
            dir = (dir + 1) % len(self.dirs)
            tried += 1

        return True

# solution two using fixed directions
# Complexity:
# O(n*m) time - where n is the number of rows and m is the number of columns
# O(n*m) space - to store the result
class Solution:
    def spiralOrder(self, matrix):
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            # increment top to exclude the top row (the row we just visited)
            top += 1

            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            # decrement right to exclude the right col (the col we just visited)
            right -= 1

            # check if we have already visited all the rows or cols
            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            # decrement bottom to exclude the bottom row (the row we just visited)
            bottom -= 1

            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            # increment left to exclude the left col (the col we just visited)
            left += 1

        return res