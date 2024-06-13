# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/657083faae2f8647ec1742a1

'''Problem:
Given a string str containing '(' and ')' characters, find the minimum number of parentheses that need to be added to a string of parentheses to make it valid.

A valid string of parentheses is one where each opening parenthesis '(' has a corresponding closing parenthesis ')' and vice versa.

The goal is to determine the least amount of additions needed to achieve this balance.

Input: "(()"
Output: 1
Explanation: The string has two opening parentheses and one closing parenthesis. Adding one closing parenthesis at the end will balance it.

Input: "))(("
Output: 4
Explanation: There are two closing parentheses at the beginning and two opening at the end. We need two opening parentheses before the first closing and two closing parentheses after the last opening to balance the string.

Input: "(()())("
Output: 1
Explanation: The string has three opening parentheses and three closing parentheses, with an additional opening parenthesis at the end. Adding one closing parenthesis at the end will balance it.
'''

'''Solution:
To solve this problem, we track the balance of parentheses as we iterate through the string.
We initialize two counters: one for the balance of parentheses and another for the count of additions needed.

For each character in the string, if it's an opening parenthesis '(', we increase the balance.
If it's a closing parenthesis ')', we decrease the balance.
If the balance is negative at any point (which means there are more closing parentheses than opening ones),
we increment the additions counter and reset the balance to zero.

The total number of additions required is the sum of the additions counter and the absolute value of the final balance,
ensuring that all unmatched opening parentheses are also accounted for.
This approach efficiently computes the minimum number of parentheses to be added for the string to become valid.
'''

# solution one
# Complexity:
# O(n) time -  where n is the length of the input string
# O(1) space
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance, addition = 0, 0
        for par in s:
            # increment balance for '(', decrement for ')'
            balance += 1 if par == '(' else -1

            # if balance is negative, we have more ')' than '('
            if balance == -1:
                # increment addition needed for each unmatched ')'
                addition += 1
                # reset balance as we've accounted for the unmatched ')'
                balance += 1

        # the total addition needed is the sum of the balance and addition
        # because balance is the unmatched '(' and addition is the unmatched ')'
        return addition + balance

# solution two using stack
# Complexity:
# O(n) time -  where n is the length of the input string
# O(n) space - where n is the length of the input string for the stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for par in s:
            # if the stack is not empty and the current parenthesis is closing
            # and the last parenthesis in the stack is opening, we pop the
            # last parenthesis because we have a valid pair
            if stack and par == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(par)

        # the length of the stack is the number of
        # parentheses that are not balanced
        return len(stack)

