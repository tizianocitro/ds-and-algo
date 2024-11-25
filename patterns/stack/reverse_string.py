# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6490189d822978cc90e2ace0

'''Problem:
Given a string, write a function that uses a stack to reverse the string.
The function should return the reversed string.

Input: "Hello, World!"
Output: "!dlroW ,olleH"
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the string
# O(n) space - where n is the length of the string
class Solution:
    def reverseString(self, s):
        stack = list(s)
        reversed_string = ''
        while len(stack) > 0:
            reversed_string += stack.pop()
        return reversed_string