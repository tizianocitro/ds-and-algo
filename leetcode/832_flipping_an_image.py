# !code: 832, !difficulty: easy, !from: https://leetcode.com/problems/flipping-an-image/

'''Problem:
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].

Constraints:
- n == image.length
- n == image[i].length
- 1 <= n <= 20
- images[i][j] is either 0 or 1

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]]. Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
'''

# solution one
# Complexity:
# O(n^2) time - where n is the number of bits in the image
# the problem states that number of columns is equal to the number of rows
# O(1) space
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        for row in range(rows):
            left, right = 0, cols - 1

            while left < right:
                # flip the matrix's row
                # xor each bit in the row with one to invert it,
                # because 0 ^ 1 = 1 and 1 ^ 1 = 0
                image[row][left], image[row][right] = image[row][right] ^ 1, image[row][left] ^ 1
                left += 1
                right -= 1

            # manage the case the image has an odd number of bits,
            # we need to invert the middle bit, because it wasn't inverted
            # in the while loop above, because we are on the middle bit
            # when left == right, so we need to invert it here
            if left == right:
                image[row][left] ^= 1

        return image
