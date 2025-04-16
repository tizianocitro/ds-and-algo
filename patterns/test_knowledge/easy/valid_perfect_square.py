# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/valid-perfect-square-easy

'''Problem:
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Input: 49
Output: true
Explanation: (7 * 7) equals 49.

Input: 55
Output: false
Explanation: There is no integer whose square is 55.

Input: 0
Output: false
Explanation: 0 is not considered a perfect square.
'''

# solution one using binary search
# Complexity:
# O(log(n)) time - where n is the size of the search space
# O(1) space
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 9 is not a perfect square
        if num == 0:
            return False
        # 1 is always a perfect square
        if num == 1:
            return True

        # alternatively to the two ifs above, we can use
        # if num < 2:
        #     return num == 1

        # consider all numbers from 0 to half of the number
        left, right = 0, num // 2
        while left <= right:
            # if the middle is equal to the number, then
            # the number is a perfect square
            middle = (left + right) // 2
            pw = middle ** 2
            if pw == num:
                return True
            if pw < num:
                left = middle + 1 
            else:
                right = middle - 1

        return False

# solution two
# Complexity:
# O(n) time - where n is the length of the input list
# O(1) space
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if it's 1 then it's a perfect square
        if num == 1:
            return True

        # for each number from 2 to half of the number, check whether the number
        # is a perfect square by dividing the number by the current number and
        # checking whether the result is equal to the current number and the remainder is 0
        for n in range(2, (num // 2) + 1):
            if num // n == n and num % n == 0:
                return True 

        return False
