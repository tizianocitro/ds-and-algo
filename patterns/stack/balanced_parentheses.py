# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64804bc840c761a52b2a872f

'''Problem:
Given a string s containing (, ), [, ], {, and } characters.
Determine if a given string of parentheses is balanced.

A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis in the correct order.

Input: s = "{[()]}";
Expected Output: true
Explanation: The parentheses in this string are perfectly balanced.
Every opening parenthesis '{', '[', '(' has a corresponding closing parenthesis '}', ']', ')' in the correct order.

Input: s = "{[}]";
Expected Output: false
Explanation: The brackets are not balanced in this string.
Although it contains the same number of opening and closing brackets for each type, they are not correctly ordered. The ']' closes '[' before '{' can be closed by '}',
and similarly, '}' closes '{' before '[' can be closed by ']'.
'''

# Solution one
# Complexity:
# 0(n) time - where n is the number of characters in the string
# 0(n) space - because in the worst-case scenario,
# when all the characters in the string are opening parentheses we push each character onto the stack
class Solution:
    def isValid(self, s):
        # creating a stack to keep track of opening parentheses
        stack = []

        for p in s:
            # if the character is an opening parenthesis, push it onto the stack
            if p in ['(', '{', '[']:
                stack.append(p)
                continue

            # if stack is empty and we have a closing parenthesis, the string is not balanced
            # the following would have been the same
            # if not stack:
            if len(stack) < 1:
                return False

            # if the character is a closing parenthesis, check whether 
            # it corresponds to the most recent opening parenthesis,
            # which should be at the top of the stack
            top = stack[-1]
            if p == ')' and top != '(':
                return False
            if p == ']' and top != '[':
                return False
            if p == '}' and top != '{':
                return False

            # remove the last opening parenthesis because the closing one matches,
            # otherwise we would not arrive here
            stack.pop()

        # if the stack is empty, all opening parentheses had a corresponding closing match
        return len(stack) == 0