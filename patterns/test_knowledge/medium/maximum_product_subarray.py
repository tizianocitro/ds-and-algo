# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/maximum-product-subarray-medium

'''Problem:
Given an integer array, find the contiguous subarray (at least one number in it) that has the maximum product. Return this maximum product.

Input: [2,3,-2,4]
Output: 6
Explanation: The subarray [2,3] has the maximum product of 6.

Input: [-2,0,-1]
Output: 0
Explanation: The subarray [0] has the maximum product of 0.

Input: [-2,3,2,-4]
Output: 48
Explanation: The subarray [-2,3,2,-4] has the maximum product of 48.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space - since we only use a few variables to store the current minimum and maximum products
class Solution:
    def maxProduct(self, nums):
        # if the input array is empty, the maximum product is 0
        if not nums:
            return 0

        # initialize the maximum product, the current minimum and maximum products
        # since a negative number can turn a large negative product into a large
        # positive product, and viceversa, we need to keep track of both the
        # maximum and minimum product at each step
        max_product = min_current = max_current = nums[0]

        # iterating from start to finish works because the product can become smaller
        # as we move through the array only in case of a negative number or zero
        for i in range(1, len(nums)):
            # handle negative numbers
            # calculate the current product of the current element
            # and the current minimum and maximum products
            # this is because the current element can be negative, so we
            # need to check which is that becomes the maximum
            # the product of the current element with the current minimum
            # or its prodict with the current maximum
            prod_max = max_current * nums[i]
            prod_min = min_current * nums[i]

            # in addition to handling negative numbers, we also handle zeros by including nums[i] in the max() and min()
            # if the current number is bigger than both the products, then it means
            # we just consider it as the maximum product so far
            # consider nums[i] = -1, prod_max = -2, prod_min = -3, then max_current = -1
            # consider also that nums[i-1] = 0 and nums[i] = 1, then prod_max = 0, prod_min = 0, but max_current = 1
            max_current = max(nums[i], prod_max, prod_min)
            min_current = min(nums[i], prod_max, prod_min)

            max_product = max(max_product, max_current)

        return max_product