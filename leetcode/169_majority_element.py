# !code: 169, !difficulty: easy, !from: https://leetcode.com/problems/majority-element/

'''Problem:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

# solution one using boyer-moore voting algorithm
# more info: https://leetcode.com/problems/majority-element/editorial/#approach-7-boyer-moore-voting-algorithm
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(1) space
class Solution:
    def majorityElement(self, nums) -> int:
        majority_el = None
        count = 0

        for num in nums:
            if count == 0:
                majority_el = num
            count += 1 if num == majority_el else -1

        return majority_el

# solution two using hash map
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(n) space - we use a hash map to store the frequency of each element in the array
from collections import Counter

class Solution:
    def majorityElement(self, nums) -> int:
        freqs = Counter(nums)
        for num, freq in freqs.items():
            if freq > len(nums) // 2:
                return num
        return -1

# solution three using sorting
# Complexity:
# O(nlogn) time - where n is the number of elements in the array
# O(1) space
class Solution:
    def majorityElement(self, nums) -> int:
        # sort the array
        nums.sort()

        # and then the majority element will be at the middle of the array
        # because there will always be a majority element (stated in the problem)
        return nums[len(nums) // 2]