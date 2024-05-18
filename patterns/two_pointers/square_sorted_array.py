# !difficulty: easy

''' Problem:
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
'''

# solution one
# Complexity:
# O(n) time - where n is the size of the array
# O(n) space - where n is the size of the array
class Solution:
    def makeSquares(self, arr):
        n = len(arr)
        squares = [0 for x in range(n)]    
        l, r = 0, n - 1
        squaresIndex = n - 1

        while l <= r:
            squaredLeft = arr[l] ** 2
            squaredRight = arr[r] ** 2

            if squaredLeft < squaredRight:
                squares[squaresIndex] = squaredRight
                r -= 1
            else:
                squares[squaresIndex] = squaredLeft
                l += 1
            squaresIndex -= 1

        return squares
