# !code: 238, !from: medium, !from: https://leetcode.com/problems/product-of-array-except-self/

'''Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Follow up:
Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis)

Constraints:
- 2 <= nums.length <= 105
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# solution one using prefix and suffix product implicitely
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - to store the answer array
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # build the answer array as you would build the left product array
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # then we update answer[i] by multiplying it (it contains the left product)
        # with its right product i.e., the product of all elements in nums to the right of answer[i]
        # and the right product is built in place starting from the rightmost element
        # that has a right product of 1
        right_prod = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right_prod
            right_prod *= nums[i]

        return answer

# solution two using prefix and suffix product arrays
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - to store the left and right product arrays as well as the answer array
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        left_prod = [1] * n
        right_prod = [1] * n

        # build left and right product arrays (prefix sum and suffix sum-like)
        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]

        answer = [1] * n

        # multiply left and right product arrays to get the answer
        for i in range(n):
            answer[i] = left_prod[i] * right_prod[i]

        return answer
