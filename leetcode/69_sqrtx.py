# !code: 69, !difficulty: easy, !from: https://leetcode.com/problems/sqrtx/

'''Problem:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Constraints:
- 0 <= x <= 2^31 - 1

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''

# solution one using binary search
# Complexity:
# O(logn) time - where n is the size of the search space
# O(1) space
class Solution:
    def mySqrt(self, x: int) -> int:
        # √0 = 0, √1 = 1
        if x < 2:
            return x

        # we could optimize the search space by using:
        # left = 2
        left = 0
        right = x // 2
        while left <= right:
            middle = (left + right) // 2
            pw = middle * middle
            if pw == x:
                return middle
            if pw < x:
                left = middle + 1
            else:
                right = middle - 1

        return right
