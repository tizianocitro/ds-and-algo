# !code: 189, !difficuty: medium, !from: https://leetcode.com/problems/rotate-array, https://neetcode.io/problems/rotate-array

'''Problem:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

# solution one using two pointers but concise
# Complexity:
# - O(n) time - where n is the length of the input array
# - O(1) space
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        # not really needed but it's a good optimization to avoid doing unnecessary work
        if k == 0:
            return

        # this works because: reverse(A + B) = reverse(B) + reverse(A)
        # so, after reversing the whole array we get: reverse(B) + reverse(A)
        # given:
        # - reverse(reverse(B)) = B
        # - reverse(reverse(A)) = A
        # reversing the first k and the remaining n-k elements gives: B + A
        self.reverse(nums, 0, len(nums) - 1)

        # reverse the first k elements to get B back as reverse(reverse(B)) = B
        self.reverse(nums, 0, k - 1)

        # reverse the remaining n-k elements to get A back as reverse(reverse(A)) = A
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# solution two using two pointers but verbose
# Complexity:
# - O(n) time - where n is the length of the input array
# - O(1) space
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        # not really needed but it's a good optimization to avoid doing unnecessary work
        if k == 0:
            return

        # this works because: reverse(A + B) = reverse(B) + reverse(A)
        # so, after reversing the whole array we get: reverse(B) + reverse(A)
        # given:
        # - reverse(reverse(B)) = B
        # - reverse(reverse(A)) = A
        # reversing the first k and the remaining n-k elements gives: B + A
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # reverse the first k elements to get B back as reverse(reverse(B)) = B
        left, right = 0, k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # reverse the remaining n-k elements to get A back as reverse(reverse(A)) = A
        left, right = k, len(nums) - 1 
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1