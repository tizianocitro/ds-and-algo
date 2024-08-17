# !difficulty: easy

'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Input: x = 4
Output: 2

Input: x = 15
Output: 3 (not 3.87, because we want the integer part of the square root)
'''

# solution one
# Complexity:
# O(log(n)) time - where n is the size of the search space
# In this case, the search space is from 2 to x/2. So O(log(x/2)) = O(logx)
# O(1) space
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 2
        right = x // 2
        while left <= right:
            middle = (left + right) // 2
            squared = middle ** 2
            if squared == x:
                return middle
            if squared > x:
                right = middle - 1
            else:
                left = middle + 1
        return right