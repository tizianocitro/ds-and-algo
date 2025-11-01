# !code: 7, !difficulty: medium, !from: https://leetcode.com/problems/reverse-integer/

'''Problem:
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:
- -2^31 <= x <= 2^31 - 1

Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21
'''

# solution one using math
# Complexity:
# O(log10(n)) time - where n is the input number
# O(1) space
class Solution:
    def reverse(self, x: int) -> int:
        MAX = (2 ** 31) - 1

        # track if the number is negative to return the correct sign
        # at then end because for processing we need it to be positive
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        rev = 0

        # at the end of the loop, rev will be the reversed number
        # and x will become 0 because we are dividing it by 10
        while x > 0:
            # check if the reversed number will be greater than the max
            # if we multiply it by 10 before adding the last digit
            if rev * 10 > MAX:
                return 0
            rev *= 10

            # check if the reversed number will be greater than the max
            # if we add the last digit
            if rev + (x % 10) > MAX:
                return 0
            rev += x % 10

            # remove the last digit from x
            x //= 10

        # return the reversed number with the correct sign
        return rev if not is_negative else rev * -1
