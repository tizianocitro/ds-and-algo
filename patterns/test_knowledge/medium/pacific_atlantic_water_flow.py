# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/pacific-atlantic-water-flow-medium

'''Problem:
You are given a matrix grid of size m x n, where each matrix[i][j] represents the height of the Island at ith row and jth column position from the sea level.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

Due to heavy rain, there is a lot of water on each cell of the island. It is given that the rain water can flow to neighboring cells directly north, south,
east, and west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list result, where result[i] = [ri, ci] represents that rainwater can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Input: matrix = [
    [1,2,2,3],
    [3,2,3,4],
    [2,4,5,3],
    [5,7,1,4],
]
Output: [[0, 3], [1, 3], [2, 2], [3, 0], [3, 1]]
Explanation: The cells that can flow to both the Pacific and Atlantic oceans are [[0, 3], [1, 3], [2, 2], [3, 0], [3, 1]]
[0,3]:
    [0, 3] -> Pacific Ocean.
    [0, 3] -> Atlantic Ocean.
[1,3]:
    [1, 3] -> [0, 3] -> Pacific Ocean.
    [1, 3] -> Atlantic Ocean.
[2, 2]:
    [2, 2] -> [1, 2] -> [0, 2] -> Pacific Ocean.
    [2, 2] -> [2, 3] -> Atlantic Ocean.
[3,0]:
    [3, 0] -> Pacific Ocean.
    [3, 0] -> Atlantic Ocean.
[3,1]:
    [3, 1] -> [3, 0] -> Pacific Ocean.
    [3, 1] -> Atlantic Ocean.

Input: matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
Output: [[0,2],[1,2],[2,0],[2,1],[2,2]]
Explanation: The cells that can flow to both the Pacific and Atlantic oceans are
[0,2]:
    [0, 2] -> Pacific Ocean.
    [0, 2] -> Atlantic Ocean.
[1,2]:
    [1,2] -> [0,2] -> Pacific Ocean.
    [1,2] -> Atlantic Ocean.
[2,0]:
    [2, 0] -> Pacific Ocean.
    [2, 0] -> Atlantic Ocean.
[2,1]:
    [2,1] -> [1,1] -> [1, 0] -> Pacific Ocean.
    [2,1] -> Atlantic Ocean.
[2,2]:
    [2, 2] -> Pacific Ocean.
    [2, 2] -> Atlantic Ocean.

Input: matrix = [
    [10,10,10],
    [10,1,10],
    [10,10,10],
]
Output: [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
Explanation: The water can flow to both oceans from all cells except from the central cell [1,1].
'''

'''Solution:
The idea is to find all the internal cells that can be reached from the cell that are near the oceans.
If a cell can be reached from both the pacific and atlantic oceans, then it can flow to both oceans.
So, if a cell can be reached from at least one cell that is near the pacific ocean and at least
one cell that is near the atlantic ocean, then it can flow to both oceans.
'''

# solution three
# Complexity:
# O((m + n) * m * n) time - where m is the number of rows and n is the number of columns
# O((m + n) * m * n) space - where m is the number of rows and n is the number of columns
class Solution:
    def __init__(self):
        # define the directions for north, east, south, and west
        self.DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def pacificAtlantic(self, matrix):
        # check if the matrix is empty or has no rows/columns
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])

        # initialize two matrices to track the visited status for pacific and atlantic oceans
        # if a cell has its entry as True, it means that the cell can reach the ocean
        # so if a cell has both entries as True, it means that the cell can reach both oceans
        pacific = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic = [[False for _ in range(cols)] for _ in range(rows)]

        # start the dfs traversal for each cell on the borders for both oceans
        for row in range(rows):
            # (0,0), (1,0), (2,0), ..., (m-1,0)
            self.dfs(matrix, row, 0, pacific, float('-inf'))
            # (0,n-1), (1,n-1), (2,n-1), ..., (m-1,n-1)
            self.dfs(matrix, row, cols - 1, atlantic, float('-inf'))
        for col in range(cols):
            # (0,0), (0,1), (0,2), ..., (0,n-1)
            self.dfs(matrix, 0, col, pacific, float('-inf'))
            # (m-1,0), (m-1,1), (m-1,2), ..., (m-1,n-1)
            self.dfs(matrix, rows - 1, col, atlantic, float('-inf'))

        # gather the result, which are the cells that both oceans can reach
        res = []
        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    res.append([row, col])

        return res

    def dfs(self, matrix, row, col, visited, prev_height):
        # check boundaries to see if we can visit the cell
        rows, cols = len(matrix), len(matrix[0])
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return

        # avoid revisiting the cell
        if visited[row][col]:
            return

        # if the current cell has a height less than the prevous cell height, we cannot visit it
        # because it means that the water cannot flow from the current cell to the previous cell
        if prev_height > matrix[row][col]:
            return

        # mark the cell as visited
        visited[row][col] = True

        # explore the neighboring cells
        for dir in self.DIRECTIONS:
            self.dfs(matrix, row + dir[0], col + dir[1], visited, matrix[row][col])

        # equivalent to the following code:
        # self.dfs(matrix, row - 1, col, visited, matrix[row][col]) or \
        #     self.dfs(matrix, row, col - 1, visited, matrix[row][col]) or \
        #     self.dfs(matrix, row + 1, col, visited, matrix[row][col]) or \
        #     self.dfs(matrix, row, col + 1, visited, matrix[row][col])

# solution two
# Complexity:
# O(m^2 * n^2) time - where m is the number of rows and n is the number of columns
# O(m * n) space - where m is the number of rows and n is the number of columns
class Solution:  
    def pacificAtlantic(self, matrix):
        res = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # we set start height to float('inf') to avoid the first check in flow
                # because we know that the first check will always be true, so
                # that we can always start moving from any starting cell (row, col) here
                # searching for a path to pacific (first) and atlantic (second) and
                # we append the cell to res if we can flow to both pacific and atlantic
                if self.flow(matrix, row, col, float('inf')) and \
                    self.flow(matrix, row, col, float('inf'), False):
                    res.append([row, col])

        return res

    def flow(self, matrix, row, col, prev_height, pacific=True):
        # check if we are in the pacific
        if row < 0 or col < 0:
            return True if pacific else False

        # check if we are in the atlantic
        if row >= len(matrix) or col >= len(matrix[0]):
            return True if not pacific else False

        # store height of current cell for backtracking
        height = matrix[row][col]

        # cannot move to higher heights, also to avoid revisiting
        if height > prev_height:
            return False

        # set current cell to float('inf') to avoid revisiting
        matrix[row][col] = float('inf')

        # check if we can flow to pacific or atlantic
        flows = self.flow(matrix, row - 1, col, height, pacific) or \
            self.flow(matrix, row, col - 1, height, pacific) or \
            self.flow(matrix, row + 1, col, height, pacific) or \
            self.flow(matrix, row, col + 1, height, pacific)

        # backtrack
        matrix[row][col] = height
        return flows

# solution three less clean
# Complexity:
# O(m^2 * n^2) time - where m is the number of rows and n is the number of columns
# O(m * n) space - where m is the number of rows and n is the number of columns
class Solution:  
    def pacificAtlantic(self, matrix):
        res = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # check if we can flow to both pacific and atlantic
                if self.canFlow(matrix, row, col):
                    res.append([row, col])

        return res

    def canFlow(self, matrix, row, col):
        # store height of current cell for backtracking
        # and set current cell to float('inf') to avoid revisiting
        height = matrix[row][col]
        matrix[row][col] = float('inf')

        # check flow to pacific
        flows_pacific = self.flow(matrix, row - 1, col, height) or \
            self.flow(matrix, row, col - 1, height) or \
            self.flow(matrix, row + 1, col, height) or \
            self.flow(matrix, row, col + 1, height)

        # check flow to atlantic
        flows_atlantic = self.flow(matrix, row - 1, col, height, False) or \
            self.flow(matrix, row, col - 1, height, False) or \
            self.flow(matrix, row + 1, col, height, False) or \
            self.flow(matrix, row, col + 1, height, False)

        # backtrack
        matrix[row][col] = height
        # true if we can flow to both pacific and atlantic
        return flows_pacific and flows_atlantic

    def flow(self, matrix, row, col, prev_height, pacific=True):
        # check if we are in the pacific
        if row < 0 or col < 0:
            return True if pacific else False

        # check if we are in the atlantic
        if row >= len(matrix) or col >= len(matrix[0]):
            return True if not pacific else False

        # store height of current cell for backtracking
        height = matrix[row][col]

        # cannot move to higher heights, also to avoid revisiting
        if height > prev_height:
            return False

        # set current cell to float('inf') to avoid revisiting
        matrix[row][col] = float('inf')

        # check if we can flow to pacific or atlantic
        flows = self.flow(matrix, row - 1, col, height, pacific) or \
            self.flow(matrix, row, col - 1, height, pacific) or \
            self.flow(matrix, row + 1, col, height, pacific) or \
            self.flow(matrix, row, col + 1, height, pacific)

        # backtrack
        matrix[row][col] = height
        return flows