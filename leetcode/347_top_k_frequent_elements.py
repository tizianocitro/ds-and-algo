# !code: 347, !difficulty: medium, !from: https://leetcode.com/problems/top-k-frequent-elements/

'''Problem:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:
- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- k is in the range [1, the number of unique elements in the array]
- It is guaranteed that the answer is unique

Follow up: Your algorithm's time complexity must be better than O(nlogn), where n is the array's size.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
'''

# solution one using a heap and a dictionary
# Complexity:
# O(n + nlogk) time - where n is the length of the input list and k is the input and size of the output list/heap
# O(n) space - where n is the length of the input list because we store the frequency of each number
# and in the worst case we have all unique numbers
from heapq import *

class Solution:
    def topKFrequent(self, nums, k):
        # get the frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # use a min_heap to keep the k most frequent numbers
        min_heap = []
        # .keys() is not necessary, but it makes the code more readable
        for num in freq.keys():
            heappush(min_heap, (freq[num], num))
            # if the heap is full, remove the smallest frequency number
            if len(min_heap) > k:
                heappop(min_heap)

        # return the k most frequent numbers
        return [num for _, num in min_heap]

# solution two is the same as solution one but less clean
# Complexity:
# O(n + nlogk) time - where n is the length of the input list and k is the input and size of the output list/heap
# O(n) space - where n is the length of the input list because we store the frequency of each number
# and in the worst case we have all unique numbers
from heapq import *

class Solution:
    def topKFrequent(self, nums, k):
        # get the frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # use a min_heap to keep the k most frequent numbers
        min_heap = []
        for num in freq:
            freq_num = freq[num]
            # if the heap is not full, add the number
            if len(min_heap) < k:
                heappush(min_heap, (freq_num, num))
                continue

            # if the heap is full, replace the smallest frequency number
            if freq_num > min_heap[0][0]:
                heappop(min_heap)
                heappush(min_heap, (freq_num, num))

        # return the k most frequent numbers
        return [num for _, num in min_heap]

# solution three using quick select
# Complexity:
# Average: O(n^2) time - where n is the length of the input list
# Best: O(n) time - where n is the length of the input list
# O(n) space - where n is the length of the input list because we store the frequency of each number
# the code also contains a commented out randomized version of the quick select algorithm
# and another possibility is to implement the pivot selection using the median of medians
class Solution:
    def topKFrequent(self, nums, k):
        # using self.freq to avoi passing the freq as an argument
        # to quickSelect and other functions
        self.freq = {}
        for num in nums:
            self.freq[num] = self.freq.get(num, 0) + 1

        # we want to apply the quick select algorithm, so we need to avoid duplicates
        # duplicates are handled by frequency, so we need to get the unique numbers
        unique_nums = list(self.freq.keys())
        n = len(unique_nums)

        # find the n - kth less frequent number, which is the kth most frequent number
        self.quickSelect(unique_nums, 0, n - 1, n - k)

        # at the end all the numbers to the right of the kth number are more frequent
        # and all the numbers to the left are less frequent, so we return the right side
        # the last k numbers are the k most frequent numbers
        return unique_nums[n - k:]

    def quickSelect(self, unique_nums, start, end, k_smallest):
        pivot_ix = self.partition(unique_nums, start, end)

        if pivot_ix == k_smallest:
            return

        if pivot_ix > k_smallest:
            self.quickSelect(unique_nums, start, pivot_ix - 1, k_smallest)
        else:
            self.quickSelect(unique_nums, pivot_ix + 1, len(unique_nums) - 1, k_smallest)

    def partition(self, unique_nums, low, high):
        if low == high:
            return low

        # the following code implements the randomized quick select algorithm, for which
        # the worst case time complexity is still O(n^2) but the probability of this happening
        # is very low, so this randomized version is a lot faster than the non-randomized version
        # import random
        # pick a random pivot and then swap it with the last element
        # so that the code remains the same as the usual partition scheme
        # where the pivot is the last element (index 'high')
        # pivot_ix = random.randint(low, high)
        # unique_nums[pivot_ix], unique_nums[high] = unique_nums[high], unique_nums[pivot_ix]

        pivot = unique_nums[high]
        for i in range(low, high):
            # sort unique numbers based on their frequency
            if self.freq[unique_nums[i]] < self.freq[pivot]:
                unique_nums[i], unique_nums[low] = unique_nums[low], unique_nums[i]
                low += 1

        unique_nums[high], unique_nums[low] = unique_nums[low], unique_nums[high]
        return low
