# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64c14baaee20248bcc6d1d4c

'''Problem:
You are given a string s and an integer k.
Your task is to remove groups of identical, consecutive characters from the string such that each group has exactly k characters.
The removal of groups should continue until it's no longer possible to make any more removals.
The result should be the final version of the string after all possible removals have been made.

Input: s = "abbbaaca", k = 3
Output: "ca"
Explanation: First, we remove "bbb" to get "aaaca". Then, we remove "aaa" to get "ca".

Input: s = "abbaccaa", k = 3
Output: "abbaccaa"
Explanation: There are no instances of 3 adjacent characters being the same.
'''

# solution one with while loop
# Complexity:
# O(n) time - where n is the length of the string
# O(n) space - because we are using a stack to store the characters
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                count = 1
                while stack and count < k and c == stack[-1]:
                    stack.pop()
                    count +=1
                # if we have removed less than k characters, we need to add them back
                # because we need to remove exactly k adjacent characters
                while count > 0 and count < k:
                    stack.append(c)
                    count -= 1
                continue
            stack.append(c)
        return "".join(stack)

# solution two with custom stack elements
# O(n) time - where n is the length of the string
# O(n) space - because we are using a stack to store the characters
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                (char, occurrencies) = stack.pop()
                if occurrencies < k - 1:
                    stack.append((char, occurrencies + 1))
                continue
            stack.append((c, 1))

        # equivalent would have been to use the following line instead of the for loop
        # return ''.join(c * n for c, n in stack)
        res = ""
        for el in stack:
            (char, occurrencies) = el
            while occurrencies > 0:
                res += char
                occurrencies -= 1
        return res

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                # increment the count of the top character in the stack
                stack[-1][1] += 1
            else:
                # otherwise, push a new character-count pair onto the stack
                stack.append([c, 1])

            # if the count of the top character in the stack reaches k
            if stack[-1][1] == k:
                # remove it from the stack
                stack.pop()
        
        return ''.join(c * n for c, n in stack)  