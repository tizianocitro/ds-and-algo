''' Problem:
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits,
leads us to the number 1. All other (not-happy) numbers will never reach 1.
Instead, they will be stuck in a cycle of numbers that does not include 1.

Given a positive number n, return true if it is a happy number otherwise return false.

Input: 23
Output: true (23 is a happy number)
Explanations: Here are the steps to find out that 23 is a happy number:
2^2 + 3^2 = 4 + 9 = 13
1^2 + 3^2 = 1 + 9 = 10
1^2 + 0^2 = 1 + 0 = 1

Input: 12
Output: false (12 is not a happy number)
Explanations: Here are the steps to find out that 12 is not a happy number:
1^2 + 2^2 = 1 + 4 = 5
5^2 = 25
2^2 + 5^2 = 4 + 25 = 29
2^2 + 9^2 = 4 + 81 = 85
8^2 + 5^2 = 64 + 25 = 89
8^2 + 9^2 = 64 + 81 = 145
1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
4^2 + 2^2 = 16 + 4 = 20
2^2 + 0^2 = 4 + 0 = 4
4^2 = 16
1^2 + 6^2 = 1 + 36 = 37
3^2 + 7^2 = 9 + 49 = 58
5^2 + 8^2 = 25 + 64 = 89

Step 13 leads us back to step 5 as the number becomes equal to 89,
this means that we can never reach 1 because we are stuck in a loop.
'''

# solution one with fast and slow pointers
# Complexity:
# O(logn) time - because the findSquareSum function iterates through the digits of the number,
# and the number of digits in the worst case is log(n) (where n is the value of the input number)
# O(1) space
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def find(self, num):
        slow, fast = num, num
        while True:
            slow = self.findSquareSum(slow)
            fast = self.findSquareSum(self.findSquareSum(fast))
            if slow == fast:
                break
        # see if the cycle is stuck on the number 1, if it is, the number is happy
        return slow == 1

    def findSquareSum(self, num):
        sum = 0
        
        # num > 0 is when all digits have been processed
        while num > 0:
            # Calculate the last digit of num using the modulus operator (num % 10).
            # This gives the remainder when dividing num by 10, which corresponds to the last digit.
            digit = num % 10
            sum += digit * digit
            
            # Update num by removing its last digit using integer division (num //= 10).
            # This operation effectively removes the last digit from num.
            num //= 10
        return sum

# solution two with hash map
# Complexity:
# O(dk) time - where d is the number of digits in the number and k is the number of ierations
# O(d) space - where d is the number of digits in the number
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def find(self, num):
        results = set([num])
        current = num

        while True:
            digits = str(current)
            sum = 0
            for i in range(len(digits)):
                sum += int(digits[i]) ** 2
            
            if sum == 1:
                return True
            if sum in results:
                return False
            
            results.add(sum)
            current = sum
