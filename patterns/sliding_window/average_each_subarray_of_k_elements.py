# !difficuly: easy

'''Problem:
Given an array, find the average of all contiguous subarrays of size K in it.

Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
'''

# solution one with two indixes for window start and end
# Complexity:
# O(n) time - where n is the length of the array
# O(1) space
class Solution:
    def findAverages(self, k, arr):
        result = []
        windowSum, windowStart, windowEnd = 0.0, 0, 0

        while windowEnd != len(arr) - 1:
            # add the next element
            windowSum += arr[windowEnd]

            # slide the window, no need to slide if we've not hit the required window size of k
            if windowEnd >= k - 1:
                # calculate and append the average
                result.append(windowSum / k)
                # subtract the element going out
                windowSum -= arr[windowStart]
                # slide the window ahead
                windowStart += 1
            # move the window end to expand the window
            windowEnd += 1

        return result

# solution one with end index increased in loop
# Complexity:
# O(n) time - where n is the length of the array
# O(1) space
class Solution:
    def findAverages(self, k, arr):
        result = []
        windowSum, windowStart = 0.0, 0

        # move the window end to expand the window
        for windowEnd in range(len(arr)):
            # add the next element
            windowSum += arr[windowEnd]

            # slide the window, no need to slide if we've not hit the required window size of k
            if windowEnd >= k - 1:
                # calculate and append the average
                result.append(windowSum / k)
                # subtract the element going out
                windowSum -= arr[windowStart]
                # slide the window ahead
                windowStart += 1

        return result
