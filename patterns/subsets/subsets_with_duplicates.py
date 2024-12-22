# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639ca98e585e4a974dfff9bf

'''Problem:
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

# solution one
# Complexity:
# O(n * 2^n) time - where n is the number of elements in the input set
# it is actually O(nlogn + 2^n) because we are sorting the input array before iterating the elements,
# but the O(nlogn) is dominated by O(2^n) because 2^n > nlogn.
# O(n * 2^n) space - for all subsets
class Solution:
    def findSubsets(self, nums):
        # sort the numbers to handle duplicates
        list.sort(nums)

        subsets = [[]]
        endIndex = 0
        for i in range(len(nums)):
            startIndex = 0

            # if current and the previous elements are same,
            # create new subsets only from the subsets added in the previous step
            # so we move the start_index to the first element that was added in the previous
            # which is the length of the subsets array before adding the new elements
            if i > 0 and nums[i] == nums[i - 1]:
                startIndex = endIndex
            
            # update end_index for this iteration and for handling
            # eventual duplicates during next step
            endIndex = len(subsets)

            for j in range(startIndex, endIndex):
                # create a new subset from the existing subset and add the current element to it
                set1 = list(subsets[j])
                set1.append(nums[i])
                subsets.append(set1)

        return subsets
