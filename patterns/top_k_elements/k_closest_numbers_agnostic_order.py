# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1d49473a7d4466d460b87

'''Problem:
Given a number array and two integers k and x, find k closest numbers to x in the array.
Return the numbers in the sorted order. the number x is not necessarily present in the array.
The array is either sorted in ascending or descending order.

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]

Input: [9, 6, 5, 4, 2], K = 3, X = 10
Output: [5, 6, 9]
'''

# solution one using order-agnostic binary search
# Complexity:
# O(logn + k) time - where n is the length of the input array and k is the number of elements we keep into the heap
# O(k) space - where k is the number of elements we keep into the heap
from heapq import *

class Solution:
    def findClosestElements(self, arr, k, x):
        min_heap = []    
        is_asc = arr[0] <= arr[len(arr) - 1]

        left, right = self.binarySearch(arr, x, is_asc)
        if left >= len(arr):
            return sorted(arr[left - k:left])
        if right < 0:
            return sorted(arr[:k])

        if is_asc:
            while right > 0 and len(min_heap) < k:
                heappush(min_heap, arr[right])
                right -= 1
            while left < len(arr) and len(min_heap) < k:
                heappush(min_heap, arr[left])
                left += 1
            while left < len(arr) and abs(arr[left] - x) < abs(min_heap[0] - x):
                heappop(min_heap)
                heappush(min_heap, arr[left])
                left += 1
        else:
            while left < len(arr) and len(min_heap) < k:
                heappush(min_heap, arr[left])
                left += 1
            while right > 0 and len(min_heap) < k:
                heappush(min_heap, arr[right])
                right -= 1
            while right > 0 and abs(arr[right] - x) < abs(min_heap[0] - x):
                heappop(min_heap)
                heappush(min_heap, arr[right])
                right -= 1

        return min_heap

    def binarySearch(self, arr, x, is_asc):
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]

            if is_asc:
                if current < x:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if current < x:
                    right = middle - 1
                else:
                    left = middle + 1

        return left, right

