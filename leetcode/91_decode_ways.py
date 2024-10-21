# !code: 91, !difficulty: medium, !from: https://leetcode.com/problems/decode-ways/

'''Problem:
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
- "1" -> 'A'
- "2" -> 'B'
- ...
- "25" -> 'Y'
- "26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message
because some codes are contained in other codes ("2" and "5" vs "25").
For example, "11106" can be decoded into:
- "AAJF" with the grouping (1, 1, 10, 6)
- "KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it.
If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s)

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.
'''

# solution one using dynamic programming
# Complexity:
# O(n) time - where n is the number of digits in the string
# O(1) space
class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0

        # two variables to store results of sub-problems
        prev, current = 1, 1
        for i in range(1, len(s)):
            temp = 0

            # if current character is not '0', it can be decoded on its own
            # the first s[0] will always have only one way to decode, so prev = 1
            # the second s[1] will have at least one way to decode if it is not zero, so current = 1
            if s[i] != '0':
                temp += current

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
