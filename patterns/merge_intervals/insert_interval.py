# !difficulty: medium

'''Problem:
Given a list of non-overlapping intervals sorted by their start time,
insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Input: intervals = [[1,3], [5,7], [8,12]], new_interval = [4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Input: intervals = [[1,3], [5,7], [8,12]], new_interval = [4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
'''

# solution one with for loop and new_interval overrading
# Complexity:
# O(n) time - because we are iterating over the intervals
# O(n) space - to store the merged intervals
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def insert(self, intervals, new_interval):
        merged = []
    
        for i in range(len(intervals)):
            interval = intervals[i]

            if interval.end < new_interval.start:
                merged.append(interval)
                continue

            if interval.start >= new_interval.end:
                merged.append(new_interval)
                new_interval = interval
                continue
            
            new_interval.start = min(interval.start, new_interval.start)
            new_interval.end = max(interval.end, new_interval.end)

        merged.append(new_interval)

        return merged

# solution two with while loop
# Complexity:
# O(n) time - because we are iterating over the intervals
# O(n) space - to store the merged intervals
class Solution:
    def insert(self, intervals, new_interval):
        merged = []

        # to iterate over the intervals in separate loops
        i = 0

        # skip (and add to output) all intervals that come before the 'new_interval'
        while i < len(intervals) and intervals[i].end < new_interval.start:
            merged.append(intervals[i])
            i += 1

        # merge all intervals that overlap with the new_interval
        while i < len(intervals) and intervals[i].start <= new_interval.end:
            new_interval.start = min(intervals[i].start, new_interval.start)
            new_interval.end = max(intervals[i].end, new_interval.end)
            i += 1

        # insert the new_interval because following intervals do not overlap,
        # they come after the new_interval
        merged.append(new_interval)

        # add all the remaining intervals to the output, the ones that come after the new_interval
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged