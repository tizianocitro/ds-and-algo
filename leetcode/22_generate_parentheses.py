# !code: 22, !difficulty: medium, !from: https://leetcode.com/problems/generate-parentheses/

'''Problem:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Constraints:
1 <= n <= 8

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
'''

# solution one using subsets (cleaner version of solution two)
# Complexity:
# O(4^n/√n) time - where n is the number of pairs of parentheses, it comes from the Catalan number,
# which counts the number of valid sequences of well-formed parentheses
# O(n) space - where n is the number of pairs of parentheses because the queue will have at most 2n elements
from collections import deque

class Combination:
    def __init__(self, str='', open=0, close=0):
        self.str = str
        self.open = open
        self.close = close

class Solution:
    def generateParenthesis(self, n: int):
        result = []

        q = deque()
        q.append(Combination('', 0, 0))

        while q:
            current_combinations = len(q)

            for _ in range(current_combinations):
                combination = q.popleft()
                if combination.open == n and combination.close == n:
                    result.append(combination.str)
                else:
                    if combination.open < n:
                        new_combination = Combination(combination.str + '(', combination.open + 1, combination.close)
                        q.append(new_combination)

                    if combination.close < combination.open:
                        new_combination = Combination(combination.str + ')', combination.open, combination.close + 1)
                        q.append(new_combination)

        return result

# solution two using subsets
# Complexity:
# O(4^n/√n) time - where n is the number of pairs of parentheses, it comes from the Catalan number,
# which counts the number of valid sequences of well-formed parentheses
# O(n) space - where n is the number of pairs of parentheses because the queue will have at most 2n elements
from collections import deque

class Combination:
    def __init__(self, str='', open=0, close=0):
        self.str = str
        self.open = open
        self.close = close

class Solution:
    def generateParenthesis(self, n: int):
        result = []

        q = deque()
        q.append(Combination('', 0, 0))

        while q:
            current_combinations = len(q)

            for _ in range(current_combinations):
                combination = q.popleft()

                if combination.open < n:
                    new_combination = Combination(
                        combination.str + '(', combination.open + 1, combination.close,
                    )
                    if new_combination.open == n and new_combination.close == n:
                        result.append(new_combination.str)
                    else:
                        q.append(new_combination)

                if combination.close < combination.open:
                    new_combination = Combination(
                        combination.str + ')', combination.open, combination.close + 1,
                    )
                    if new_combination.open == n and new_combination.close == n:
                        result.append(new_combination.str)
                    else:
                        q.append(new_combination)

        return result
