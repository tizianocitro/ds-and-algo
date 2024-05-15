# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1d49473a7d4466d460b87

'''Problem:
Given a number array sorted in ascending order and two integers k and x, find k closest numbers to x in the array.
Return the numbers in the sorted order. the number x is not necessarily present in the array.

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
'''

# solution one
# Complexity:
# O(nlogk) time - where n is the length of the input array
# O(k) space - where k is the number of elements we keep into the heap
from heapq import *

class Solution:
    def findClosestElements(self, arr, k, x):
        min_heap = []

        for i in range(k):
            heappush(min_heap, arr[i])

        # this is based on the fact that the array is sorted, thus
        # the further we are before or after X, the higher the distance will get.
        # given so, we can start from the kth element and compare
        # the distance between the current element and x with
        # the distance between the first element in the heap and x
        # if the current element is closer, we remove the first element
        # from the heap and add the current element, mantaining also the asc order
        for i in range(k, len(arr)):
            el = arr[i]
            if abs(x - el) < abs(x - min_heap[0]):
                heappop(min_heap)
                heappush(min_heap, el)

        return min_heap

# solution two with binary search
# Complexity:
# O(logn + klogk) time - where n is the length of the input array and k is the number of elements we keep into the heap
# O(k) space - where k is the number of elements we keep into the heap
from heapq import *

class Solution:
    def findClosestElements(self, arr, k, x):
        index = self.binary_search(arr, x)
        low, high = index - k, index + k

        # 'low' should not be less than zero
        low = max(low, 0)
        # 'high' should not be greater the size of the array
        high = min(high, len(arr) - 1)

        minHeap = []

        # add all candidate elements to the min heap,
        # sorted by their absolute difference from 'X'
        for i in range(low, high + 1):
            heappush(minHeap, (abs(arr[i] - x), arr[i]))

        # we need the top 'K' elements having smallest difference from 'X'
        result = []
        for _ in range(k):
            result.append(heappop(minHeap)[1])

        # this will take O(klogk)
        result.sort()
        return result

    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # low will point to the smallest element larger than 'key'
        # but we want to start from the largest element smaller than 'key'
        if low > 0:
            return low - 1
        return low

# solution two using two pointers
# Complexity:
# O(n + k) time - where n is the length of the input array and k is input k
# O(k) space - where k is the number of elements we keep into the queue
from collections import deque

class Solution:
    def findClosestElements(self, arr, k, x):
        result = deque()

        # binary search to find the index of the element closest to X
        index = self.binary_search(arr, x)
        leftPointer, rightPointer = index, index + 1
        n = len(arr)

        for _ in range(k):
            # check if there are elements on both sides of the chosen element
            if leftPointer >= 0 and rightPointer < n:
                diff1 = abs(x - arr[leftPointer])
                diff2 = abs(x - arr[rightPointer])

                # choose the element with the smaller absolute difference
                if diff1 <= diff2:
                    # add the left element to the result
                    result.appendleft(arr[leftPointer])
                    leftPointer -= 1
                else:
                    # add the right element to the result
                    result.append(arr[rightPointer])
                    rightPointer += 1
            # if there are no elements on one side, add elements from the other side
            elif leftPointer >= 0:
                result.appendleft(arr[leftPointer])
                leftPointer -= 1
            elif rightPointer < n:
                result.append(arr[rightPointer])
                rightPointer += 1

        return result

    # binary search method to find the index of the closest element to the target
    def binary_search(self, arr,  target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if low > 0:
            return low - 1
        return low
