# !code: 27, !difficulty: easy, !from: https://leetcode.com/problems/remove-element/

'''Problem:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
  The remaining elements of nums are not important as well as the size of nums.
- Return k.

Custom Judge:
The judge will test your solution with the following code:
    int[] nums = [...]; // Input array
    int val = ...; // Value to remove
    int[] expectedNums = [...]; // The expected answer with correct length.
                                // It is sorted with no values equaling val.

    int k = removeElement(nums, val); // Calls your implementation

    assert k == expectedNums.length;
    sort(nums, 0, k); // Sort the first k elements of nums
    for (int i = 0; i < actualLength; i++) {
        assert nums[i] == expectedNums[i];
    }
If all assertions pass, then your solution will be accepted.

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

# solution one using two pointers
# this approach is better if the number of elements that are equal to val
# is less than the number of elements that are not equal to val
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(1) space
class Solution:
    def removeElement(self, nums, val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                # if the element is equal to val, swap it with the element at right
                nums[left], nums[right] = nums[right], nums[left]
                # and exclude the element now at right
                right -= 1
            else:
                # if the element is not equal to val, just move the left pointer
                left += 1

        # the elements on the left of right are
        # the elements that are not equal to val
        # we return right + 1 because it will be used in nums[:right]
        # so to include the last element we need to add 1
        return right + 1

# solution two using two pointers
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(1) space
class Solution:
    def removeElement(self, nums, val: int) -> int:
        n = len(nums)

        # move left to the first occurrence of val
        left = 0
        while left < n and nums[left] != val:
            left += 1

        # move right to the first element that is not equal to val after left
        right = left
        while right < n and nums[right] == val:
            right += 1

        # the number of elements that are not equal to val is equal to
        # number of elements that are in the positions from 0 to left - 1
        # because we left is on the first occurrence of val
        k = left - 1

        while left < n and right < n:
            # if the element at right is not equal to val
            # swap it with the element at left (which is equal to val)
            # and increment k
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                k += 1

            # move left to the next occurrence of val
            while left < n and nums[left] != val:
                left += 1
            # move right to the next element that is not equal to val
            while right < n and nums[right] == val:
                right += 1

        # return k + 1 because k is the index of the last element that is not equal to val
        return k + 1
