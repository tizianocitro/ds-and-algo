# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6393a98bd8a93f4bff961b4d

'''Problem:
We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence.
This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n) and without using any extra space.
For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# Although we are not incrementing the index i when swapping the numbers,
# this will result in more than n iterations of the loop, but in the worst-case scenario,
# the while loop will swap a total of n-1 numbers, and once a number is at its correct index,
# we will move on to the next number by incrementing i.
# O(1) space
class Solution:
    def sort(self, nums):
        i = 0
        while i < len(nums):
            num = nums[i]
            # the number at index i should be i + 1
            # (e.g. 1 at index 0, 2 at index 1, etc)
            if num == i + 1:
                i += 1
                continue
            nums[i], nums[num - 1] = nums[num - 1], nums[i]
        return nums

# solution two
# Complexity:
# O(n) time - where n is the length of the input array
# Although we are not incrementing the index i when swapping the numbers,
# this will result in more than n iterations of the loop, but in the worst-case scenario,
# the while loop will swap a total of n-1 numbers, and once a number is at its correct index,
# we will move on to the next number by incrementing i.
# O(1) space
class Solution:
    def sort(self, nums):
        i = 0
        while i < len(nums):
            # calculate the index where the current element should be placed
            j = nums[i] - 1
            # check if the current element is not in its correct position
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                # if the current element is already in its correct position, move to the next element.
                i += 1
        return nums