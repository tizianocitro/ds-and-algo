# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/path-with-minimum-effort-medium

'''Problem:
You are given a 2D array heights[][] of size n x m, where heights[n][m] represents the height of the cell (n, m).

Find a path from the top-left corner to the bottom-right corner that minimizes the effort required to travel between consecutive points, 
where effort is defined as the absolute difference in height between two points. In a single step, you can either move up, down, left or right.

Return the minimum effort required for any path from the first point to the last.

Constraints:
- rows == heights.length
- columns == heights[i].length

Input: heights =
    [[1,2,3],
    [3,8,4],
    [5,3,5]]
Output: 1
Explanation: The path with the minimum effort is along the edges of the grid (right, right, down, down) which requires an effort of 1 between each pair of points.

Input: heights =
    [[1,2,2],
    [3,3,3],
    [5,3,1]]
Output: 2
Explanation: The path that minimizes the maximum effort goes through (1,2,2,3,1), which has a maximum effort of 2 (from 3 to 1).

Input: heights =
    [[1,1,1],
    [1,1,1],
    [1,1,1]]
Output: 0
Explanation: The path that minimizes the maximum effort goes through (1,1,1,1,1), which has a maximum effort of 0.
'''

# solution one using union find
# Complexity:
# O(n * m * log(n * m)) time - where n is the number of rows and m is the number of columns in the heights matrix
# O(n * m) space - for the parent and rank arrays and the edges list
class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.rank = [node for node in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def minimumEffortPath(self, heights):
        row, col = len(heights), len(heights[0])
        # we will encode each two adjacent cells into an integer using the formula i * col + j
        # where i is the row index, j is the column index, and col is the number of columns
        uf = UnionFind(row * col)

        # each edge is a tuple (x, y, diff) where x and y are the cells as integers connected
        # by the edge and diff is the difference in heights between the two cells
        edges = []

        for i in range(row):
            for j in range(col):
                # add edge to the cell above (if it exists)
                if i > 0:
                    edges.append((i * col + j, (i - 1) * col + j, abs(heights[i][j] - heights[i - 1][j])))
                # add edge to the cell on the left (if it exists)
                if j > 0:
                    edges.append((i * col + j, i * col + (j - 1), abs(heights[i][j] - heights[i][j - 1])))

        # sort edges by the difference in heights
        # this takes O(n * m * log(n * m)) time because there are approximately 2 * n * m edges
        edges.sort(key=lambda x: x[2])

        first_cell, last_cell = 0, row * col - 1
        # this takes O(n * m * a(n * m)) time
        for x, y, diff in edges:
            # union the cells connected by the edge
            uf.union(x, y)
            # if the source and destination cells are connected, return the effort
            if uf.find(first_cell) == uf.find(last_cell):
                return diff

        return 0

# solution two using heap and bfs
# Complexity:
# O(n * m * log(n * m)) time - where n is the number of rows and m is the number of columns in the heights matrix
# O(n * m) space - for the heap and the efforts matrix
import heapq

class Solution:
    def minimumEffortPath(self, heights):
        if not heights:
            return 0

        rows, cols = len(heights), len(heights[0])
        # directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # effort for all nodes though which we have passed
        efforts = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        # effort for the starting node is 0
        efforts[0][0] = 0

        # (effort, row, col)
        min_heap = [(0, 0, 0)]
        while min_heap:
            current_effort, row, col = heapq.heappop(min_heap)

            if row == rows - 1 and col == cols - 1:
                return current_effort

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # effort to move from the current node to the new node (new path)
                    new_effort = abs(heights[new_row][new_col] - heights[row][col])
                    # max effort of the current path and the new path
                    max_effort = max(current_effort, new_effort)

                    # found a path that has effort smaller than any
                    # other path that goes through this node
                    if max_effort < efforts[new_row][new_col]:
                        efforts[new_row][new_col] = new_effort
                        heapq.heappush(min_heap, (max_effort, new_row, new_col))

        return 0