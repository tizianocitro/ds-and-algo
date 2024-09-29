# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/valid-sudoku-medium

'''Problem:
Determine if a 9x9 Sudoku board is valid. A valid Sudoku board will hold the following conditions:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- The 9 3x3 sub-boxes of the grid must also contain the digits 1-9 without repetition.

Note:
- The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
- You need to validate only filled cells.

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
Explanation: This Sudoku board is valid as it adheres to the rules of no repetition in each row, each column, and each 3x3 sub-box.

Input:
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
Explanation: The first and fourth rows both contain the number '8', violating the Sudoku rules.

Input:
    [[".",".","4",".",".",".","6","3","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,["5",".",".",".",".",".",".","9","."]
    ,[".",".",".","5","6",".",".",".","."]
    ,["4",".","3",".",".",".",".",".","1"]
    ,[".",".",".","7",".",".",".",".","."]
    ,[".",".",".","5",".",".",".",".","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,[".",".",".",".",".",".",".",".","."]]
Output: false
Explanation: The fourth column contains the number '5' two times, violating the Sudoku rules.
'''

# solution one
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

# solution two using sets
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