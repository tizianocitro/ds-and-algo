# !difficulty: medium

# Write a function that takes in a non-empty array of arbitrary intervals,
# merges any overlapping intervals, and returns the new intervals in no particular order.
# Each interval interval is an array of two integers,
# with interval[0] as the start of the interval and interval[1] as the end of the interval.
# Note that back-to-back intervals aren't considered to be overlapping.
# For example, [1, 5] and [6, 7] aren't overlapping;
# however, [1, 6] and [6, 7] are indeed overlapping.
# Also note that the start of any particular interval will always be less than or equal to the end of that interval.

# Input:
# intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
# Output:
# [[1, 2], [3, 8], [9, 10]] // Merge the intervals [3, 5], [4, 7], and [6, 8].

# solution one
# Complexity
# O(nlog(n)) time - where n is the number of intervals
# O(1) space - because we are merging intervals in place
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            del intervals[i + 1]
        else:
            i += 1
    return intervals

# Complexity
# Time: O(nlog(n)) where n is the number of intervals
# Space: O(n) where n is the number of intervals

# solution two
def mergeOverlappingIntervals(intervals):
    if len(intervals) < 1:
        return [[]]

    intervals = sorted(intervals, key=lambda x: x[0])
    mergedIntervals = []
    l, r = intervals[0]

    for lCurrent, rCurrent in intervals:
        if lCurrent > r:
            mergedIntervals.append([l, r])
            l, r = lCurrent, rCurrent
            continue
        if lCurrent < l:
            l = lCurrent
        if rCurrent > r:
            r = rCurrent

    mergedIntervals.append([l, r])
    return mergedIntervals

# solution three is identical to solution one, just different syntax
def mergeOverlappingIntervals(intervals):
    length = len(intervals)
    if length < 1:
        return [[]]

    intervals = sorted(intervals, key=lambda x: x[0])
    mergedIntervals = []
    l, r = intervals[0]

    for i in range(1, length):
        lCurrent, rCurrent = intervals[i]
        if lCurrent > r:
            mergedIntervals.append([l, r])
            l, r = lCurrent, rCurrent
            continue
        if lCurrent < l:
            l = lCurrent
        if rCurrent > r:
            r = rCurrent

    mergedIntervals.append([l, r])
    return mergedIntervals

# solution four uses a different approach to keep track of the current interval
def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)
    
    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)

    return mergedIntervals