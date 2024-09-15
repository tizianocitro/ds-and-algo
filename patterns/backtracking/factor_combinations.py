# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/factor-combinations-medium

'''Problem:
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.

Given an integer n, return all possible combinations of its factors.
You may return the answer in any order.

Input: n = 8  
Output: [[2, 2, 2], [2, 4]]

Input: n = 20  
Output: [[2, 2, 5], [2, 10], [4, 5]]  
'''

# solution one
# Complexity:
# O(n^sqrt(n)) time - where n is the input number because we can't have more than O(n) factors of a number n
# thus, the backtracking function can be called a maximum of O(n) times recursively.
# The for loop iterates a maximum of O(sqrt(n)) times. This means that the overall time complexity is O(n^sqrt(n)) or O(n^1.5)
# O(logn) space - where n is the input number because the maximum depth of the recursion tree can go up to logn
class Solution:
    def getFactors(self, n):
        if n < 2:
            return []

        # the list of all factors
        factors = []
        self.backtrack(n, 2, [], factors)
        return factors

    def backtrack(self, n, start, current, factors):
        # iterate through all integers i from start to the square root of n + 1
        # this loop is used to find all the factors of the input number n
        for i in range(start, int(n**0.5) + 1):
            # if n is not divisible by i, i cannot be a factor of n
            if n % i != 0:
                continue

            # found a factor, append it to the list of factors
            current.append(i)

            # append the current factors and the corresponding factor of n // i
            factors.append(list(current + [n // i]))
            # recursively call the function with n // i as the new input,
            # wiht i as the new start value
            self.backtrack(n // i, i, current, factors)

            # pop the last element from current to backtrack and find other factors
            current.pop()

# solution two
# Complexity:
# O(n^2) time - where n is the input number because we can't have more than O(n) factors of a number n
# thus, the backtracking function can be called a maximum of O(n) times recursively.
# The for loop iterates a maximum of O(n // i) times.
# O(logn) space - where n is the input number because the maximum depth of the recursion tree can go up to logn
class Solution:
    def getFactors(self, n):
        if n < 2:
            return []

        factors = []
        self.backtrack(n, 2, n, [], factors)
        return factors

    def backtrack(self, n, start, end, current, factors):
        # if n is not divisible by i, i cannot be a factor of n
        if n == 1:
            factors.append(list(current))
            return

        # this loop is used to find all the factors of the input number n
        for i in range(start, end):
            if n % i != 0:
                continue

            # found a factor, append it to the list of factors
            current.append(i)

            # recursively call the function with n // i as the new input,
            # wiht i as the new start value
            self.backtrack(n // i, i, (n // i) + 1, current, factors)

            # pop the last element from current to backtrack and find other factors
            current.pop()