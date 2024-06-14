# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/65729e974d58e556cb200517

'''Problem:
Given a string s containing 0 to 9 digits, create the largest possible palindromic number using the string characters.

A palindromic number reads the same backward as forward.

If it's not possible to form such a number using all digits of the given string, you can skip some of them.

Input: "323211444"
Output: "432141234"
Explanation: This is the largest palindromic number that can be formed from the given digits.

Input: "998877"
Output: "987789"
Explanation: "987789" is the largest palindrome that can be formed.

Input: "54321"
Output: "5"
Explanation: Only "5" can form a valid palindromic number as other digits cannot be paired.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string for the queue
# holding the palindromic number, while the frequency map will have at
# most 10 entries (the numbers from 0 to 9) so it takes O(1) space
from collections import deque

class Solution:
    def largestPalindromic(self, num: str) -> str:
        # build the frequency map of the input string and,
        # at the same time, find the smallest and largest number
        # that we will use to build the palindromic number
        # the frequency map will have at most 10 entries (0 to 9)
        # thus, we could also use an array to store the frequency
        freq = {}
        sm, lg = float('inf'), float('-inf')
        for n in num:
            freq[n] = freq.get(n, 0) + 1
            sm = min(sm, int(n))
            lg = max(lg, int(n))

        # if the largest number is 0 or negative infinity, return 0
        # because if it is 0, then the largest palindromic number is 0
        # if it is -inf, then it means that the input string is empty
        if lg == 0 or lg == float('-inf'):
            return 0

        # find the middle character of the palindromic number
        # as the max character that has an odd frequency and,
        # at the same time, reduce the frequency of odd characters by 1
        # so tht all characters will have even frequencies for the
        # next step where we will build the palindromic number
        # this takes O(1) time because there are at most 10 characters in freq
        middle = ''
        for char, fr in freq.items():
            if fr % 2 != 0:
                middle = max(middle, char)
                freq[char] -= 1

        # initialize a deque to build the palindromic number
        # and if there is a middle character, append it to the deque
        q = deque()
        if middle != '':
            q.append(middle)

        # build the palindromic number by appending the characters
        # to the deque in the order of the smallest to the largest
        # this is because we start building the palindromic number
        # from the middle character and then go to the left and right
        for n in range(sm, lg + 1):
            char = str(n)
            fr = freq.get(char, 0)
            while fr > 0:
                q.append(char)
                q.appendleft(char)
                fr -= 2

            # alternative way to append the characters to the queue
            # it appends half the frequency of the character to the left
            # and half of it to the right
            # fr = int(freq.get(char, 0)) // 2
            # q.extend([char] * fr)
            # q.extendleft([char] * fr)

        # also direclty possible to do
        # return ''.join([char for char in q])
        return ''.join([q.popleft() for _ in range(len(q))])

# solution two
# Complexity:
# O(n) time - where n is the length of the input string
# O(n) space - where n is the length of the input string for the result
class Solution:
    def largestPalindromic(self, num: str) -> str:
        # count the frequency of each digit in the input number
        # usoing a frequency array for digits 0 to 9
        freq = [0] * 10
        for digit in num:
            freq[int(digit)] += 1

        first_half, middle = [], ''
        # iterate from the highest digit (9) to the lowest (0)
        for i in range(9, -1, -1):
            # check if the digit count is odd and middle is empty
            if freq[i] % 2 != 0 and middle == '':
                # assign the largest odd-count digit as the middle digit
                middle = str(i)
            # add half of the even-count digits to the first half
            first_half.extend([str(i)] * (freq[i] // 2))

        # handle special cases
        if not first_half:
            # return the middle digit or "0"
            return middle if middle else '0'
        # case for multiple zeros, e.g., "0000", so the input is all zeros
        elif all(d == '0' for d in first_half):
            return '0'

        # concatenate the first half, middle digit, and the reversed first half
        # thus building the largest palindromic number
        return ''.join(first_half) + middle + ''.join(reversed(first_half))