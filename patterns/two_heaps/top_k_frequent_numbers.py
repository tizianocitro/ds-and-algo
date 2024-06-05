# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1d04a19e6a3ce13cedede

'''Problem:
Given an unsorted array of numbers, find the top K frequently occurring numbers in it.
It is guaranteed that the answer is unique and K is in the range [1, the number of unique elements in the array].

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
'''

# solution one with hash map, it has better time complexity than solution two but worse space complexity
# Complexity:
# O(nlogk) time - where n is the number of elements in the array and k is the number in input
# O(n) space - to store the numbers in the map, the heap will have only k elements and k < n
from heapq import *

class Solution:
    def findTopKFrequentNumbers(self, nums, k):
        # find the frequency of each number, it takes O(n) time
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        top_numbers = []

        # go through all numbers of the map and push them in the heap, which 
        # will have top k frequent numbers. If the heap size is more than k,
        # we remove the smallest (i.e., the top) number
        # this takes O(nlogk) time because we are iterating through the map (o(n) time)
        # and we are pushing and popping the numbers in the heap (O(logk) time)
        for num, frequency in frequencies.items():
            heappush(top_numbers, (frequency, num))
            if len(top_numbers) > k:
                heappop(top_numbers)

        return [heappop(top_numbers)[1] for _ in range(k)]

# solution two with sorting, it has worse time complexity than solution one but better space complexity
# Complexity:
# O(nlogn) time - where n is the number of elements in the array because of sorting
# O(k) space - to store the numbers in the heap which will have up to k elements
from heapq import *
import heapq

class Solution:
    def findTopKFrequentNumbers(self, nums, k):
        # sorting is O(nlogn) time
        nums.sort()

        top_numbers = []
        prev = nums[0]
        occurences = 1

        # this is O(n) time, because we are iterating through the array
        # so the total time complexity is O(nlogk)
        for i in range(1, len(nums)):
            current = nums[i]
            if current == prev:
                occurences += 1
                continue

            # this takes O(logk) time, because we keep the heap of size k
            self.add_to_heap(top_numbers, k, prev, occurences)

            prev = current
            occurences = 1

        self.add_to_heap(top_numbers, k, prev, occurences)

        # this is O(klogk) time, because we are popping k elements from the heap
        return [heappop(top_numbers)[1] for _ in range(k)]

    def add_to_heap(self, heap, k, el, occurrences):
        heappush(heap, (occurrences, el))
        # just remove the top of the min heap will be equal
        # to only inserting the elements that have greater
        # occurrences than the top of the heap
        if len(heap) > k:
            heappop(heap)

    # this is the same as the above implementation,
    # but more verbose, though it's easier to understand
    # def add_to_heap(self, heap, k, el, occurences):
    #     if len(heap) < k:
    #         heappush(heap, (occurences, el))
    #     elif occurences > heap[0][0]:
    #         heappop(heap)
    #         heappush(heap, (occurences, el))

# solution three brute force with heap
# Complexity:
# O(n^2) time - where n is the number of elements in the array
# O(n) space - to store the numbers in the heap
from heapq import *
import heapq

class Solution:
    def findTopKFrequentNumbers(self, nums, k):
        top_numbers = []

        # this is O(n) time, because we are iterating through the array
        for n in nums:
            # this takes O(n) time, because we are iterating
            # through the heap to find the index of the element
            self.insertOrUpdate(top_numbers, n)

        return [heappop(top_numbers)[1] for _ in range(k)]

    def insertOrUpdate(self, heap, el):
        ix = -1
        for i, n in enumerate(heap):
            if n[1] == el:
                ix = i
                break

        if ix == -1:
            heappush(heap, (-1, el))
            return
        
        target = heap[ix]

        heap[ix] = heap[-1]
        del heap[-1]

        if ix < len(heap):
            heapq._siftup(heap, ix)
            heapq._siftdown(heap, 0, ix)

        heappush(heap, (target[0] - 1, target[1]))

