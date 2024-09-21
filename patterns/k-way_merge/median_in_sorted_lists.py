# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dc98a892999e03afaee850

'''Problem:
Given M sorted arrays, find the median number among all arrays.

Input: [1, 3, 5], [2, 4, 6], [0, 9, 10, 11]
Output: 4
'''

# solution one
# Complexity:
# O(klogm) time - where m is the number of lists and k is the median position
# O(m) space - to store the min heap
from heapq import *

class Solution:
    def findMedianSortedLists(self, lists):
        min_heap = []

        # push the first element of each list into the heap
        # each element of the heap is a tuple of (number, list_index, next_element_index)
        for i, l in enumerate(lists):
            # if the list is not empty, push the first element of the list
            if len(l) > 0:
                heappush(min_heap, (l[0], i, 1))

        # find median position
        total_elements = sum(len(list) for list in lists)
        median_pos = total_elements // 2

        median = 0
        for i in range(median_pos + 1):
            # pop the ith element from the min heap and
            # if the next element exists, push it to the heap
            ith_num, ith_list, ith_ix = heappop(min_heap)
            if ith_ix < len(lists[ith_list]):
                next_num = lists[ith_list][ith_ix]
                heappush(min_heap, (next_num, ith_list, ith_ix + 1))

            median = ith_num

        return median
