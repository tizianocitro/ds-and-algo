# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1e7c1b231098e09f3c88d

'''Problem:
Given a string and a number K, find if the string can be rearranged such
that the same characters are at least K distance apart from each other.

Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.

Input: "Programming", K=3
Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more  
Explanation: All same characters are 3 distance apart.

Input: "aab", K=2
Output: "aba"
Explanation: All same characters are 2 distance apart.

Input: "aappa", K=3
Output: ""
Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of characters in the input string
# O(n) space - where n is the number of characters in the input string for the map and heap
from heapq import *
from collections import deque

class Solution:
    def reorganizeString(self, str1, k):
        # if k is less than 2, return the string as is
        # because the characters can follow each other, even if they are the same 
        if k < 2:
            return str1

        frequencies = {}
        for c in str1:
            frequencies[c] = frequencies.get(c, 0) + 1

        max_heap = []
        for c, freq in frequencies.items():
            heappush(max_heap, (-freq, c))

        reorganized_string = []
        prev_queue = deque()
        while max_heap:
            freq, c = heappop(max_heap)

            # in this case, we check if the queue has k - 1 elements
            # because we append the current char after the check
            # so we should remove from k the current char, thus why the -1
            if len(prev_queue) >= k - 1:
                prev = prev_queue.popleft()
                if -prev[0] > 0:
                    heappush(max_heap, prev)

            # append the current character to the result string
            reorganized_string.append(c)
            # decrement the frequency and append to the queue
            # freq is negative, so we add 1 to decrement it
            freq += 1
            prev_queue.append((freq, c))

        # if we were successful in appending all the characters to the result string, return it
        return ''.join(reorganized_string) if len(reorganized_string) == len(str1) else ''


# solution two
# Complexity:
# O(nlogn) time - where n is the number of characters in the input string
# O(n) space - where n is the number of characters in the input string for the map and heap
from heapq import *
from collections import deque

class Solution:
    def reorganizeString(self, str1, k):
        # if k is less or equale than 1, return the string as is
        # because the characters can follow each other, even if they are the same
        if k <= 1: 
            return str1

        frequencies = {}
        for c in str1:
            frequencies[c] = frequencies.get(c, 0) + 1

        maxHeap = []
        for c, freq in frequencies.items():
            heappush(maxHeap, (-freq, c))

        prev_queue = deque()
        reorganized_string = []
        while maxHeap:
            freq, c = heappop(maxHeap)
            # append the current character to the result string
            reorganized_string.append(c)
            # decrement the frequency and append to the queue
            # freq is negative, so we add 1 to decrement it
            prev_queue.append((c, freq + 1))

            # in this case, we check if the queue has k elements
            # because we append the current char before checking
            if len(prev_queue) == k:
                c, freq = prev_queue.popleft()
                if -freq > 0:
                    heappush(maxHeap, (freq, c))

        # if we were successful in appending all the characters to the result string, return it
        return ''.join(reorganized_string) if len(reorganized_string) == len(str1) else ""