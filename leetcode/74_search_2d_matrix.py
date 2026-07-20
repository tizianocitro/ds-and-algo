# !code: 74, !difficulty: medium, !from: https://leetcode.com/problems/search-a-2d-matrix, https://neetcode.io/problems/search-2d-matrix

"""Problem:
You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

# solution one using binary search twice, first on rows then on columns
# Complexity:
# O(log m + log n) = O(log(m * n)) time - where m is the number of rows and n is the number of columns, as we perform two binary searches
# O(1) space
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        # find the row that may contain the target using binary search,
        # we search for the row whose first element is <= target and its next row's first element is > target
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        # after the first binary search onm rows,
        # bottom represents the last row whose first element <= target
        # if bottom < 0, then every row's first element is > target
        # it means target is not in the matrix
        if bottom < 0:
            return False

        # normal binary search on the found row to find the target
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid_col = (left + right) // 2
            if matrix[bottom][mid_col] == target:
                return True

            if matrix[bottom][mid_col] < target:
                left = mid_col + 1
            else:
                right = mid_col - 1

        return False

# solution two using binary search on each row found using binary search on rows
# Complexity:
# O(log(m * n)) time - where m is the number of rows and n is the number of columns, as we perform a single binary search on the entire matrix
# O(1) space
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        # perform binary search on each row found using binary search on rows
        while top <= bottom:
            mid_row = (top + bottom) // 2

            left = 0
            right = len(matrix[0]) - 1
            while left <= right:
                mid_col = (left + right) // 2
                if matrix[mid_row][mid_col] == target:
                    return True

                if matrix[mid_row][mid_col] < target:
                    left = mid_col + 1
                else:
                    right = mid_col - 1

            if matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        return False

# solution tree using binary search on the whole matrix by treating it as a flattened sorted array
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # suppose matrix is:
        # [
        #   [1,  3,  5,  7],
        #   [10, 11, 16, 20],
        #   [23, 30, 34, 60]
        # ]
        #
        # rows = 3, cols = 4
        # total elements = rows * cols = 12
        #
        # if we flatten this matrix row by row, it becomes conceptually:
        # index:   0  1  2  3   4   5   6   7   8   9  10  11
        # value:   1  3  5  7  10  11  16  20  23  30  34  60
        #
        # notice: every row contributes exactly cols elements

        left = 0
        right = rows * cols - 1 # last index in flattened array

        while left <= right:
            mid = left + (right - left) // 2

            # integer division tells us how many full rows of size cols we have passed
            #
            # example with cols = 4:
            # mid = 0 -> 0 // 4 = 0  -> row 0
            # mid = 1 -> 1 // 4 = 0  -> row 0
            # mid = 2 -> 2 // 4 = 0  -> row 0
            # mid = 3 -> 3 // 4 = 0  -> row 0
            # mid = 4 -> 4 // 4 = 1  -> row 1
            # mid = 5 -> 5 // 4 = 1  -> row 1
            #
            # because every 4 elements we move to next row
            #
            # in general, each row has cols elements, so dividing by cols jumps rows correctly
            row = mid // cols

            # modulo gives the position inside the row
            #
            # continuing example with cols = 4:
            # mid = 0 -> 0 % 4 = 0 -> col 0
            # mid = 1 -> 1 % 4 = 1 -> col 1
            # mid = 2 -> 2 % 4 = 2 -> col 2
            # mid = 3 -> 3 % 4 = 3 -> col 3
            # mid = 4 -> 4 % 4 = 0 -> col 0 (new row)
            # mid = 5 -> 5 % 4 = 1 -> col 1
            #
            # modulo resets to 0 every time we complete a row
            #
            # so:
            # division -> tells which row
            # modulo   -> tells position inside that row
            col = mid % cols

            # now matrix[row][col] is exactly the same element
            # as the flattened array at index mid

            if target == matrix[row][col]:
                return True

            if target > matrix[row][col]:
                left = mid + 1
            else:
                right = mid - 1

        return False
