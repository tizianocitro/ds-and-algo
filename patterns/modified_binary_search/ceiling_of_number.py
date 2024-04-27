# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1fd54e4f288d4a83ab44

'''Problem:
Given an array of numbers sorted in an ascending order, find the ceiling of a given number key.
The ceiling of the key will be the smallest element in the given array greater than or equal to the key.

Write a function to return the index of the ceiling of the key. If there isn’t any ceiling return -1.

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to 6 is 6 having index 1.

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to 12 is 15 having index 4.

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to 17 in the given array.

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to -1 is 4 having index 0.
'''

# solution one with a ceil variable
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

            if current == key:
                return middle
            
            if current > key:
                ceil = middle
                right = middle - 1
            else:
                left = middle + 1

        return ceil

# solution two using left pointer position
# it is based on the fact that since the loop is running until 'start <= end',
# so at the end of the while loop, 'start == end + 1' we are not able to find the element in the given array,
# so the next big number will be arr[start]
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def searchCeilingOfANumber(self, arr, key):
        n = len(arr)
        # if the key is bigger than the biggest element
        # it is no part of the array, so just return -1
        if key > arr[n - 1]:
            return -1

        start, end = 0, n - 1
        while start <= end:
            middle = start + (end - start) // 2
            if key < arr[middle]:
                end = middle - 1
            elif key > arr[middle]:
                start = middle + 1
            else: # found the key
                return middle

        # since the loop is running until 'start <= end', so at the end of the while loop, 
        # 'start == end + 1' we are not able to find the element in the given array, so the next
        # big number will be arr[start]
        return start
