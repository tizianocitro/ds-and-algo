# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/solution-kth-smallest-number-1

'''Problem:
Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three smaller numbers are
[1, 2, 5].

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
'''

'''Note:
This is a well-known problem and there are multiple solutions available to solve this.
A few other similar problems are:
- Find the Kth largest number in an unsorted array
- Find the Kth smallest or largest numbers in an unsorted array
- Find the median of an unsorted array
'''

# solution one brute force
# Complexity:
# O(nk) time - where n is the length of the input array and k is the input k
# O(1) space
import math

class Solution:
    def findKthSmallestNumber(self, nums, k):
        # to handle duplicates, we will keep track of previous smallest number and its index
        previousSmallestNum, previousSmallestIndex = -math.inf, -1
        currentSmallestNum, currentSmallestIndex = math.inf, -1

        for i in range(k):
            for j in range(len(nums)):
                if nums[j] > previousSmallestNum and nums[j] < currentSmallestNum:
                    # found the next smallest number
                    currentSmallestNum = nums[j]
                    currentSmallestIndex = j
                elif nums[j] == previousSmallestNum and j > previousSmallestIndex:
                    # found a number which is equal to the previous smallest number; since numbers 
                    # can repeat, we will consider 'nums[j]' only if it has a different index than 
                    # previous smallest
                    currentSmallestNum = nums[j]
                    currentSmallestIndex = j
                    # break here as we have found our definitive next smallest number
                    break

            # current smallest number becomes previous smallest number for the next iteration
            previousSmallestNum = currentSmallestNum
            previousSmallestIndex = currentSmallestIndex
            currentSmallestNum = math.inf

        return previousSmallestNum

# solution two using sorting
# Complexity:
# O(nlogn) time - where n is the length of the input array
# O(1) space
class Solution:
    def findKthSmallestNumber(self, nums, k):
        nums.sort()
        return nums[k - 1]

# solution three using max-heap
# Complexity:
# O(nlogk) time - where n is the length of the input array and k is the input k
# O(k) space - to store the heap
from heapq import *

class Solution:
    def findKthSmallestNumber(self, nums, k):
        max_heap = []
        # it takes O(klogk)
        for i in range(k):
            heappush(max_heap, -nums[i])

        # it takes (n-k)logk
        for i in range(k, len(nums)):
            num = nums[i]
            # since we want to keep track of the k smallest numbers,
            # we can compare every number with the top of the heap
            # while iterating through all numbers, and if it is smaller than the top,
            # we’ll take the top out and insert the smaller number,
            # this way the top of the heap will always have the kth smallest number
            if num <= -max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -num)      

        return -max_heap[0]

# solution four using min-heap
# Complexity:
# O(klogn) time - where n is the length of the input array and k is the input k
# O(n) space - to store the heap
from heapq import *

class Solution:
    # insert all the numbers in the min-heap and then extract
    # the top k numbers from the heap to find the Kth smallest number
    def findKthSmallestNumber(self, nums, k):
        min_heap = nums

        heapify(min_heap)

        kth_min = heappop(min_heap)
        for _ in range(k - 1):
            kth_min = heappop(min_heap)

        return kth_min


'''Solution (known as Quickselect):
Quicksort picks a number called pivot and partition the input array around it. After partitioning, all numbers
smaller than the pivot are to the left of the pivot, and all numbers greater than or equal to the pivot are to the right of the pivot.
This ensures that the pivot has reached its correct sorted position.

We can use this partitioning scheme to find the Kth smallest number. We will recursively partition the input array and if,
after partitioning, our pivot is at the K-1 index we have found our required number; if not, we will choose one the following option:
- If pivot’s position is larger than K-1, we will recursively partition the array on numbers lower than the pivot.
- If pivot’s position is smaller than K-1, we will recursively partition the array on numbers greater than the pivot.
'''

# solution five using partition scheme of quicksort (quickselect)
# Best: O(n) time | O(n) space - where n is the length of the input array
# Average: O(n) time | O(n) space - where n is the length of the input array
# Worst: O(n^2) time | O(n) space - where n is the length of the input array
# contrary to quicksort, instead of recursing into both sides, quickselect only recurses into one side,
# i.e., the side with the element it is searching for and this reduces the average and best case time complexity to O(n)
# the worst case time complexity is still O(n^2) and happens when the input array is sorted or if all of its elements are the same
class Solution:
    def findKthSmallestNumber(self, nums, k):
        return self.findKthSmallestNumberRec(nums, k, 0, len(nums) - 1)

    def findKthSmallestNumberRec(self, nums, k, start, end):
        p = self.partition(nums, start, end)

        if p == k - 1:
            return nums[p]

        # search lower part
        if p > k - 1:
            return self.findKthSmallestNumberRec(nums, k, start, p - 1)

        # search higher part
        return self.findKthSmallestNumberRec(nums, k, p + 1, end)

    def partition(self, nums, low, high):
        if low == high:
            return low

        # this is called lamuto partition scheme
        pivot = nums[high]
        for i in range(low, high):
            # all elements less than 'pivot' will be before the index 'low'
            if nums[i] < pivot:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1

        # put the pivot in its correct place
        nums[low], nums[high] = nums[high], nums[low]
        return low

'''Solution (known as Randomized Quickselect):
To mitigate the worst case for quicksort and quickselect, instead of always picking a fixed index for pivot (e.g., in the solution five, we
always pick nums[high] as the pivot), we can randomly select an element as pivot. After randomly choosing the pivot element, we expect the
split of the input array to be reasonably well balanced on average.
'''

# solution six using quicksort's randomized partition scheme (randomized quickselect)
# Best: O(n) time | O(n) space - where n is the length of the input array
# Average: O(n) time | O(n) space - where n is the length of the input array
# Worst: O(n^2) time | O(n) space - where n is the length of the input array
# the worst case time complexity is still O(n^2) but the probability of this happening is very low
# this algorithm is a lot faster than the non-randomized version
import random

class Solution:
    def findKthSmallestNumber(self, nums, k):
        return self.findKthSmallestNumberRec(nums, k, 0, len(nums) - 1)

    def findKthSmallestNumberRec(self, nums, k, start, end):
        p = self.partition(nums, start, end)

        if p == k - 1:
            return nums[p]

        # search lower part
        if p > k - 1:
            return self.findKthSmallestNumberRec(nums, k, start, p - 1)

        # search higher part
        return self.findKthSmallestNumberRec(nums, k, p + 1, end)

    def partition(self, nums, low, high):
        if low == high:
            return low

        # pick a random pivot and then swap it with the last element
        # so that the code remains the same as the usual partition scheme
        # where the pivot is the last element (index 'high')
        pivot_index = random.randint(low, high)
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]

        pivot = nums[high]
        for i in range(low, high):
            # all elements less than 'pivot' will be before the index 'low'
            if nums[i] < pivot:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1

        # put the pivot in its correct place
        nums[low], nums[high] = nums[high], nums[low]
        return low

'''Solution (known as Median of Medians):
Median of Medians algorithm allows us to choose a good pivot for the partitioning algorithm of the Quicksort. This algorithm finds an
approximate median of an array in linear time O(n). When this approximate median is used as the pivot, the worst-case complexity of the
partitioning procedure reduces to linear O(n), which is also the asymptotically optimal worst-case complexity of any sorting/selection algorithm.
This algorithm was originally developed by Blum, Floyd, Pratt, Rivest, and Tarjan and was describe in their 1973 paper.

This is how the selction of the pivot using the Median of Medians algorithm works:
- If we have 5 or less than 5 elements in the input array, we simply take its first element as the pivot.
  If not then we divide the input array into subarrays of five elements (for simplicity we can ignore any subarray having less than five elements).
- Sort each subarray to determine its median. Sorting a small and fixed numbered array takes constant time.
  At the end of this step, we have an array containing medians of all the subarray.
- Recursively call the partitioning algorithm on the array containing medians until we get our pivot.
- Every time the partition procedure needs to find a pivot, it will follow the above three steps.
'''

# solution seven using median of medians
# Best: O(n) time | O(n) space - where n is the length of the input array
# Average: O(n) time | O(n) space - where n is the length of the input array
# Worst: O(n) time | O(n) space - where n is the length of the input array
class Solution:
    def findKthSmallestNumber(self, nums, k):
        return self.findKthSmallestNumberRec(nums, k, 0, len(nums) - 1)

    def findKthSmallestNumberRec(self, nums, k, start, end):
        p = self.partition(nums, start, end)

        if p == k - 1:
            return nums[p]

        # search lower part
        if p > k - 1:
            return self.findKthSmallestNumberRec(nums, k, start, p - 1)

        # search higher part
        return self.findKthSmallestNumberRec(nums, k, p + 1, end)

    def partition(self, nums, low, high):
        if low == high:
            return low

        median = self.medianOfMedians(nums, low, high)
        # find median in the array and swap it with 'nums[high]' which will become our pivot
        for i in range(low, high):
            if nums[i] == median:
                nums[i], nums[high] = nums[high], nums[i]
                break

        pivot = nums[high]
        for i in range(low, high):
            # all elements less than 'pivot' will be before the index 'low'
            if nums[i] < pivot:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1

        # put the pivot in its correct place
        nums[low], nums[high] = nums[high], nums[low]
        return low

    def medianOfMedians(self, nums, low, high):
        # get lenght of the current window on the array that we are working on
        n = high - low + 1

        # if we have less than 5 elements, ignore the partitioning algorithm
        if n < 5:
            # and just return the median, which is at index 'low'
            return nums[low]

        # partition the given array into chunks of 5 elements
        partitions = [nums[j:j + 5] for j in range(low, high + 1, 5)]

        # for simplicity, lets ignore any partition with less than 5 elements
        full_partitions = [partition for partition in partitions if len(partition) == 5]

        # sort all partitions
        sorted_partitions = [sorted(partition) for partition in full_partitions]

        # find median of all partations of length 5,
        # so the median of each partition is at index '2'
        medians = [partition[2] for partition in sorted_partitions]

        return self.partition(medians, 0, len(medians) - 1)