# !code: 9, !difficulty: easy, !from: https://leetcode.com/problems/palindrome-number/

'''Problem:
Given an integer x, return true if x is a palindrome, and false otherwise.

Constraints:
-231 <= x <= 231 - 1

Follow Up Question:
Could you solve it without converting the integer to a string?

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

# solution one using two pointers with convertion of the integer to a string
# Complexity:
# O(n) time - where n is the number of digits in the integer
# O(n) space - for creating the string representation of the integer
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers will never be palindromes
        # it is still managed by the loop but it is not necessary to do so
        if x < 0:
            return False

        # convert the integer to a string
        x_str = str(x)

        # iterate through the string from both ends
        left, right = 0, len(x_str) - 1
        while left <= right:
            # if the characters are not equal, the number is not a palindrome
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1

        # if the loop completes, the number is a palindrome
        return True

# solution two without converting the integer to a string (follow up question)
# Complexity:
# O(log10(n)) time - where n is the number of digits in the integer because we are dividing the number by 10 in each iteration
# O(1) space
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers will never be palindromes
        # it is still managed by the loop but it is not necessary to do so
        if x < 0:
            return False

        # if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0
        # only 0 satisfy this property
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        while reversed_half < x:
            # x % 10 gives us the last digit of the number
            # so with x = 12321, x % 10 = 1
            reversed_half = (reversed_half * 10) + (x % 10)
            # x // 10 removes the last digit of the number,
            # so with x = 12321, x // 10 = 1232, in this way,
            # the next iteration we can get 2 as the last digit with x % 10
            x //= 10

        # when the length is an odd number, we can get rid of the middle digit by reversed_half // 10
        # e.g., when the input is 12321, at the end of the while loop we get x = 12, reversed_half = 123,
        # since the middle digit doesn't matter in palidrome (it will always equal to itself),
        # we can simply get rid of it  by checking x == reversed_half // 10 along with x == reversed_half
        # for when the length is an even number, so the two halves are the same as each other
        return x == reversed_half or x == reversed_half // 10