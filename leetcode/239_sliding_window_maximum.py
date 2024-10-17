# !code: 239, !difficulty: hard, !from: https://leetcode.com/problems/sliding-window-maximum/

'''Problem:"
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

Input: nums = [1], k = 1
Output: [1]
'''

# solution one using monotonically decreasing queue
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(n) space - because the result will contain n - k + 1 elements
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []

        window = deque()
        start = 0
        for end in range(len(nums)):
            # remove all elements from the window that are less than the current element
            # to build the queue in a way that is monotonically decreasing
            while window and nums[end] > nums[window[-1]]:
                window.pop()

            window.append(end)

            # if the leftmost element in the window is out of the window
            if start > window[0]:
                # remove it
                window.popleft()

            # if the window size reaches k
            if end - start + 1 > k - 1:
                # append the leftmost element in the window to the result
                result.append(nums[window[0]])
                # move the start of the window to the right
                start += 1

        return result

# solution two using queue with max() function
# Complexity:
# O((n - k) * k) time - where n is the number of elements in the array and k is the size of the window
# because for each element in the array, we iterate over the window of size k
# O(n) space - because the result will contain n - k + 1 elements while the queue will contain at most k elements
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []

        # use a queue to store the current window
        # and to be able to pop from the left
        window = deque()

        start = 0
        for end in range(len(nums)):
            window.append(nums[end])

            if len(window) > k - 1:
                # add the max element from the window
                result.append(max(window))
                # pop the first element from the window to make room for the next element
                window.popleft()
                # move the start of the window to the right
                start += 1

        return result
