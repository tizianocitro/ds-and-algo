# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd6ec0b9c2c77f772d5970

'''Problem:
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given key is present in it.

Write a function to return the index of the key in the rotated array. If the key is not present, return -1.
The given array may contain duplicates.

Input: [3, 7, 3, 3, 3], key = 7
Output: 1
Explanation: '7' is present in the array at index '1'.
'''

'''Solution idea:
After calculating the middle, we can compare the numbers at indices start and middle. This will give us two options:
1. If arr[start] <= arr[middle], the numbers from start to middle are sorted in ascending order.
2. Else, the numbers from middle + 1 to end are sorted in ascending order.

Once we know which part of the array is sorted, it is easy to adjust our ranges.
For example, if option-1 is true, we have two choices:
1. By comparing the key with the numbers at index start and middle we can easily find out
   if the key lies between indices start and middle; if it does, we can skip the second part => end = middle - 1.
2. Else, we can skip the first part => start = middle + 1.

The code above will fail in case of duplicate because we also need to take into account
the problematic scenario where the numbers at indices start, middle, and end are the same, as in this case,
we can’t decide which part of the array is sorted. In such a case, the best we can do is to skip one number from both ends,
so: start = start + 1, end = end - 1.
'''

# solution two with direction
# Complexity:
# O(n) time - where n is the number of elements in the input array
# this is because when start == middle == end, we need to skip one number from both ends
# so, in the worst case, we will be doing O(n) operations
# O(1) space
class Solution:
    def search(self, arr, key):
        # left -> start, right -> end
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == key:
                return middle

            # the only difference from the previous solution,
            # if numbers at indexes start, mid, and end are same, we can't choose a side
            # the best we can do, is to skip one number from both ends as key != arr[mid]
            # in the worst case, this will cost O(n) time
            if arr[left] == arr[middle] and arr[right] == arr[middle]:
                left += 1
                right -= 1
                continue

            if arr[left] <= arr[middle]: # left side is sorted in ascending order
                if key >= arr[left] and key < arr[middle]:
                    right = middle - 1
                else: # key > arr[mid]
                    left = middle + 1
            else: # right side is sorted in ascending order
                if key > arr[middle] and key <= arr[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        # we are not able to find the element in the given array
        return -1
