# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a0a649ef4e913a2e2bf4cd

'''Problem:
Every non-negative integer N has a binary representation, for example, 8 can be represented as "1000" in binary and 7 as "0111" in binary.

The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1.
For example, the binary complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

Input: 8
Output: 7
Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.

Input: 10
Output: 5
Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5 in base-10.
'''

# solution one
# Complexity:
# O(n) time - where n is the number of bits in the input number
# O(1) space
class Solution:
    def bitwiseComplement(self, num):
        # count number of total bits in num
        # we need to copy num in because we will shift the bits
        bit_count = 0
        n = num
        while n > 0:
            bit_count += 1
            n = n >> 1

        # (2^bit_count) - 1 will provide the highest number that
        # is representabe with that number of bits, which will always be
        # represented with all bits set to 1. E.g., with bit_count = 4,
        # 2^4 = 16 -> 16 - 1 = 15 -> bin(15) = 1111
        all_bits_set = pow(2, bit_count) - 1

        # the complement of a number is complement = num ^ all_bits_set
        # because the xor of the number with a set of bits all set to 1
        # will produce the complement of the number. E.g., with num = 8,
        # bit_count = 4 -> all_bits_set = 1111 -> bin(8) == 1000
        # -> 1000 ^ 1111 = 0111 -> int('0111', 2) = 7
        return num ^ all_bits_set

