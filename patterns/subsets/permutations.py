# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639cae5754a43e1fc3c40cb6

'''Problem:
Given a set of distinct numbers, find all of its permutations.
All the numbers in the given set are unique.

Permutation is defined as the re-arranging of the elements of the set.
For example, {1, 2, 3} has the following six permutations:
- {1, 2, 3}
- {1, 3, 2}
- {2, 1, 3}
- {2, 3, 1}
- {3, 1, 2}
- {3, 2, 1}

If a set has N distinct elements it will have N! permutations.

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
'''

# solution one iterative
# Complexity:
# O(n + n!) time - where n is the number of elements in the input array
# this is because we are iterating over the input array to create permutations
# and then we are creating n! permutations, in the nested two for loops
# O(n * n!) space - becasue each of the n! permutations has n elements, so the result list has n * n! elements
from collections import deque

class Solution:
    def findPermutations(self, nums):
        nums_length = len(nums)

        result = []
        permutations = deque()
        permutations.append([])

        for current in nums:
            # we will take all existing permutations and add the current number to create new permutations
            num_permutations = len(permutations)

            for _ in range(num_permutations):
                permutation = permutations.popleft()

                # create a new permutation by adding the current number at every position
                # len(permutation) + 1 because we need to add a position for the current number
                # if we have a permutation of length 2, we will have 3 positions to add the current number
                # for example, if we have a permutation [1, 3] (length is 2), we will have the following new permutations:
                # [5, 1, 3], [1, 5, 3], [1, 3, 5], so we need to iterate over the length of 2 + 1
                for i in range(len(permutation) + 1):
                    new_permutation = list(permutation)
                    new_permutation.insert(i, current)

                    if len(new_permutation) == nums_length:
                        result.append(new_permutation)
                    else:
                        permutations.append(new_permutation)

        return result

# solution two recursive
# Complexity:
# O(n * n!) time - where n is the number of elements in the input array
# O(n * n!) space - where n is the number of elements in the input array
class Solution:
    def generatePermutations(self, nums):
        result = []
        self.generatePermutationsRecursive(nums, 0, [], result)
        return result

    def generatePermutationsRecursive(self, nums, index, current_permutation, result):
        if index == len(nums):
            result.append(current_permutation)
        else:
            # create a new permutation by adding the current number at every position
            for i in range(len(current_permutation) + 1):
                new_permutation = list(current_permutation)
                new_permutation.insert(i, nums[index])

                self.generatePermutationsRecursive(nums, index + 1, new_permutation, result)