# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639ca6d8585e4a974dfff649

'''Problem:
Given a set with distinct elements, find all of its distinct subsets.
All the numbers in the given set are unique.

Input: [1, 3]
Output: [], [1], [3], [1,3]

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''

# solution one
# Complexity:
# O(n * 2^n) time - where n is the number of elements in the input set.
# This is because, in each step, the number of subsets doubles as we add each element to all the existing subsets,
# therefore, we will have a total of O(2^n) subsets.
# And since we construct a new subset from an existing set using list(),
# the time complexity of the above algorithm will be O(n * 2^n) time.
# O(n * 2^n) - where n is the number of elements in the input set.
# This is because we will have a total of O(2^n) subsets with each of them up to O(n) space.
class Solution:
    def find_subsets(self, nums):
        # start with subsets containing the empty subset
        subsets = [[]]

        for current in nums:
            # we will take all existing subsets and insert the current number in them to create new subsets
            level_size = len(subsets)
            for i in range(level_size):
                # create a new subset from the existing subset and insert the current element to it
                level = list(subsets[i])
                level.append(current)

                # append the new subset to the subsets
                subsets.append(level)

        return subsets