# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/valid-parentheses-easy

'''Problem:
Determine if an input string containing only the characters '(', ')', '{', '}', '[', and ']' is valid.
The string in input consists of only '()[]{}'.

A string is considered valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Each close bracket has a corresponding open bracket of the same type.

Input: "(]"
Output: false
Explanation: The opening parenthesis '(' is not closed by its corresponding closing parenthesis.

Input: "{[]}"
Output: true
Explanation: The string contains pairs of opening and closing brackets in the correct order.

Input: "[{]}"
Output: false
Explanation: The opening square bracket '[' is closed by a curly brace '}', which is incorrect.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the prices
# O(n) space - for the stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            # if it's any of the closing brackets, check if the top of the stack
            # is the corresponding open bracket and pop it if it is
            if stack and p == ')' and stack[-1] == '(':
                stack.pop()
                continue
            if stack and p == ']' and stack[-1] == '[':
                stack.pop()
                continue
            if stack and p == '}' and stack[-1] == '{':
                stack.pop()
                continue

            # if it's an open bracket, add it to the stack
            # or if it's a closing bracket, but the top of the stack
            # is not the corresponding open bracket
            stack.append(p)

        # the stack should be empty if all brackets are valid
        return len(stack) == 0

# solution two
# Complexity:
# O(n) time - where n is the length of the prices
# O(n) space - for the stack
class Solution:
    def isValid(self, s):
        stack = []

        for p in s:
            # if the character is an opening parenthesis, push it onto the stack
            if p in ['(', '{', '[']:
                stack.append(p)
                continue

            # if stack is empty and we have a closing parenthesis, the string is not balanced
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

# solution three
# Complexity:
# O(n) time - where n is the length of the prices
# O(n) space - for the stack
class Solution:
    def isValid(self, s: str) -> bool:
        # mapping of closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}

        stack = []
        for p in s:
            # if it is a closing bracket
            if p in mapping:
                top_element = stack.pop() if stack else '#'

                # check if the bracket matches the top of the stack
                if mapping[p] != top_element:
                    return False
            else:
                stack.append(p)

        return not stack
