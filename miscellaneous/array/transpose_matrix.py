# !difficulty: easy

# You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.
# The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left to bottom-right);
# it switches the row and column indices of the original matrix.
# You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

# Example 1:
# input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Example 2:
# input = [[1, 2], [3, 4], [5, 6]]
# expected = [[1, 3, 5], [2, 4, 6]]

# Example 3:
# input = [[1, 2]]
# expected = [[1], [2]]

# Complexity
# O(n * m) time where n is the number of rows and m the number of columns
# O(n * m) memory where n is the number of rows and m the number of columns because we create a whole new matrix

# solutione one creates one row per each iteration
def transposeMatrix(matrix):
    numOfRows = len(matrix)
    numOfColumns = len(matrix[0])
    transposedMatrix = []
    for col in range(numOfColumns):
        transposedRow = []
        for row in range(numOfRows):
            transposedRow.append(matrix[row][col])
        transposedMatrix.append(transposedRow)
    return transposedMatrix

# solution three creates the whole transposed matrix at the beginning
def transposeMatrix(matrix):
    numOfRows = len(matrix)
    numOfColumns = len(matrix[0])
    transposedMatrix = [[0 for _ in range(numOfRows)] for _ in range(numOfColumns)]
    for row in range(numOfRows):
        for col in range(numOfColumns):
            transposedMatrix[col][row] = matrix[row][col]
    return transposedMatrix
