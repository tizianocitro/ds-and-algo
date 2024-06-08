# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f27ef7ae2ac6893f42b83

'''Problem:
Given an array of numbers sorted in ascending order, find the range of a given number key.
The range of the key will be the first and last position of the key in the array.

Write a function to return the range of the key. If the key is not present return [-1, -1].

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]
'''

# solution one with double binary search
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def findRange(self, arr, key):
        result = [- 1, -1]
        result[0] = self.binarySearch(arr, key)
        # no need to search, if 'key' is not present in the input array
        if result[0] != -1:
            result[1] = self.binarySearch(arr, key, True)
        return result

    # it keeps searching until it finds 'key' at the smallest index if find_max == False
    # or at the biggest index if find_max == True
    def binarySearch(self, arr, key, find_max = False):
        index = -1
        left, right = 0, len(arr) - 1

        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]
            if current == key:
                index = middle
                if find_max:
                    left = middle + 1
                else:
                    right = middle - 1

            if current < key:
                left = middle + 1

            if current > key:
                right = middle - 1

        return index

# solution two with loop in case of matching key
# Complexity:
# O(n) time - where n is the number of elements in the input array
# because we have to iterate through all the numbers to find the range
# in case the input array has contains only numbers equal to the key
# O(1) space
class Solution:
    def findRange(self, arr, key):
        result = [-1, -1]

        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]

            if current == key:
                i = j = middle
                while i >= 0 and arr[i] == key:
                    result[0] = i
                    i -= 1
                while j < len(arr) and arr[j] == key:
                    result[1] = j
                    j += 1
                return result

            if current < key:
                left = middle + 1
            else:
                right = middle - 1

        return result
