# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639c8fe6165a22967d308303

'''Problem:
Given an array of numbers and a number k, find the median of all the k sized sub-arrays (or windows) of the array.

Example:
Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Let's consider all windows of size 2:
[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
'''

# solution one
# Complexity:
# O(nklogk) time - where n is the number of elements in the array, and k is the size of the window
# O(k) space - where k is the size of the window, to store the numbers in the heaps
from heapq import *

class Solution:
    def findSlidingWindowMedian(self, nums, k):    
        result = []
        min_heap, max_heap = [], []
        start = 0

        # takes O(n) time, where each heappush and heappop take O(logk) time
        for end in range(len(nums)):
            if not max_heap or nums[end] <= -max_heap[0][0]:
                heappush(max_heap, (-nums[end], end))
            else:
                heappush(min_heap, (nums[end], end))
            
            self.balanceHeaps(max_heap, min_heap)
            
            if end >= k - 1:
                if len(max_heap) == len(min_heap):
                    result.append((-max_heap[0][0] + min_heap[0][0]) / 2.0)
                else:
                    result.append((-max_heap[0][0]) / 1.0)
                
                self.removeFromHeap(max_heap, min_heap, start)
                start += 1

        return result

    # takes O(klogk) time, because we are iterating through the k elements in the heap
    # and we are heapifying the heap which takes O(logk) time
    def removeFromHeap(self, max_heap, min_heap, pos):
        for i in range(len(max_heap)):
            if max_heap[i][1] == pos:
                del max_heap[i]
                heapify(max_heap)
                break
        
        for i in range(len(min_heap)):
            if min_heap[i][1] == pos:
                del min_heap[i]
                heapify(min_heap)
                break

        self.balanceHeaps(max_heap, min_heap)

    # takes O(logk) time, because we are heappushing and heappopping the heap
    def balanceHeaps(self, max_heap, min_heap):
        if len(max_heap) > len(min_heap) + 1:
            num, i = heappop(max_heap)
            heappush(min_heap, (-num, i))
        elif len(max_heap) < len(min_heap):
            num, i = heappop(min_heap)
            heappush(max_heap, (-num, i))

# solution two with heap.index to get element index instead of storing the index of the elements and iterating through the heap
# Complexity:
# O(nk) time - where n is the number of elements in the array, and k is the size of the window
# O(k) space - where k is the size of the window, to store the numbers in the heaps
from heapq import *
import heapq

class Solution:
    def findSlidingWindowMedian(self, nums, k):    
        result = []
        min_heap, max_heap = [], []
        start = 0

        # takes O(n) time, where each heappush and heappop take O(logk) time,
        # balanceHeaps takes O(logk) time, and removeFromHeap takes O(k) time
        # so, the total time complexity is O(nk)
        for end in range(len(nums)):
            if not max_heap or nums[end] <= -max_heap[0]:
                heappush(max_heap, -nums[end])
            else:
                heappush(min_heap, nums[end])

            self.balanceHeaps(max_heap, min_heap)

            if end >= k - 1:
                if len(max_heap) == len(min_heap):
                    result.append((-max_heap[0] + min_heap[0]) / 2.0)
                else:
                    result.append(-max_heap[0] / 1.0)
                
                if nums[start] <= -max_heap[0]:
                    self.removeFromHeap(max_heap, -nums[start])
                else:
                    self.removeFromHeap(min_heap, nums[start])

                self.balanceHeaps(max_heap, min_heap)
                start += 1

        return result

    # takes O(k) time, because we are iterating through the k elements in the heap
    def removeFromHeap(self, heap, el):
        pos = heap.index(el)
        
        # copy the last element of the heap to the el index
        heap[pos] = heap[-1]

        # decrement the heap size by removing the element
        del heap[-1]

        # handle the case where the element being removed was not the last element of the heap
        # adjust the position of the element while maintaining the heap property.
        # we can use heapify to readjust the elements but that would be O(k),
        # instead, we will adjust only one element which will O(logk)
        if pos < len(heap):
            # adjusts the heap from the bottom up, ensuring that the element at position pos satisfies the heap property
            heapq._siftup(heap, pos)
            # adjusts the heap from the top down, ensuring that the element at position pos satisfies the heap property
            heapq._siftdown(heap, 0, pos)

    def balanceHeaps(self, max_heap, min_heap):
        if len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(max_heap) < len(min_heap):
            heappush(max_heap, -heappop(min_heap))


