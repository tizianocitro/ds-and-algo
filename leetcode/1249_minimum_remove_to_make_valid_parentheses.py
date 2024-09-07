# !code: 1249, !difficulty: medium, !from: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

'''Problem:
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
= It can be written as (A), where A is a valid string.

Constraints:
- 1 <= s.length <= 105
- s[i] is either '(' , ')', or lowercase English letter

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''

# solution one using a set and a stack
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string
# because in the worst case we have all unmatched parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        unmatched_ix_set, unmatched_par_stack = set(), []

        for i, ch in enumerate(s):
            # if we have a closing parenthesis and there is an opening parenthesis
            # in the stack, we remove the opening parenthesis from the stack
            if ch == ')' and unmatched_par_stack and unmatched_par_stack[-1][0] == '(':
                _, ix = unmatched_par_stack.pop()
                unmatched_ix_set.remove(ix)
            # else if we have an opening or closing parenthesis,
            # we add it to the stack along with its index for later removal if needed
            elif ch == '(' or ch == ')':
                unmatched_ix_set.add(i)
                unmatched_par_stack.append((ch, i))

        res = ''
        for i in range(len(s)):
            # skip the indexes of the unmatched parentheses
            if i in unmatched_ix_set:
                continue
            res += s[i]

        return res

# solution two using two stacks
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string
# because in the worst case we have all unmatched parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        unmatched_ix_stack, unmatched_par_stack = [], []

        for i, ch in enumerate(s):
            if ch == ')' and unmatched_par_stack and unmatched_par_stack[-1] == '(':
                    unmatched_ix_stack.pop()
                    unmatched_par_stack.pop()
            elif ch == '(' or ch == ')':
                unmatched_ix_stack.append(i)
                unmatched_par_stack.append(ch)

        res = ''
        i = j = 0
        while i < len(s):
            # if we have an unmatched parenthesis, we skip it
            if j < len(unmatched_ix_stack) and i == unmatched_ix_stack[j]:
                j += 1
            else:
                # otherwise we add the character to the result
                res += s[i]
            i += 1

        return res 

