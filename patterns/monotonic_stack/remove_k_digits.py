# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64c15ba01e1cb44fbe63ddc3

'''Problem:
Given a non-negative integer represented as a string num and an integer k, delete k digits from num to obtain the smallest possible integer.
Return this minimum possible integer as a string.

Input: num = "1432219", k = 3
Output: "1219"
Explanation: The digits removed are 4, 3, and 2 forming the new number 1219 which is the smallest.

Input: num = "10200", k = 1
Output: "200"
Explanation: Removing the leading 1 forms the smallest number 200.

Input: num = "1901042", k = 4
Output: "2"
Explanation: Removing 1, 9, 1, and 4 forms the number 2 which is the smallest possible.
'''

'''Solution:
The idea is to keep removing the peak digit from the number num.
The peak digit in a number is a digit after which the next digit is smaller.
By doing so, we are always trying to minimize the leftmost digit which will give us the smallest possible number.

We will use a monotonically increasing stack to keep track of the decreasing peak digits.

1. Initialize an empty stack.
2. Iterate over the digits in num.
3. For each digit:
    1. While k is greater than 0, the stack is not empty and the current digit is smaller than the top digit on the stack,
       pop the top digit from the stack and decrease k by 1.
    2. Push the current digit onto the stack.
4. If k is still greater than 0, pop k digits from the stack.
5. Build the result string from the digits in the stack. Remove the leading zeros.
6. If the result string is empty, return "0". Otherwise, return the result string.
'''
# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - because we are using a stack to store the digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        # minimize the leftmost digits with respect to the maximum number of skips
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # truncate the remaining K digits
        stack = stack[:-k] if k > 0 else stack
        
        # remove any leading zeros
        return "".join(stack).lstrip("0") or "0"