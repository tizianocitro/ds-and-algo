# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1fd54e4f288d4a83ab44/discuss/ceiling-of-a-number-medium/6448e6e46b9bfe6e0d0b3518 (the comment)

'''Problem:
Given an array of numbers sorted in an ascending order, find the ceiling of a given number key.
The ceiling of the key will be the smallest element in the given array greater than or equal to the key.

Write a function to return the index of the ceiling of the key.
If there isn’t any ceiling return -1.
Return the smallest index in case of repeated ceilings.

Input: [4, 6, 6, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to 6 at the smallest index is 6 having index 1.

Input: [4, 5, 5, 7, 7, 10], key = 6
Output: 3
Explanation: The smallest number greater than or equal to 6 at the smallest index is 7 having index 3.
'''

# solution one using a ceil variable
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def searchCeilingOfANumber(self, arr, key):
        ceil = -1

        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]
            
            if current >= key:
                # if the ceil is not set or if the new ceil
                # is at a smaller index than the current ceil,
                # which since the array is sorted,
                # it will equal or smaller than the current ceil
                if ceil == -1 or middle < ceil:
                    ceil = middle
                    right = middle - 1
            else:
                left = middle + 1

        return ceil
