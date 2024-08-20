# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/sudoku-solver-hard

'''Problem:
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells. It is guaranteed that the input board has only one solution.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'

Input:
    {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
    {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
    {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
    {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
    {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
    {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
    {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
    {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
    {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
Output:
    {'5'', '3'', '4'', '6'', '7'', '8'', '9'', '1'', '2''},
    {'6'', '7'', '2'', '1'', '9'', '5'', '3'', '4'', '8''},
    {'1'', '9'', '8'', '3'', '4'', '2'', '5'', '6'', '7''},
    {'8'', '5'', '9'', '7'', '6'', '1'', '4'', '2'', '3''},
    {'4'', '2'', '6'', '8'', '5'', '3'', '7'', '9'', '1''},
    {'7'', '1'', '3'', '9'', '2'', '4'', '8'', '5'', '6''},
    {'9'', '6'', '1'', '5'', '3'', '7'', '2'', '8'', '4''},
    {'2'', '8'', '7'', '4'', '1'', '9'', '6'', '3'', '5''},
    {'3'', '4'', '5'', '2'', '8'', '6'', '1'', '7'', '9''}
Explanation: The given output is the only valid Sudoku solution.
'''

# solution one
# Complexity:
# O(1) time - because the board size is fixed as there is no variable input
# there is actually 9!^9 number of operations. Let's consider one row where we have 9 cells to fill.
# There are not more than 9 possibilities for the first number to put, not more than 9×8 for the second one, not more than 9×8×7 for the third one, and so on.
# In total, that results in not more than 9! possibilities for just one row; this means not more than 9!^9 operations in total.
# O(1) space - because the board size is fixed and the space is used to store the board containing 81 cells
class Solution:
    def solveSudoku(self, board):
        # for all cells
        for row in range(9):
            for col in range(9):
                # if we find an empty cell
                if board[row][col] == '.':
                    # try every number from 1-9 in case of empty cell
                    for num in range(1, 10):
                        # check if the number is valid in the current cell
                        if self.isValid(board, row, col, str(num)):
                            # if it is valid, fill the cell with the number
                            board[row][col] = str(num)
                            # recursively call the function to solve the rest of the board
                            if self.solveSudoku(board):
                                return True
                            else:
                                # if the current number doesn't lead to a solution, backtrack by emptying the cell
                                board[row][col] = '.' 

                    # if we have tried every number and none of them lead to a solution, return false
                    return False

        # if the board is completely filled, return true
        return True

    # check if a given number is valid in the current cell
    def isValid(self, board, row, col, num):
        # check if we already have the same number in the same row, col or box
        for x in range(9):
            # check if the same number is in the same row
            if board[row][x] == num:
                return False
            # check if the same number is in the same col
            if board[x][col] == num:
                return False
            # check if the same number is in the same 3x3 box
            '''
            First bracket [(row//3)*3 + x//3]:
            - row//3: gives us 0 for rows 0-2, 1 for rows 3-5, and 2 for rows 6-8
            - (row//3)*3: gives us 0, 3, or 6. This is the starting row of the 3x3 box
            - x//3: as x goes from 0 to 8, this gives us 0, 0, 0, 1, 1, 1, 2, 2, 2
            - the sum of these gives us the correct row within the 3x3 box
            - this because we have to check three times the row 0 (just with different columns), then three times the row 1 and 2
            Second bracket [(col//3)*3 + x%3]:
            - (col//3)*3: gives us the starting column of the 3x3 box (0, 3, or 6)
            - x%3: as x goes from 0 to 8, this gives us 0, 1, 2, 0, 1, 2, 0, 1, 2

            So with these two we go over every column of every row in the 3x3 box
            '''
            if board[(row//3)*3 + x//3][(col//3)*3 + x%3] == num:
                return False
        return True
