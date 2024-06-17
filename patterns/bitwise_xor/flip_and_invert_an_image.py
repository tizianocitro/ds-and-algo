# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a0a7c7ef4e913a2e2bf5de

'''Problem:
Given a square binary matrix representing an image, we want to flip the image horizontally, then invert it.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [1, 1, 0] results in [0, 0, 1].

Input: [
    [1,0,1],
    [1,1,1],
    [0,1,1],
]
Output: [
    [0,1,0],
    [0,0,0],
    [0,0,1],
]
Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]

Input: [
    [1,1,0,0],
    [1,0,0,1],
    [0,1,1,1], 
    [1,0,1,0],
]
Output: [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,0,1],
    [1,0,1,0],
]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
'''

# solution one
# Complexity:
# O(n^2) time - where n is the number of bits in the matrix
# the problem states that number of columns is equal to the number of rows
# O(1) space
class Solution:
    def flipAndInvertImage(self, matrix):
        for row in matrix:
            left, right = 0 , len(row) - 1

            while left <= right:
                # flip the matrix's row
                row[left], row[right] = row[right], row[left]

                # xor each bit in the row with one to invert it,
                # because 0 ^ 1 = 1 and 1 ^ 1 = 0
                row[left] ^= 1
                if left != right:
                    # we do this only when left != right, because
                    # we don't want to invert the middle bit in the case
                    # of an odd number of bits
                    row[right] ^= 1

                left += 1
                right -= 1

        return matrix

# solution two with a tiny modification from solution one
# Complexity:
# O(n^2) time - where n is the number of bits in the matrix
# the problem states that number of columns is equal to the number of rows
# O(1) space
class Solution:
    def flipAndInvertImage(self, matrix):
        for row in matrix:
            left, right = 0 , len(row) - 1

            while left <= right:
                # flip the matrix's row
                # xor each bit in the row with one to invert it,
                # because 0 ^ 1 = 1 and 1 ^ 1 = 0
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1

                left += 1
                right -= 1

            # manage the case the array has an odd number of bits,
            # we need to invert the middle bit, because it wasn't inverted
            # in the while loop above, because we are on the middle bit
            # when left == right, so we need to invert it here
            if left == right:
                row[left] ^= 1

        return matrix

# solutione three which is a bit more elegant
# Complexity:
# O(n^2) time - where n is the number of bits in the matrix
# the problem states that number of columns is equal to the number of rows
# O(1) space
class Solution:
    def flipAndInvertImage(self, matrix):
        # get the number of columns in the matrix
        columns = len(matrix[0])

        for row in matrix:
            # oterate through the first half of the row
            for i in range((columns + 1) // 2):
                # swap and invert elements symmetrically from the beginning and end of the row
                row[i], row[columns - i - 1] = row[columns - i - 1] ^ 1, row[i] ^ 1

        return matrix
