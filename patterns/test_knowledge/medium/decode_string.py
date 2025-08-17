# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/decode-string-medium

'''Problem:
You have a string s that represents encodings of substrings, where each encoding is of the form k[encoded_string],
where k is a positive integer, and encoded_string is a string that contains letters only.

Your task is to decode this string by repeating the encoded_string k times and return it.
It is given that k is always a positive integer.

Constraints:
- s consists of lowercase English letters, digits, and square brackets '[]'
- s is guaranteed to be a valid input

Input: "3[a3[c]]"
Output: "acccacccaccc"
Explanation: The inner 3[c] is decoded as ccc, and then a is appended to the front, forming acc. This is then repeated 3 times to form acccacccaccc.

Input: "2[b3[d]]"
Output: "bdddbddd"
Explanation: The inner 3[d] is decoded as ddd, and then b is appended to the front, forming bddd. This is then repeated 2 times to form bddd bddd.

Input: "4[z]"
Output: "zzzz"
Explanation: The 4[z] is decoded as z repeated 4 times, forming zzzz.
'''

# solution one using a stack assuming numbers are always of one digit
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - for the stack because in the worst case, the stack will
# contain all the n characters of the input string
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        for c in reversed(s):
            # if it is a number, we need to multiply the current string
            # by that number, and push it back to the stack
            # and then clear the current string for the next iteration
            if c.isdigit():
                curr_str = int(c) * curr_str
                stack.append(curr_str)
                curr_str = ""
            # if it is a opening bracket, we need to build the string up to
            # the next closing bracket into the stack, so that we can multiply
            # it by the number that is before the opening bracket
            elif c == "[":
                while stack and stack[-1] != "]":
                    curr_str += stack.pop()
                # remove the remaining ] from the stack, so that next iteration
                # will correctly build the string by finding the proper opening bracket
                stack.pop() 
            else:
                # if it is a character or a closing bracket, we just add it to the stack
                stack.append(c)

        # because it is a stack, the substrings making the string
        # will be in reversed order, e.g., given input s = "3[a]2[bc]"
        # result should be "aaabcbc" but the stack will be ['bcbc', 'aaa'],
        # so if we just join, we get result = "bcbcaaa", however,
        # by reversing the result become "aaabcbc", i.e., the correct one
        return ''.join(reversed(stack))

# solution two using a stack without assuming numbers are always of one digit
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - for the stack because in the worst case, the stack will
# contain all the n characters of the input string
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        num = 0
        for c in reversed(s):
            if c.isdigit():
                # calculate the number for the repeatition
                # if you find another number before the current one
                # you need to add it to the current number, but
                # the current number has to be multiplied by 10 because
                # if you have 3 but the number in the string is 23,
                # you need to calculate it as 2 * 10 + 3 = 23
                # it can also be done in the following way (when num = 0, 0 * 10 = 0):
                # num = (num * 10) + int(c)
                num = int(c) if num == 0 else (num * 10) + int(c)
            elif c == "[":
                while stack and stack[-1] != "]":
                    curr_str += stack.pop()
                # remove the remaining ]
                stack.pop() 
            else:
                curr_str = num * curr_str
                stack.append(curr_str)
                curr_str = ""
                num = 0
                stack.append(c)

        # handle the leftmost num
        curr_str = num * curr_str
        stack.append(curr_str)

        # because it is a stack, so the substrings making the
        # string, will be in reversed order, e.g., s = "3[a]2[bc]"
        # result should be "aaabcbc" but the stack will be ['bcbc', 'aaa']
        # so if we just join, we get result = "bcbcaaa", but by
        # reversing the result become "aaabcbc", i.e., the right one
        return ''.join(reversed(stack))

# solution three using a stack without reverting the string
# and without assuming that numbers are always of one digit
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - for the stack because in the worst case, the stack will
# contain all the n characters of the input string
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr_str = ""
        for c in s:
            if c.isdigit():
                # calculate the number for the repeatition
                # if you find another number before the current one
                # you need to add it to the current number, but
                # the current number has to be multiplied by 10 because
                # if you have 3 but the number in the string is 23,
                # you need to calculate it as 2 * 10 + 3 = 23
                num = (num * 10) + int(c)
            elif c == '[':
                # push the number and current string to the stack
                # in case of a new opening bracket
                stack.append(num)
                stack.append(curr_str)

                # clean the number and current string for the next iteration
                num = 0
                curr_str = ""
            elif c == ']':
                # when we find a closing bracket, we need to
                # build the string the between the opening and closing brackets
                prev_str = stack.pop()
                repeat = stack.pop()
                curr_str = prev_str + curr_str * repeat
            else:
                # append the character to the current string
                # if it is not a number or a bracket
                curr_str += c

        return curr_str