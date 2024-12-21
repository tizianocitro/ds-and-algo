# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639dcb67ef27e08651fb4db6

'''Problem:
Given an expression containing digits and operations (+, -, *),
find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

Input: "1+2*3"
Output: 7, 9
Explanation: 
    1+(2*3) => 7
    (1+2)*3 => 9

Input: "2*3-4-5"
Output: 8, -12, 7, -7, -3 
Explanation: 
    2*(3-(4-5)) => 8
    2*(3-4-5) => -12
    2*3-(4-5) => 7
    2*(3-4)-5 => -7
    (2*3)-4-5 => -3
'''

# solution one recursive
# Complexity:
# O(n * 2^n) time - where n is the length of the input string
# O(2^n) space - where n is the length of the input string
class Solution:
    def diffWaysToEvaluateExpression(self, input):
        result = []
        # base case: if the input string is a number, parse and add it to output
        # we got to a single number, so we can't break it down any further
        if '+' not in input and '-' not in input and '*' not in input:
            result.append(int(input))
        else:
            # for example, if input is 1+2*3, then we will break in this way:
            # for char = '+', leftPart = 1, rightPart = 2*3
            # the recursive call will have for char = '*', leftPart = 2, rightPart = 3
            # then we combine the results of these two sub-expressions as 1 + 6 = 7
            # continue this process for the other part of the input, we will have:
            # for char = '*', leftPart = 1+2, rightPart = 3
            # the recursive call will have for char = '+', leftPart = 1, rightPart = 2
            # then we combine the results of these two sub-expressions as 3 * 3 = 9
            for i in range(0, len(input)):
                char = input[i]

                if not char.isdigit():
                    # break the equation here into two parts and make recursively calls
                    leftParts = self.diffWaysToEvaluateExpression(input[0:i])
                    rightParts = self.diffWaysToEvaluateExpression(input[i+1:])

                    for part1 in leftParts:
                        for part2 in rightParts:
                            if char == '+':
                                result.append(part1 + part2)
                            elif char == '-':
                                result.append(part1 - part2)
                            elif char == '*':
                                result.append(part1 * part2)

        return result

# solution two recursive with memoization
# the problem has overlapping subproblems, as recursive calls in solution one
# can be evaluating the same sub-expression multiple times
# to resolve this, we can use memoization and store the intermediate results in a HashMap
# in each function call, we can check our map to see if we have already evaluated this sub-expression before
# Complexity:
# O(n * 2^n) time - where n is the length of the input string
# O(2^n) space - where n is the length of the input string
class Solution:
    def diffWaysToEvaluateExpression(self, input):
        map = {}
        return self.diffWaysToEvaluateExpressionWithMemo(map, input)

    def diffWaysToEvaluateExpressionWithMemo(self, map, input):
        # check if the result for the input expression is already in map
        if input in map:
            return map[input]

        result = []
        # base case: if the input string is a number, parse and add it to output
        # we got to a single number, so we can't break it down any further
        if '+' not in input and '-' not in input and '*' not in input:
            result.append(int(input))
        else:
            # for example, if input is 1+2*3, then we will break in this way:
            # for char = '+', leftPart = 1, rightPart = 2*3
            # the recursive call will have for char = '*', leftPart = 2, rightPart = 3
            # then we combine the results of these two sub-expressions as 1 + 6 = 7
            # continue this process for the other part of the input, we will have:
            # for char = '*', leftPart = 1+2, rightPart = 3
            # the recursive call will have for char = '+', leftPart = 1, rightPart = 2
            # then we combine the results of these two sub-expressions as 3 * 3 = 9
            for i in range(0, len(input)):
                char = input[i]

                if not char.isdigit():
                    # break the equation here into two parts and make recursively calls
                    leftParts = self.diffWaysToEvaluateExpression(input[0:i])
                    rightParts = self.diffWaysToEvaluateExpression(input[i+1:])

                    for part1 in leftParts:
                        for part2 in rightParts:
                            if char == '+':
                                result.append(part1 + part2)
                            elif char == '-':
                                result.append(part1 - part2)
                            elif char == '*':
                                result.append(part1 * part2)

        # memoize result to input expression
        map[input] = result

        return result

# solution three iterative
# Complexity:
# O(n * 3^n) time - where n is the length of the input string
# O(3^n) space - where n is the length of the input string
from collections import deque

class Expression:
    def __init__(self, expr, next, open_p, closed_p, digits):
        self.expr = expr
        self.next = next
        self.open_p = open_p
        self.closed_p = closed_p
        self.digits = digits

    def __str__(self):
        # for more details, switch the commented line between the two below
        # return f'expr: {self.expr}, digits: {self.digits}, open_p: {self.open_p}, closed_p: {self.closed_p}'
        return f'expr: {self.expr}'

class Solution:
    def diffWaysToEvaluateExpression(self, input):
        result = set()

        # in case no digit is given, just return []
        num_digits = self.getNumOfDigits(input)
        if num_digits == 0:
            return []

        q = deque()
        q.append(Expression('', 0, 0, 0, 0))

        while q:
            expr = q.popleft()

            # we have added all digits, so just complete the expr by adding
            # eventually missing closed parentheses
            if expr.digits == num_digits:
                # we need to eval the expression because we need the result
                result.add(eval(self.completeExpr(expr)))
            else:
                current_char = input[expr.next]

                # if it's a symbol, just add the symbol to the expr
                if self.isSymbol(current_char):
                    q.append(Expression(expr.expr + current_char, expr.next + 1,
                                        expr.open_p, expr.closed_p, expr.digits))
                    continue

                # just append the digit without parentheses
                q.append(Expression(expr.expr + current_char, expr.next + 1,
                                    expr.open_p, expr.closed_p, expr.digits + 1))

                # in all cases except for the last digit,
                # also append the digit with an open parentheses
                if expr.digits < num_digits - 1:
                    q.append(Expression(expr.expr + '(' + current_char, expr.next + 1,
                                        expr.open_p + 1, expr.closed_p, expr.digits + 1))

                # if there are more open than closed parentheses,
                # also append the digit with a closed parentheses
                if expr.open_p > expr.closed_p:
                    q.append(Expression(expr.expr + current_char + ')', expr.next + 1,
                                        expr.open_p, expr.closed_p + 1, expr.digits + 1))

        return [e for e in result]

    def getNumOfDigits(self, input):
        digits = 0
        for char in input:
            if char.isdigit():
                digits +=1
        return digits

    def isSymbol(self, char):
        return char == '*' or char == '+' or char == '-'

    def completeExpr(self, expr):
        e = list(expr.expr)
        if e[-1] == '(':
            del e[-1]

        while expr.closed_p < expr.open_p:
            e.append(')')
            expr.closed_p += 1

        return ''.join(e)