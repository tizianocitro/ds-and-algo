# !difficulty: medium

# You're given a list of integers nums.
# Write a function that returns a boolean representing whether there exists a zero-sum subarray of nums.
# A zero-sum subarray is any subarray where all of the values add up to zero.
# A subarray is any contiguous section of the array.
# For the purposes of this problem, a subarray can be as small as one element and as long as the original array.

# Input: [-5, -5, 2, 3, 2]
# Output: True // The subarray [-5, 2, 3] sums up to zero.

# solution one
# The key idea here is that if the cumulative sum of numbers at some index i is the same as the cumulative sum at some index j,
# where j > i, then the sum of the elements between i+1 and j must be zero.
# This is because the same total sum is reached at index i and j,
# implying that the sum of elements between i+1 and j didn't change the total sum, hence it must be zero.
# Here's a simple example: consider the array [3, 1, -4, 2, -2]. The cumulative sums are [3, 4, 0, 2, 0].
# Notice that 0 appears twice in the cumulative sums. This means that there's a subarray that sums to zero, specifically 1, -4, 2, -2.
# Complexity:
# O(n) time - where n is the length of nums
# O(n) space - where n is the length of nums used for the set of sums
def zeroSumSubarray(nums):
    sums = set([0])
    sum = 0
    for n in nums:
        sum += n
        if sum in sums:
            return True
        sums.add(sum)
    return False