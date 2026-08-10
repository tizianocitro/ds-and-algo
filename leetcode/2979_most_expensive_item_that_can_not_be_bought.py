# !code: 2979, !difficult: medium, !from: https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought

'''Problem:
You are given two distinct prime numbers primeOne and primeTwo.
Alice and Bob are visiting a market. The market has an infinite number of items, for any positive integer x there exists an item whose price is x.
Alice wants to buy some items from the market to gift to Bob. She has an infinite number of coins in the denomination primeOne and primeTwo.
She wants to know the most expensive item she can not buy to gift to Bob.

Return the price of the most expensive item which Alice can not gift to Bob.

Constraints:
- 1 < primeOne, primeTwo < 104
- primeOne, primeTwo are prime numbers
- primeOne * primeTwo < 105

Input: primeOne = 2, primeTwo = 5
Output: 3
Explanation: The prices of items which cannot be bought are [1,3]. It can be shown that all items with a price greater than 3 can be bought using a combination of coins of denominations 2 and 5.

Input: primeOne = 5, primeTwo = 7
Output: 23
Explanation: The prices of items which cannot be bought are [1,2,3,4,6,8,9,11,13,16,18,23]. It can be shown that all items with a price greater than 23 can be bought.
'''

# solution one using chicken mcnugget theorem
# Complexity:
# O(1) time
# O(1) space
class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # if the two numbers are coprime, meaning their greatest common divisor is 1
        # then they can form any number greater than or equals to their product minus their sum
        # so all number greater or equal to (primeOne - 1) * (primeTwo - 1) can be formed
        # so the highest number that can not be formed is (primeOne - 1) * (primeTwo - 1) - 1
        # e.g., with primeOne = 2 and primeTwo = 5, we can form all numbers greater than 1 * 4 = 4
        # so the highest number that can not be formed is 4 - 1 = 3
        # e.g., with primeOne = 5 and primeTwo = 7, we can form all numbers greater than 4 * 6 = 24
        # so the highest number that can not be formed is 24 - 1 = 23
        return (primeOne - 1) * (primeTwo - 1) - 1

# solution two using chicken mcnugget theorem with slightly different calculation
# Complexity:
# O(1) time
# O(1) space
class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # if the two numbers are coprime, meaning their greatest common divisor is 1
        # then they can form any number greater than or equals to their product minus their sum
        # so all number greater or equal to (primeOne * primeTwo) - primeOne - primeTwo can be formed
        # e.g., with primeOne = 2 and primeTwo = 5, we can form all numbers greater than 2 * 5 = 10
        # so the highest number that can not be formed is 10 - 2 - 5 = 3
        # e.g., with primeOne = 5 and primeTwo = 7, we can form all numbers greater than 5 * 7 = 35
        # so the highest number that can not be formed is 35 - 5 - 7 = 23
        return (primeOne * primeTwo) - primeOne - primeTwo

# solution three using bottom-up dynamic programming
# Complexity:
# O(primeOne * primeTwo) time - because we are iterating through all numbers from 0 to primeOne * primeTwo
# O(primeOne * primeTwo) space - because we are storing the dp array of size primeOne * primeTwo
class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # the product of the two prime numbers,
        # all numbers greater than this can be formed
        prod = primeOne * primeTwo

        dp = [False] * prod
        # base cases, the two prime numbers can be formed for sure
        dp[primeOne] = True
        dp[primeTwo] = True

        for num in range(prod):
            dp[num] = dp[num] or dp[num - primeOne] or dp[num - primeTwo]

        # find the highest number that can not be formed
        # by iterating from the highest number to 0
        for num in range(prod - 1, -1, -1):
            # if the number can not be formed
            # then this is the highest number that we can not form
            if not dp[num]:
                return num

        # we will never reach this because we
        # will always find it in the loop
        return prod - primeOne - primeTwo