# !difficulty: easy

'''Problem:
Given a string s, remove all adjacent duplicate characters recursively to generate the resultant string.

Input: s = "abccba"
Output: ""
Explanation: First, we remove "cc" to get "abba". Then, we remove "bb" to get "aa". Finally, we remove "aa" to get an empty string.

Input: s = "foobar"
Output: "fbar"
Explanation: We remove "oo" to get "fbar".
'''

# solution one with while loop
# Complexity:
# O(n) time - where n is the length of the string
# O(n) space - because we are using a stack to store the characters,
# and, in the worst case, when the string has no adjacent duplicates,
# all the characters will be pushed onto the stack, requiring n space
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
                continue
            while stack and stack[-1] == c:
                stack.pop()
        res = ''
        for c in stack:
            res += c
        return res

# solution one with if statement
# Complexity:
# O(n) time - where n is the length of the string
# O(n) space - because we are using a stack to store the characters,
# and, in the worst case, when the string has no adjacent duplicates,
# all the characters will be pushed onto the stack, requiring n space
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            # if the stack is not empty and the current character is the same as the top of the stack,
            # pop the character from the stack
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        # join the stack to a string
        return ''.join(stack)