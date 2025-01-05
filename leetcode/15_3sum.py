# !code: 15, !difficulty: medium, !from: https://leetcode.com/problems/3sum/

'''Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
- 3 <= nums.length <= 3000
- -105 <= nums[i] <= 105

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

# solution one using two pointers
# Complexity:
# O(n^2) time - where n is the length of the input array
# O(n) space - for sorting
class Solution:
    def threeSum(self, nums):
        # sort the number to make it easier to find duplicates
        # and move pointers based on the sum
        nums.sort()

        triplets = []
        for i, num in enumerate(nums):
            # do not start the search from duplicates
            if i > 0 and num == nums[i - 1]:
                continue

            # find the remaining two numbers that sum up to zero
            self.findTripletsToZero(nums, triplets, i, num)

        return triplets

    def findTripletsToZero(self, nums, triplets, i, num):
        # start searching from the next number after num
        # because we need i != left != right
        left, right = i + 1, len(nums) - 1

        # left and right should be left != right
        while left < right:
            total = num + nums[left] + nums[right]

            # if we get the sum, add it to the triplets
            if total == 0:
                triplets.append([num, nums[left], nums[right]])
                left += 1
                right -= 1

                # skip duplicates because we need unique triplets
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            # if the sum is less than zero, move left pointer because we need a bigger number
            elif total < 0:
                left += 1
            # if the sum is greater than zero, move right pointer because we need a smaller number
            else:
                right -= 1
