# !code: 36, !difficulty: medium, !from: https://leetcode.com/problems/valid-sudoku/, https://neetcode.io/problems/valid-sudoku/

'''Problem:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- The 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Input:
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''

# solution one, similar to solution two but with simpler logic for sub-boxes
# Complexity:
# O(1) time - because the board size is fixed (81 cells) as there is no variable input
# O(1) space - because the board size is fixed and the space is used to store the board containing 81 cells
class Solution:
    def isValidSudoku(self, board):
        # you can also use simply 9 instead of len(board) and len(board[0])
        # because the board is always 9x9
        # so, for all cells in the 9x9 board
        for r in range(9):
            for c in range(9):
                # if the cell is not empty
                if board[r][c] != '.':
                    # check if the number is valid in the current cell
                    if not self.isValidValue(board, r, c):
                        return False
        # if all numbers are valid in the cell they are placed,
        # return true as the board is valid
        return True

    def isValidValue(self, board, row, col):
        num = board[row][col]

        # validate row and cols to check if num is the same as another number in the same row/col
        for i in range(9):
            # if num is the same as another number in the same row
            if i != col and board[row][i] == num:
                return False

            # if num is the same as another number in the same column
            if i != row and board[i][col] == num:
                return False

        # determine the starting row and col of the 3x3 box
        # for example:
        # - if row=0..2, then row_box=0 because 0//3=0, 1//3=0, 2//3=0 and 0*3=0
        # - if row=3..5, then row_box=3 because 3//3=1, 4//3=1, 5//3=1 and 1*3=3
        # - if row=6..8, then row_box=6 because 6//3=2, 7//3=2, 8//3=2 and 2*3=6
        # same logic applies to col_box
        row_box = (row // 3) * 3
        col_box = (col // 3) * 3

        # validate box to check if num is the same as another number in the same 3x3 box
        # we stop at row_box + 3 and col_box + 3 to cover the 3x3 box
        for i in range(row_box, row_box + 3):
            for j in range(col_box, col_box + 3):
                # if num is the same as another number in the same 3x3 box
                if i != row and j != col and board[i][j] == num:
                    return False

        return True

# solution two
# Complexity:
# O(1) time - because the board size is fixed (81 cells) as there is no variable input
# O(1) space - because the board size is fixed and the space is used to store the board containing 81 cells
class Solution:
    def isValidSudoku(self, board):
        # for all cells in the 9x9 board
        for row in range(9):
            for col in range(9):
                # if the cell is not empty
                if board[row][col] != ".":
                    # check if the number is valid in the current cell
                    if not self.isValidValue(board, row, col):
                        return False
        # if all numbers are valid in the cell they are placed, return true
        return True

    def isValidValue(self, board, row, col):
        num = board[row][col]
        # for all possible columns and rows
        for x in range(9):
            # if num is the same as another number in the same row
            if col != x and board[row][x] == num:
                return False
            # if num is the same as another number in the same column
            if row != x and board[x][col] == num:
                return False

            # if num is the same as another number in the same 3x3 box
            # this (box_row, box_col) will match each cell in the 3x3 box
            # across the 0..8 range for x in the loop
            box_row = (row // 3) * 3 + x // 3
            box_col = (col // 3) * 3 + x % 3
            if board[box_row][box_col] == num:
                # if num is the same as another number in the same 3x3 box
                # we first check if the cell is not the same as the current cell
                if (row, box_col) == (row, col) or (box_row, col) == (row, col):
                    continue
                # if the cell is not the same as the
                # current cell, we found a non-valid number
                return False
        return True

# solution three using sets
# Complexity:
# O(1) time - because the board size is fixed (81 cells) as there is no variable input
# O(1) space - because the board size is fixed and the space is used to store the board containing 81 cells
class Solution:
    def isValidSudoku(self, board):
        # initialize sets to keep track of the numbers in each row, column, and box
        rows = set()
        columns = set()
        boxes = set()

        # iterate through each cell in the 9x9 board
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    # formulate keys for the row, column, and box
                    row_key = f"row{row}({num})"
                    col_key = f"col{col}({num})"
                    # mapping the 3x3 boxes in the board to positions
                    box_key = f"box{row // 3 * 3 + col // 3}({num})"

                    # check the corresponding sets for these keys
                    if row_key in rows or col_key in columns or box_key in boxes:
                        return False

                    # add the keys to the corresponding sets
                    rows.add(row_key)
                    columns.add(col_key)
                    boxes.add(box_key)

        return True