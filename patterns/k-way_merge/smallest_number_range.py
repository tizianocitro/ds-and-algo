# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a38178a70d5d4526eae293

'''Problem:
Given M sorted arrays, find the smallest range that includes at least one number from each of the M arrays.

Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.

Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
Output: [9, 12]
Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3
'''

# solution one using only k-way merge
# Complexity:
# O(nlogm) time - where n is the total number of elements in all the lists and m is the number of lists
# O(m) space - where m is the number of lists
from heapq import *

class Solution:
    def findSmallestRange(self, lists):
        min_heap = []
        # another option is to use -float('inf') instead of -1
        # in case the arrays can contain negative numbers
        # current_max_number = -float('inf')
        current_max_number = -1

        for i in range(len(lists)):
            if len(lists[i]) > 0:
                heappush(min_heap, (lists[i][0], i, 1))
                # keep track of the maximum number encountered so far,
                # it will be used to calculate the current range
                current_max_number = max(current_max_number, lists[i][0])

        # initialize the range start and end to have the maximum possible length
        range_start, range_end = 0, float('inf')

        # we will do it until the heap has the same length as the number of lists
        # because when it will have less, it means that we have reached the end of one of the lists,
        # so it will not be possible to have a range that includes at least one number from each list
        while len(min_heap) == len(lists):
            num, list_ix, next_num_ix = heappop(min_heap)

            # if the current range is smaller than the smallest range so far
            # we update the smallest range and the start and end of the range
            if range_end - range_start > current_max_number - num:
                range_start, range_end = num, current_max_number

            if next_num_ix < len(lists[list_ix]):
                heappush(min_heap, (lists[list_ix][next_num_ix], list_ix, next_num_ix + 1))
                # whenever we push a new number into the heap, we update the maximum number
                # encountered so far because the new number could be the bigger than the current max
                current_max_number = max(current_max_number, lists[list_ix][next_num_ix])

        return [range_start, range_end]

# solution two with k-way merge and sliding window
# Complexity:
# O(nlogm) time - where n is the total number of elements in all the lists and m is the number of lists
# O(n) space - where n is the total number of elements in all the lists
from heapq import *

class Solution:
    # O(nlogm) time, O(n) space
    def findSmallestRange(self, lists):
        full_list = self.get_full_list(lists)
        return self.find_range(full_list, lists)

    # get the full list of all numbers from all lists
    # by using k-way merge to merge all lists into one list
    # O(nlogm) time, O(n) space
    def get_full_list(self, lists):
        min_heap = []
        for i in range(len(lists)):
            if len(lists[i]) > 0:
                heappush(min_heap, (lists[i][0], i, 1))

        result = []
        while min_heap:
            num, list_ix, next_num_ix = heappop(min_heap)
            if next_num_ix < len(lists[list_ix]):
                heappush(min_heap, (lists[list_ix][next_num_ix], list_ix, next_num_ix + 1))

            # append the number and the list index it came from,
            # the list index will be used to keep track of the number's origin
            result.append((num, list_ix))

        return result

    # find the smallest range that includes at least one number from each of the M arrays
    # O(n) time, O(m) space
    def find_range(self, full_list, lists):
        # keep track of the number of numbers encountered from each list
        encountered_lists = {}
        # keep track of the number of lists that have been encountered
        matched = 0

        # initialize the smallest range and the window start and end
        range_min_len, range_start, range_end = float('inf'), 0, 0
        start, end = 0, 0

        while end < len(full_list):
            num, list_ix = full_list[end]
            # update the number of numbers encountered from the list
            encountered_lists[list_ix] = encountered_lists.get(list_ix, 0) + 1
            # if this is the first time the number is encountered from the list
            # we increment the number of lists that have been encountered
            if encountered_lists[list_ix] == 1:
                matched += 1

            # if all lists have been encountered
            while matched == len(lists):
                start_num, start_ix = full_list[start]

                # calculate the length of the range currently in the window
                # so if start_num = 4 and num = 7, the range is 4 to 7, which is 3 numbers
                range_len = num - start_num
                # if the current range is smaller than the smallest range so far
                # we uodate the smallest range and the start and end of the range
                if range_len < range_min_len:
                    range_start, range_end = start, end
                    range_min_len = range_len

                # move the window start to the right, and if the number at the start
                # was the last one encountered from its list, we decrement the number of lists
                encountered_lists[start_ix] -= 1
                if encountered_lists[start_ix] == 0:
                    matched -= 1
                start += 1

            # move the window end to the right
            end += 1

        # return the smallest range using the min_start and min_end indices
        return [full_list[range_start][0], full_list[range_end][0]]