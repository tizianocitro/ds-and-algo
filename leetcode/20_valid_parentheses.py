# !code: 20, !difficulty: easy, !from: https://leetcode.com/problems/valid-parentheses, http://neetcode.io/problems/valid-parentheses

'''Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Constraints:
-  1 <= s.length <= 104
- s consists of parentheses only '()[]{}'

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([])"
Output: true
'''

'''Notes:
Look at patterns/test_knowledge/easy/valid_parentheses.py for other solutions (like the one using hash map).
'''

# solution one using stack and hash map
# Complexity:
# O(n) time - where n is the length of the string
# O(n) space - where n is the length of the string
class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open_parentheses = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch not in closed_to_open_parentheses:
                stack.append(ch)
                continue

            # if it's a closing parenthesis, we check if the stack is empty
            # if it is, we return False because there's no opening parenthesis to match it
            if not stack:
                return False

            # if the the top element in the stack is
            # not the corresponding opening parenthesis
            # than it's not a valid string
            if stack[-1] != closed_to_open_parentheses[ch]:
                return False

            # it is the corresponding opening parenthesis, we pop it from the stack
            stack.pop()

        return len(stack) == 0


# solution two using stack and enum arrays
# Complexity:
# O(n) time - where n is the length of the string
# O(n) space - where n is the length of the string
class Solution:
    def isValid(self, s: str) -> bool:
        closing_parentheses = [')', ']', '}']
        opening_parentheses = ['(', '[', '{']
        stack = []

        for ch in s:
            # if it's an opening parenthesis, we add it to the stack
            if ch in opening_parentheses:
                stack.append(ch)
                continue

            # if it's a closing parenthesis, we check if the stack is empty
            # if it is, we return False because there's no opening parenthesis to match it
            if not stack:
                return False

            # for each closing parenthesis, we check if the last element in the stack
            # is the corresponding opening parenthesis, if it is, we pop it from the stack
            # if it's not, we return False because the closing parenthesis doesn't match the opening parenthesis
            for i, closing_parenthesis in enumerate(closing_parentheses):
                if ch != closing_parenthesis:
                    continue

                if stack[-1] != opening_parentheses[i]:
                    return False
                else:
                    stack.pop()

        # return True if the stack is empty, otherwise, return False
        # becauseif it's not empty, then there are unmatched opening parentheses
        return len(stack) == 0
