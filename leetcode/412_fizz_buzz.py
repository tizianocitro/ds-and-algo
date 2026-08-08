# !code: 412, !difficulty: easy, !from: https://leetcode.com/problems/fizz-buzz

'''Problem:
Given an integer n, return a string array answer (1-indexed) where:
- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.

Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
'''

# solution one
# Complexity:
# O(n) time - where n is the input number
# O(n) space - where n is the input number for the result array
class Solution:
    def fizzBuzz(self, n):
        res = []
        for num in range(1, n + 1):
            # in alternative to % 15, you can use % 3 and % 5, as:
            # if num % 3 == 0 and num % 5 == 0:
            if num % 15 == 0:
                res.append("FizzBuzz")
            elif num % 3 == 0:
                res.append("Fizz")
            elif num % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(num))
        return res