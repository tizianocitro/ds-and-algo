# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd6e48b9c2c77f772d447a

'''Problem:
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given key.

In case of multiple elements at the minimum difference, return the one that appears first in the array.

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 

Input: [4, 6, 10], key = 4
Output: 4

Input: [1, 3, 8, 10, 15], key = 12
Output: 10

Input: [4, 6, 10], key = 17
Output: 10
'''

# solution one leveraging left and right positions
# Complexity:
# O(logn) time - where n is the number of elements in the array
# O(1) space
class Solution:
    def searchMinDiffElement(self, arr, key):
        # if the key is smaller than the first element, return the first element
        if key < arr[0]:
            return arr[0]

        # if the key is bigger than the last element, return the last element
        n = len(arr)
        if key > arr[n - 1]:
            return arr[n - 1]

        start, end = 0, n - 1
        while start <= end:
            middle = (start + end) // 2
            if key < arr[middle]:
                end = middle - 1
            elif key > arr[middle]:
                start = middle + 1
            else:
                return arr[middle]

        # at the end of the while loop, 'start == end+1'
        # start and end are the elements closest to 'key',
        # start points to the element bigger than the 'key',
        # end points to the element smaller than the 'key'
        # in case we are not able to find the element in the given array
        # return the element which is closest to the 'key'
        if (arr[start] - key) < (key - arr[end]):
            return arr[start]
        return arr[end]


# solution two with min_* variables
# Complexity:
# O(logn) time - where n is the number of elements in the array
# O(1) space
class Solution:
    def searchMinDiffElement(self, arr, key):
        min_diff_el = -1
        min_distance = float('inf')

        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]

            local_distance = float('inf')
            if current >= key:
                local_distance = current - key
                right = middle - 1
            else:
                local_distance = key - current
                left = middle + 1
            
            if local_distance <= min_distance:
                if local_distance == min_distance and current > min_diff_el:
                    continue

                min_diff_el = current
                min_distance = local_distance

        return min_diff_el
