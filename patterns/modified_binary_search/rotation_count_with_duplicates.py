# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd6ef9be2006431ceac540

'''Problem:
Given an array of numbers which is sorted in ascending order and is rotated k times around a pivot, find k.

The given array can contain duplicates.

Keep in mind that k can be 0, so the given array is an ascending array that is possibly rotated.

Input: [3, 3, 7, 3]
Output: 3
Explanation: The array has been rotated 3 times.
'''

# solution oen by finding the peak
# Complexity:
# O(n) time - where n is the number of elements in the input array
# this is because when start == middle == end, we could need to only skip one number
# from both ends, so, in the worst case, we will be doing O(n) operations
# O(1) space
class Solution:
    # the idea is that the number or rotations is equal
    # to the index of the smallest number
    def countRotations(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            middle = left + (right - left) // 2

            # if element at mid is greater than the next element
            # than the element at mid + 1 is the smallest
            if middle < right and arr[middle] > arr[middle + 1]:
                return middle + 1

            # if element at mid is smaller than the previous element
            # than mid is the smallest element
            if middle > left and arr[middle - 1] > arr[middle]:
                return middle

            # this is the only difference from the previous solution
            # if numbers at indices start, mid, and end are same, we can't choose a side
            # the best we can do is to skip one number from both ends if they are not the 
            # smallest number
            if arr[left] == arr[middle] and arr[right] == arr[middle]:
                # if element at start + 1 is not the smallest
                if arr[left] > arr[left + 1]:
                    return left + 1
                left += 1
                # if the element at end is not the smallest
                if arr[right - 1] > arr[right]:
                    return right
                right -= 1
            # left side is sorted, so the pivot is on right side
            elif arr[left] < arr[middle] or (arr[left] == arr[middle] and arr[middle] > arr[right]):
                left = middle + 1
            else:  # right side is sorted, so the pivot is on the left side
                right = middle - 1

        # the array has not been rotated
        return 0