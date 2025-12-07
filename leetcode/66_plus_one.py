# !code: 66, !difficulty: easy, !from: https://leetcode.com/problems/plus-one/

'''Problem:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Constraints:
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322. Thus, the result should be [4,3,2,2].

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be [1,0].
'''

# solution one
# Complexity:
# O(n) time - where n is the number of digits in the input list
# O(1) space
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            # if the digit is 9, set it to 0 and continue to the next digit
            if digits[i] == 9:
                digits[i] = 0
                continue

            # we found a digit that is not 9, so we can just increment it by 1
            # and break the execution because we don't need to update the rest of the digits
            digits[i] += 1
            break

        # this can happen when all digits are 9
        # or when the input is [0]
        if digits[0] == 0:
            # update the first digit to 1 and just add the removed 0 to the end
            digits[0] = 1
            digits.append(0)

        return digits