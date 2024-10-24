# !code: 219, !difficulty: easy, !from: https://leetcode.com/problems/contains-duplicate-ii/

'''Problem:
iven an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

# solution one using sliding window and set
# Complexity:
# O(n) time - where n is the length of the nums array
# O(k) space - where k is input param for the hash map
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        # the checks could be removed
        if k < 1 or len(nums) < 2:
            return False

        chars = set()

        start = 0
        for end in range(len(nums)):
            # if the num is in the window, then the difference
            # between the indexes is less than k
            if nums[end] in chars:
                return True

            chars.add(nums[end])

            # in alternative:
            # if end > k - 1:
            if end - start + 1 > k:
                # remove the start element from the window
                chars.remove(nums[start])
                # move the start pointer forward
                start += 1

        return False

# solution two using sliding window and hash map
# Complexity:
# O(n) time - where n is the length of the nums array
# O(k) space - where k is input param for the hash map
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        # the checks could be removed
        if k < 1 or len(nums) < 2:
            return False

        chars = defaultdict(int)

        start = 0
        for end in range(len(nums)):
            # if the num is in the window, then the difference
            # between the indexes is less than k
            if nums[end] in chars:
                return True

            chars[nums[end]] += 1

            # in alternative:
            # if end > k - 1:
            if end - start + 1 > k:
                # remove the start element from the window
                chars[nums[start]] -= 1
                if chars[nums[start]] == 0:
                    del chars[nums[start]]
                # move the start pointer forward
                start += 1

        return False

# solution three using implicit sliding window and hash set
# Complexity:
# O(n) time - where n is the length of the nums array
# O(k) space - where k is input param for the hash map
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        # the checks could be removed
        if k < 1 or len(nums) < 2:
            return False

        chars = set()

        for end in range(len(nums)):
            # if the num is in the window, then the difference
            # between the indexes is less than k
            if nums[end] in chars:
                return True

            chars.add(nums[end])

            if len(chars) > k:
                # remove the start element from the window
                # we get start by subtracting k from end
                # start = end - k
                chars.remove(nums[end - k])

        return False
