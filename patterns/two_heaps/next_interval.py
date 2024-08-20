# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639ca31ddf76bf2533026e64

'''Problem:
Given an array of intervals, find the next interval of each interval.
In a list of intervals, for an interval i its next interval j will have the smallest start greater than or equal to the end of i.

Write a function to return an array containing indices of the next interval of each input interval.
If there is no next interval of a given interval, return -1.

It is given that none of the intervals have the same start point.

Input: intervals = [[2,3], [3,4], [5,6]]  
Output: [1, 2, -1]  
Explanation: The next interval of [2,3] is [3,4] having index 1. Similarly, the next interval of [3,4] is [5,6] having index 2. There is no next interval for [5,6] hence we have -1.

Input: intervals = [[3,4], [1,5], [4,6]]  
Output: [2, -1, -1]  
Explanation: The next interval of [3,4] is [4,6] which has index 2. There is no next interval for [1,5] and [4,6].
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of intervals
# O(n) space - where n is the number of intervals
from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def findNextInterval(self, intervals):
        n = len(intervals)
        result = [-1 for _ in range(n)]

        # heaps for finding the maximum start and end
        max_ends, max_starts = [], []
        for i in range(n):
            heappush(max_ends, (-intervals[i].end, i))
            heappush(max_starts, (-intervals[i].start, i))

        # go through all the intervals to find each interval's next interval
        for _ in range(n):
            # find the next interval of the interval which has the highest end
            end, i = heappop(max_ends)

            if -end <= -max_starts[0][0]:
                start, j = heappop(max_starts)

                # find the the interval that has the closest start
                while max_starts and -end <= -max_starts[0][0]:
                    start, j = heappop(max_starts)

                result[i] = j

                # put the interval back as it could be the next interval of other intervals
                # we can discard others because they would be the next interval of no other interval,
                # because we are dealing with the one with the highest end,
                # so none of the other will need an interval with a higher start than the current one
                heappush(max_starts, (start, j))

        return result