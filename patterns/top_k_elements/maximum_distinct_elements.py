# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1da0f1d305c96d5e6191d

'''Problem:
Given an array of numbers and a number K, we need to remove K numbers from the array such that we are left with maximum distinct numbers.

Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have 
to skip 5 because it is not distinct and occurred twice. 
Another solution could be to remove one instance of '5' and '3' each to be left with three distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.

Input: [3, 5, 12, 11, 12], and K=3
Output: 2
Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then we can delete any two numbers which will leave us 2 distinct numbers in the result.

Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
Output: 3
Explanation: We can remove one occurrence of '4' to get three distinct numbers.
'''

# solution one
# this solution can be improved in time complexity (see solution three)
# Complexity:
# O(nlogn) time - where n is the number of numbers in the input array
# more precisely, it is O(nlogn + klogn) where n is the number of numbers in the input array
# O(n) space - where n is the number of numbers in the input array
from heapq import *

class Solution:
    def findMaximumDistinctElements(self, nums, k):
        distinct_elements_count = 0
        # if the array has less than or equal to 'k' elements,
        # we can return 0 because we have to basically remove all numbers
        if len(nums) <= k:
            return distinct_elements_count

        # find the frequency of each number
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        min_heap = []
        # insert all numbers with frequency greater than '1' into the min heap,
        # otherwise, add them to the distinct numbers count
        for num, frequency in frequencies.items():
            if frequency > 1:
                heappush(min_heap, (frequency, num))
                continue
            distinct_elements_count += 1

        # following a greedy approach, try removing the
        # least frequent numbers first from the min heap
        # if the frequency of a number is greater than '1', add it to
        # the min heap again, otherwise, add it to the distinct numbers count
        while k > 0 and min_heap:
            frequency, num = heappop(min_heap)
            # decrement the frequency of the number as many times as possible
            while k > 0 and frequency > 1:
                frequency -= 1
                k -= 1
            # if a number still has a frequency greater than '1',
            # add it to the heap again, otherwise, increase the distinct numbers count
            if frequency > 1:
                heappush(min_heap, (frequency, num))
                continue
            distinct_elements_count += 1

            # the above code could just be simplified as follows
            # because there is no need to add the number to the heap again,
            # if it has a frequency greater than '1' since k has already become 0
            # if frequency == 1:
            #    distinct_elements_count += 1

        # if k > 0, it means we have to remove some distinct numbers
        # so we will subtract the remaining k from the distinct numbers count
        # if k == 0, the distinct numbers count will not change anyway
        return distinct_elements_count - k

# solution two
# this solution can be improved in time complexity,
# similarly to how is done in solution three for solution one
# Complexity:
# O(nlogn) time - where n is the number of numbers in the input array
# more precisely, it is O(nlogn + klogn) where n is the number of numbers in the input array
# O(n) space - where n is the number of numbers in the input array
from heapq import *

class Solution:
    def findMaximumDistinctElements(self, nums, k):
        distinct_elements_count = 0
        if len(nums) <= k:
            return distinct_elements_count

        # find the frequency of each number
        frequencies = {}
        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1

        min_heap = []
        # insert all numbers with frequency greater than '1' into the min-heap
        for num, frequency in frequencies.items():
            if frequency == 1:
                distinct_elements_count += 1
            else:
                heappush(min_heap, (frequency, num))

        # following a greedy approach, try removing the
        # least frequent numbers first from the min-heap
        while k > 0 and min_heap:
            frequency, num = heappop(min_heap)
            # to make an element distinct, we need to
            # remove all of its occurrences except one
            k -= frequency - 1
            # if k is still greater than '0', we cna add the number
            # to the distinct numbers count because it has become distinct
            if k >= 0:
                distinct_elements_count += 1

        # if k > 0, this means we have to remove some distinct numbers
        if k > 0:
            distinct_elements_count -= k

        return distinct_elements_count

# solution three is solution one but with better time complexity
# because we store at most k elements into the heap, this is because,
# in the worst case, we will be extracting k elements from the heap
# Complexity:
# O(nlogk) time - where n is the number of numbers in the input array
# more precisely, it is O(nlogk + klogk) where n is the number of numbers in the input array
# O(n) space - where n is the number of numbers in the input array
from heapq import *

class Solution:
    def findMaximumDistinctElements(self, nums, k):
        distinct_elements_count = 0
        # if the array has less than or equal to 'k' elements,
        # we can return 0 because we have to basically remove all numbers
        if len(nums) <= k:
            return distinct_elements_count

        # find the frequency of each number
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        min_heap = []
        # insert all numbers with frequency greater than '1' into the min heap,
        # otherwise, add them to the distinct numbers count
        for num, frequency in frequencies.items():
            if frequency == 1:
                distinct_elements_count += 1
            # thanks to the following condition, we only store at most
            # k elements into the heap, optimizing the time complexity
            if frequency > 1 and len(min_heap) < k:
                heappush(min_heap, (frequency, num))

        # following a greedy approach, try removing the
        # least frequent numbers first from the min heap
        # if the frequency of a number is greater than '1', add it to
        # the min heap again, otherwise, add it to the distinct numbers count
        while k > 0 and min_heap:
            frequency, num = heappop(min_heap)
            # decrement the frequency of the number as many times as possible
            while k > 0 and frequency > 1:
                frequency -= 1
                k -= 1
            # if a number still has a frequency greater than '1',
            # add it to the heap again, otherwise, increase the distinct numbers count
            if frequency > 1:
                heappush(min_heap, (frequency, num))
                continue
            distinct_elements_count += 1

            # the above code could just be simplified as follows
            # because there is no need to add the number to the heap again,
            # if it has a frequency greater than '1' since k has already become 0
            # if frequency == 1:
            #    distinct_elements_count += 1

        # if k > 0, it means we have to remove some distinct numbers
        # so we will subtract the remaining k from the distinct numbers count
        # if k == 0, the distinct numbers count will not change anyway
        return distinct_elements_count - k