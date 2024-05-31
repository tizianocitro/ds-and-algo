# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a348bd7bde61668d15d011

'''Problem:

'''

# solution one
# Complexity:
# O(nlogk) - where n is the total number of elements in all the k input lists
# O(k) - where k is the number of input lists because the heap will store at most k elements
from heapq import *

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def merge(self, lists):
        min_heap = []

        # put the head of each list in the min heap
        for head in lists:
            if head is not None:
                heappush(min_heap, head)

        # take the smallest (top) element form the min heap and add it to the result
        # if the top element has a next element add it to the heap
        # this will cost O(nlogk) because we'll be iterating through all the elements
        # and each time we will pop from the heap and eventually push to the heap
        result_head, result_tail = None, None
        while min_heap:
            node = heappop(min_heap)

            if result_head is None:
                result_head = node

            if result_tail is not None:
                result_tail.next = node
            result_tail = node

            if node.next is not None:
                heappush(min_heap, node.next)

        return result_head

# solution two with just a different way of performing the
# result_head and result_tail updates
# Complexity:
# O(nlogk) - where n is the total number of elements in all the k input lists
# O(k) - where k is the number of input lists because the heap will store at most k elements
from heapq import *

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def merge(self, lists):
        min_heap = []

        # put the head of each list in the min heap
        for head in lists:
            if head is not None:
                heappush(min_heap, head)

        # take the smallest (top) element form the min heap and add it to the result
        # if the top element has a next element add it to the heap
        # this will cost O(nlogk) because we'll be iterating through all the elements
        # and each time we will pop from the heap and eventually push to the heap
        result_head, result_tail = None, None
        while min_heap:
            node = heappop(min_heap)

            if result_head is None:
                result_head = node
                result_tail = node
            else:
                result_tail.next = node
                result_tail = node

            if node.next is not None:
                heappush(min_heap, node.next)

        return result_head