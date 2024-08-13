# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/my-calendar-i-medium

'''Problem:
Given a 2D array nums of size N x 2, where nums[i] = [starti, endi] and starti is the starting time of the event and endi is the ending time of the event.
For each nums[i], determine if a requested booking time conflicts with any existing bookings.
Return a boolean array of size N, representing whether the booking can be done in the given time interval.

Input: nums = [[10, 20], [15, 25], [20, 30]]
Output: [true, false, true]
Explanation: The first event is booked successfully. The second event overlaps with the first one and is rejected. The third event starts when the first event ends, so it's booked successfully.

Input: [[5, 10], [10, 15], [5, 15]]
Output: [true, true, false]
Explanation: The first and second events are booked without overlap. The third event overlaps with both the first and second, so it's rejected.

Input: [[8, 13],[13, 17], [17, 20]]
Output: [true, true, true]
Explanation: All events are booked without any overlap, as each event starts exactly when the previous one ends.
'''

# solution one using ordered set
# O(nlogn) time - where n is the number of events
# O(n) space - to store the results
import bisect

class Solution:
    def book(self, nums):
        results = [False] * len(nums)

        bookings = []
        for i in range(len(nums)):
            # get the event we want to know if we can book
            event = nums[i]
            start, end = event

            # find the index where the event should be inserted to maintain sorted order
            # this takes O(logn) time because in the worst case, all events are not overlapping
            idx = bisect.bisect_left(bookings, event)

            # find lower and higher (if they exist) neighbors to check for overlap with them
            # the lower neighbor should end before the start of the event
            # the higher neighbor should start after the end of the event
            lower = bookings[idx - 1] if idx > 0 else None
            higher = bookings[idx] if idx < len(bookings) else None

            # check for overlap with neighboring events
            # if the event starts after the lower neighbor ends and ends before the higher neighbor starts
            # then there is no overlap, and we can book the event
            if (lower is None or lower[1] <= start) and (higher is None or end <= higher[0]):
                # add to list if no overlap, it takes O(n) time for shifting elements eventually
                bisect.insort(bookings, event)
                # book the event
                results[i] = True

        return results

# solution two simply merging interval
# O(n) time - where n is the number of events
# O(n) space - to store the results
class Solution:
    def book(self, nums):
        results = [False] * len(nums)

        # the previous event is the last finishing event
        # so if we have [[10, 20], [8, 10], [20, 30]]
        # prev will start as [10, 20], then it will be [20, 30]
        # because even if we can book [8, 10], it will finish before [10, 20]
        # so when moving to [20, 30], we have to check if it starts after [10, 20] ends
        prev = nums[0]
        results[0] = True

        for i in range(1, len(nums)):
            current = nums[i]

            # get the start and end times of the current and previous events
            # this is mostly for readability
            start, end = current
            prev_start, prev_end = prev

            # if the current event starts after the previous
            # event ends, we can book it
            if start >= prev_end:
                prev = current
                results[i] = True
            # or else, if the current event starts and ends before
            # the previous event starts, we can book it
            elif start < prev_start and end <= prev_start:
                results[i] = True

        return results