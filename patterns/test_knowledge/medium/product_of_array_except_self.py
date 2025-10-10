# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/product-of-array-except-self-medium

'''Solution:
1. Initialize Two Arrays: start by initializing two arrays, left and right. The left array will hold the product of
   all numbers to the left of index i and the right array will hold the product of all numbers to the right of index i.

2. Populate the Left Array: the first element of the left array will always be 1 because there are no numbers to the left of
   the first element. For the remaining elements, each value in the left array is the product of its previous value and the
   corresponding value in the input array.

3. Populate the Right Array: similarly, the last element of the right array will always be 1 because there are no numbers to
   the right of the last element. For the remaining elements, each value in the right array is the product of its next value
   and the corresponding value in the input array.

4. Calculate the Result: for each index i, the value in the result array will be the product of left[i] and right[i].
'''

# solution one just a bit easier
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - to store the result array and the left and right product arrays
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left, right, result = [1] * n, [1] * n, [1] * n

        # populate the left array with the product of all
        # elements to the left of the current element
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # populate the right array with the product of all
        # elements to the right of the current element
        # we start from n - 2 because we use i + 1 in the calculation
        # so the first iteration will be n - 1 for both right and nums access
        # will the set in right is at position n - 2 because we have 1 at n - 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # given [2, 3, 4, 5], left = [1, 2, 6, 24], right = [60, 20, 5, 1]
        # so for 2, result[0] = left[0] * right[0] = 1 * 60 = 60
        # for 3, result[1] = left[1] * right[1] = 2 * 20 = 40
        # and so on
        for i in range(n):
            result[i] = left[i] * right[i]

        return result

# solution two
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - to store the result array and the left and right product arrays
from collections import deque

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result =  [1] * n
        left, right = self.buildLeftAndRightProds(nums)

        # given [2, 3, 4, 5], left = [1, 2, 6, 24, 120], right = [120, 60, 20, 5, 1]
        # so for 2, result[0] = left[0] * right[1] = 1 * 60 = 60
        # for 3, result[1] = left[1] * right[2] = 2 * 20 = 40
        # and so on
        for i in range(n):
            result[i] = left[i] * right[i + 1]
        return result

    def buildLeftAndRightProds(self, nums):
        left = [1]
        # use a queue to build the right product array using appendleft()
        right = deque()
        right.append(1)

        # build the left and right product arrays at the same time
        end = len(nums) - 1
        for start in range(len(nums)):
            left.append(left[-1] * nums[start])
            right.appendleft(right[0] * nums[end])
            end -= 1

        return left, right
