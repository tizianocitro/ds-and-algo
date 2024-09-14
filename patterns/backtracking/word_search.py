# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/word-search-medium

'''Problem:
Given an m x n grid of characters board and a string word, return true if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once.
The board and word consist of only lowercase and uppercase English letters.

Input: word="ABCCED", board:
    { 'A', 'B', 'C', 'E' },
    { 'S', 'F', 'C', 'S' },
    { 'A', 'D', 'E', 'E' }
Output: true
Explanation: The word exists in the board:
    -> { 'A', 'B', 'C', 'E' },
    -> { 'S', 'F', 'C', 'S' },
    -> { 'A', 'D', 'E', 'E' }

Input: word="SEE", board:
    { 'A', 'B', 'C', 'E' },
    { 'S', 'F', 'C', 'S' },
    { 'A', 'D', 'E', 'E' }
Output: true
Explanation: The word exists in the board:
    -> { 'A', 'B', 'C', 'E' },
    -> { 'S', 'F', 'C', 'S' },
    -> { 'A', 'D', 'E', 'E' }
'''

# solution one
# Complexity:
# O(i*j*4^n) time, where n is the length of the word and i, j are the dimensions of the board
# This is because the function uses DFS to traverse the board, and for each cell in the board,
# it checks all 4 adjacent cells recursively. The worst-case scenario is when the word is
# found in the last cell of the board, and in that case, the we will have to check all
# possible paths from the starting cell to the last cell, which is 4^n possible paths.
# O(n) space, where n is the length of the word, because, in the worst case, we stop when we
# reach the end of the word or before it if the current cell doesn't match the current character of the word.
class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                # start the search from every cell
                if self.backtrackExist(board, word, i, j, 0):
                    return True

        return False

    def backtrackExist(self, board, word, i, j, current_index):
        # check if current coordinates are out of grid
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        # check if the current cell doesn't match the current character of the word
        if board[i][j] != word[current_index]:
            return False

        # check if we have reached the end of the word
        if current_index == len(word) - 1:
            return True

        # mark the current cell as visited by replacing it with '/'
        current, board[i][j] = board[i][j], '/'

        # check all 4 adjacent cells recursively
        exist = self.backtrackExist(board, word, i + 1, j, current_index + 1) or \
            self.backtrackExist(board, word, i - 1, j, current_index + 1) or \
            self.backtrackExist(board, word, i, j + 1, current_index + 1) or \
            self.backtrackExist(board, word, i, j - 1, current_index + 1)

        # backtrack by replacing the current cell with its original value
        board[i][j] = current

        return exist

# solution two with usage of any function
# Complexity:
# O(4^n) time, where n is the length of the word
# This is because the function uses DFS to traverse the board, and for each cell in the board,
# it checks all 4 adjacent cells recursively. The worst-case scenario is when the word is
# found in the last cell of the board, and in that case, the we will have to check all
# possible paths from the starting cell to the last cell, which is 4^n possible paths.
# O(n) space, where n is the length of the word, because, in the worst case, we stop when we
# reach the end of the word or before it if the current cell doesn't match the current character of the word.
class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                # start the search from every cell
                if self.backtrackExist(board, word, i, j, 0):
                    return True

        return False

    def backtrackExist(self, board, word, i, j, current_index):
        # check if current coordinates are out of grid
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        # check if the current cell doesn't match the current character of the word
        if board[i][j] != word[current_index]:
            return False

        # check if we have reached the end of the word
        if current_index == len(word) - 1:
            return True

        # mark the current cell as visited by replacing it with '/'
        current, board[i][j] = board[i][j], '/'

        # check all 4 adjacent cells recursively with any function
        exist = any([
            self.backtrackExist(board, word, i + 1, j, current_index + 1),
            self.backtrackExist(board, word, i - 1, j, current_index + 1),
            self.backtrackExist(board, word, i, j + 1, current_index + 1),
            self.backtrackExist(board, word, i, j - 1, current_index + 1),
        ])

        # backtrack by replacing the current cell with its original value
        board[i][j] = current

        return exist