# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/counting-subarrays-with-product-less-than-a-target-medium

'''Problem:
Given an array nums with positive numbers and a positive integer target,
return the count of contiguous subarrays whose product is less than the target number.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= target <= 10^6

Input: nums = [2, 5, 3, 10], target = 30
Output: 6
Explanation: There are six contiguous subarrays ([2], [5], [2, 5], [3], [5, 3], [10]) whose product is less than the target.

Input: nums = [8, 2, 6, 5], target = 50
Output: 7
Explanation: There are seven contiguous subarrays ([8], [2], [8, 2], [6], [2, 6], [5], [6, 5]) whose product is less than the target.

Input: nums = [10, 5, 2, 6], target = 0
Expected Output: 7
Explanation: Subarrays with product less than 0 does not exist.
'''

# solution one using two pointers
# Complexity:
# O(n) time - where n is the length of the array because we iterate through the array once
# and consider each element at most twice (once when we add it to the total count and once when we remove it)
# O(1) space
class Solution:
    def findSubarrays(self, nums, target):
        total_count = 0

        # there is no positive product less than or equal to 1
        if target <= 1:
            return 0

        left = 0
        current_prod = 1
        for right in range(len(nums)):
            num = nums[right]
            # if the current number is less than the target, we add 1 to the total count
            # because the subarray with this number only is a valid subarray
            if num < target:
                total_count += 1

            current_prod *= num
            while current_prod >= target and left < len(nums):
                current_prod //= nums[left]
                left += 1

            # in the while above we might end up with:
            # - left == right if nums[right] < target
            # - left > right if nums[right] >= target
            if left < right:
                # if we have an array of x numbers where the product
                # is less than target, it means the product of all
                # contiguos subarrays within that array is less than target
                # if nums = [1, 2, 3, 4], target = 10, current_prod = 3,
                # and the portion of the array identified by left = 0 and right = 2 is [1, 2, 3],
                # we add 2 - 0 = 2 to the total count because:
                # - we have already consired [1, 2] and [2] as valid subarrays in the previous iteration
                # - +1 for [1, 2, 3] because 1 * 2 * 3 < 10
                # - +1 for [2, 3] because 2 * 3 < 10 and we have not considered it yet
                # and so on
                total_count += right - left

        return total_count

# solution two same as solution one but a bit cleaner
# Complexity:
# O(n) time - where n is the length of the array because we iterate through the array once
# and consider each element at most twice (once when we add it to the total count and once when we remove it)
# O(1) space
class Solution:
    def findSubarrays(self, nums, target):
        total_count = 0

        # there is no positive product less than or equal to 1
        if target <= 1:
            return 0

        left = 0
        current_prod = 1
        for right in range(len(nums)):
            current_prod *= nums[right]

            while current_prod >= target and left < len(nums):
                current_prod //= nums[left]
                left += 1

            # if we have an array of x numbers where the product
            # is less than target, it means the product of all
            # contiguos subarrays within that array is less than target
            # if nums = [1, 2, 3, 4], target = 10, current_prod = 3,
            # and the portion of the array identified by left = 0 and right = 2 is [1, 2, 3],
            # we add 2 - 0 = 2 to the total count because:
            # - we have already consired [1, 2] and [2] as valid subarrays in the previous iteration
            # - +1 for [1, 2, 3] because 1 * 2 * 3 < 10
            # - +1 for [2, 3] because 2 * 3 < 10 and we have not considered it yet
            # and so on
            # the +1 is because we have not considered the subarray with the current number only
            total_count += (right - left) + 1

        return total_count