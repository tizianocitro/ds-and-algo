# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a0a41ebc8d0eddc47362f7

'''Problem:
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once.
Find the two numbers that appear only once.

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]

Input: [2, 1, 3, 2]
Output: [1, 3]
'''

'''Solution
1. Take XOR of all numbers in the given array to get the XOR of num1 and num2, calling this XOR as n1xn2.
2. Find any bit which is set in n1xn2. We can take the rightmost bit which is '1'. Let’s call this rightmostSetBit.
3. Iterate through all numbers of the input array to partition them into two groups based on rightmostSetBit.
4. Take XOR of all numbers in both the groups separately. Both these XORs are our required numbers.
'''

# solution one
# Complexity:
# O(n) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def findSingleNumbers(self, nums):
        # get the XOR of the all the numbers
        # assuming n1 and n2 are the two single numbers
        # if we do XOR of all elements of the given array,
        # we will be left with XOR of n1 and n2 as all other numbers
        # will cancel each other because all of them appeared twice
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num

        # get the rightmost bit that is '1'
        # as we know that n1 and n2 are two different numbers,
        # they should have at least one bit different between them
        # if a bit in n1xn2 is ‘1’, this means that n1 and n2 have different bits in that place,
        # as we know that we can get ‘1’ only when we do XOR of two different bits
        # we can find any but let's take the rightmost bit which is ‘1’
        rightmost_set_bit = 1
        while (rightmost_set_bit & n1xn2) == 0:
            rightmost_set_bit = rightmost_set_bit << 1
        n1, n2 = 0, 0

        # partition all numbers in the given array into two groups based on the selected bit
        # one group will have all those numbers with that bit set to ‘0’ and the other
        # with the bit set to ‘1’. This will ensure that n1 will be in one group and
        # n2 will be in the other. We can take XOR of all numbers in each group separately
        # to get n1 and n2, as all other numbers in each group will cancel each other 
        for num in nums:
            # the bit is set
            if (num & rightmost_set_bit) != 0:
                n1 ^= num
            else: # the bit is not set
                n2 ^= num

        return [n1, n2]