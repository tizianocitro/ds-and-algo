# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/decode-ways-medium

'''Problem:
You have given a string that consists only of digits.
This string can be decoded into a set of alphabets where '1' can be represented as 'A', '2' as 'B', ... , '26' as 'Z'.
The task is to determine how many ways the given digit string can be decoded into alphabets.

Input: "121"
Output: 3
Explanation: The string "121" can be decoded as "ABA", "AU", and "LA".

Input: "27"
Output: 1
Explanation: The string "27" can only be decoded as "BG".

Input: "110"
Output: 1
Explanation: The string "110" can only be decoded as "JA".
'''

# solution one using dynamic programming
# Complexity:
# O(n) time - where n is the number of digits in the string
# O(1) space
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s.startswith('0'):
            return 0

        if n == 1:
            return 1

        # two variables to store results of sub-problems
        # the first s[0] will always have only one way to decode, so prev = 1
        # the second s[1] will have at least one way to decode if it is not zero, so current = 1
        prev, current = 1, 1
        for i in range(1, len(s)):
            temp = 0

            # if current character is not '0', it can be decoded on its own
            if s[i] != '0':
                temp = current

            # check if two characters can be decoded together
            # alternatively, you can do as follows:
            # two_digit_num = (int(s[i - 1]) * 10) + int(s[i])
            # the used approach takes the substring from i - 1 to i
            # and the converts it to integer:
            two_digit_num = int(s[i - 1:i + 1])

            # the two characters can be decoded together if
            # they are between 10 and 26, because the last character mapping is 26 (z)
            if 10 <= two_digit_num <= 26:
                temp += prev

            prev = current
            current = temp

        return current

# solution two using top-down dynamic programming with memoization
# Complexity:
# O(n) time - where n is the number of digits in the string
# with memoization, each subproblem (decoding from index i to the end of the string) is solved at most once.
# since the function countDecodingWays() is only called once per index, the total number of recursive calls is linear, corresponding to the length n of the string.
# O(n) space - where n is the number of digits in the string for the recursion stack and the memoization dictionary
class Solution:
    def numDecodings(self, s: str) -> int:
        # these three checks could be avoided because
        # the solution handles them already
        if len(s) == 0 or s.startswith('0'):
            return 0

        if len(s) == 1:
            return 1

        # momoization dictionary to store the results of sub-problems
        self.memo = {}
        return self.countDecondingWays(s, 0)

    def countDecondingWays(self, s, ix):
        n = len(s)

        # backtrack when you end up on a zero
        # because there is no way to decode a zero
        # no character mapping starts with zero
        if ix <= n - 1 and s[ix] == '0':
            return 0

        # if the result is already in the memoization dictionary
        if ix in self.memo:
            # return the result directly to avoid recomputation
            return self.memo[ix]

        # if you reach the end of the string (when recursion is on ix + 2)
        # or the last character (when recursion is on ix + 1),
        # then you have found a way to decode the string
        if ix == n - 1 or ix == n:
            return 1

        count = 0

        # try deconding with the next character
        count += self.countDecondingWays(s, ix + 1)

        # try decoding two characters but only if the two characters
        # are less than 27, because the last character mapping is 26 (z)
        two_digit_num = (int(s[ix]) * 10) + int(s[ix + 1])
        if two_digit_num < 27:
            count += self.countDecondingWays(s, ix + 2)

        # store the result in the memoization dictionary for future use
        self.memo[ix] = count
        return count

# solution three using top-down dynamic programming
# this also uses a class level variable to store the result
# Complexity:
# O(2^n) time - where n is the number of digits in the string
# because for each index in the strinf we might need to make two recursive calls
# O(n) space - where n is the number of digits in the string for the recursion stack 
class Solution:
    def numDecodings(self, s: str) -> int:
        # these three checks could be avoided because
        # the solution handles them already
        if len(s) == 0 or s.startswith('0'):
            return 0

        if len(s) == 1:
            return 1

        self.decode_ways = 0
        self.countDecondingWays(s, 0)
        return self.decode_ways

    def countDecondingWays(self, s, ix):
        n = len(s)

        # backtrack when you end up on a zero
        # because there is no way to decode a zero
        # no character mapping starts with zero
        if ix <= n - 1 and s[ix] == '0':
            return

        # if you reach the end of the string (when recursion is on ix + 2)
        # or the last character (when recursion is on ix + 1),
        # then you have found a way to decode the string
        if ix == n - 1 or ix == n:
            self.decode_ways += 1
            return

        # try deconding with the next character
        self.countDecondingWays(s, ix + 1)

        # try decoding two characters but only if the two characters
        # are less than 27, because the last character mapping is 26 (z)
        two_digit_num = (int(s[ix]) * 10) + int(s[ix + 1])
        if two_digit_num < 27:
            self.countDecondingWays(s, ix + 2)
