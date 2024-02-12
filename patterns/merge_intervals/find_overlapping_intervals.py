# !difficulty: medium

'''Problem:
Given a set of intervals, find out if any two intervals overlap.

Input: intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap
'''


# solution one
# Complexity:
# O(nlogn) time - because we are sorting the intervals
# O(1) space
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        # sort to ensure the we can make the check at line 25 to verify overlapping
        intervals.sort(key=lambda x: x.start)
        current = intervals[0]

        for i in range(1, len(intervals)):      
            interval = intervals[i]
            # intervals overlap
            if interval.start <= current.end:
                return True
            current = interval

        return False