# !difficulty: medium

'''Problem:
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Input: arr1 = [[1, 3], [5, 6], [7, 9]], arr2 = [[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Input: arr1 = [[1, 3], [5, 7], [9, 12]], arr2 = [[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
'''

# solution one
# O(n + m) time - where n and m are the number of intervals in arr1 and arr2 respectively
# becuase we are iterating through both the lists once
# O(k) space - where k is the number of intervals in the intersection of the two lists
# Ignoring the space needed for the result list, the algorithm runs in constant space O(1).
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def merge(self, intervals_a, intervals_b):
        result = []

        i, j = 0, 0
        while i < len(intervals_a) and j < len(intervals_b):
            # check if intervals overlap and intervals_a[i]'s start time lies within the  other intervals_b[j]
            # so if it starts after the other and starts before the other finishes
            a_overlaps_b = intervals_a[i].start >= intervals_b[j].start and intervals_a[i].start <= intervals_b[j].end

            # check if intervals overlap and intervals_b[j]'s start time lies within the other intervals_a[i]
            b_overlaps_a = intervals_b[j].start >= intervals_a[i].start and intervals_b[j].start <= intervals_a[i].end

            # store the the intersection part of the two intervals
            if a_overlaps_b or b_overlaps_a:
                result.append([
                    max(intervals_a[i].start, intervals_b[j].start),
                    min(intervals_a[i].end, intervals_b[j].end),
                ])

            # move next from the interval which is finishing first
            if intervals_a[i].end < intervals_b[j].end:
                i += 1
            else:
                j += 1

        return result