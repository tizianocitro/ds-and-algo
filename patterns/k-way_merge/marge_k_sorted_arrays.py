# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dc98a892999e03afaee850

'''Problem:
Given a list of k sorted arrays, merge them into one sorted list.

Input: A1=[2, 6, 8], A2=[3, 6, 7], A3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
'''

# solution one
# Complexity:
# O(nlogk) time - where n is the total number of elements in all the arrays and k is the number of arrays
# O(k) space - to store the min heap
from heapq import *

class Solution:
    def merge(self, arrays):
        min_heap = []

        # push the first number of each array into the heap
        # each element of the heap is a tuple of
        # (number, list_index, next_number_index)
        for i in range(len(arrays)):
            if len(arrays[i]) > 0:
                heappush(min_heap, (arrays[i][0], i, 1))

        result = []
        while min_heap:
            num, list_ix, next_num_ix = heappop(min_heap)
            # if the next number exists, push it to the heap
            if next_num_ix < len(arrays[list_ix]):
                heappush(min_heap, (arrays[list_ix][next_num_ix], list_ix, next_num_ix + 1))

            # add current number to the result
            result.append(num)

        return result