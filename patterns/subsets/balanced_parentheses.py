# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639cbb3b4374f9a7aada8ed0

'''Problem:
For a given number N, write a function to generate all combination of N pairs of balanced parentheses.

Input: n = 2
Output: (()), ()()

Input: n = 3
Output: ((())), (()()), (())(), ()(()), ()()()
'''

# solution one
# Complexity:
# O(n * 2^n) time -  where n is the number of pairs of parentheses
# If we don’t care for the ordering that ) can only come after (, then we have two options for every position,
# i.e., either put open parentheses or close parentheses.
# This means we can have a maximum of 2^n combinations. Because of the ordering, the actual number will be less than 2^n.
# While processing each element, we do need to concatenate the current string with ( or ).
# This operation will take O(n), so the overall time complexity of our algorithm will be (n * 2^n).
# This is not completely accurate but reasonable enough to be presented in the interview.
# The actual time complexity is O(4^n/SQRTn) bounded by the Catalan number but it is beyond the scope of a coding interview.
# O(n * 2^n) space -  where n is the number of pairs of parentheses
from collections import deque

class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount

class Solution:
    def generateValidParentheses(self, num):
        result = []
        queue = deque()
        queue.append(ParenthesesString("", 0, 0))

        while queue:
            ps = queue.popleft()

            # if we've reached the maximum number of open and close parentheses, add to result
            if ps.openCount == num and ps.closeCount == num:
                result.append(ps.str)
            else:
                # if we can add an open parentheses, add it
                if ps.openCount < num:
                    queue.append(ParenthesesString(ps.str + "(", ps.openCount + 1, ps.closeCount))

                # if we can add a close parentheses, add it
                if ps.openCount > ps.closeCount:
                    queue.append(ParenthesesString(ps.str + ")", ps.openCount, ps.closeCount + 1))

        return result
