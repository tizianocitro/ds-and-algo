# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638f976d20f87893374e4e6b

''' Problem:
Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

Input: [2, 5, 3, 10], target = 30
Output: [[2], [5], [2, 5], [3], [5, 3], [10]] // There are six contiguous subarrays whose product is less than the target.
'''

# solution one with sliding window
# Complexity:
# O(N^3) time - N for the outer loop and N for the inner loop (list() is O(N))
# O(N) space - for the result list
'''
If we do not ignore the space required for the output list, the algorithm needs more space which is used for the contiguos list.

For an array with distinct elements, finding all of its contiguous subarrays
is like finding the number of ways to choose two indices, i and j, in the array such that i <= j.

If there are a total of n elements in the array, here is how we can count all the contiguous subarrays:
- When i = 0, j can have any value from 0 to n-1, giving a total of n choices.
- When i = 1, j can have any value from 1 to n-1, giving a total of n-1 choices.
- Similarly, when i = 2, j can have n-2 choices.
- When i = n-1, j can only have only 1 choice.
Combining all the choices we get: [n * (n + 1)] / 2.
So, at most, we need space for O(N^2) output lists, making our space complexity O(N^3).
'''
class Solution:
    def findSubarrays(self, arr, target):
        result = []
        left, right = 0, 0
        prod = 1

        while right < len(arr):
            prod *= arr[right]
            while prod >= target and left < len(arr):
                prod /= arr[left]
                left += 1
            contiguos = []

            # !IMPORTANT: we need to iterate from right to left
            # range(right, left - 1, -1) because we need the combination of the arr[right] element
            # with the previous elements till left, not the opposite
            # For example, given the array arr = [1, 2, 3, 4] and indices left = 1 and right = 3,
            # range(left, right) would generate subarrays [2], [2, 3], [2, 3, 4],
            # while range(right, left - 1, -1) would generate subarrays [4], [4, 3], [4, 3, 2].
            for i in range(right, left - 1, -1):
                # this adds at the beginning of the list to be ordered
                # contiguos.insert(0, arr[i])
                contiguos.append(arr[i])
                result.append(list(contiguos))
            right += 1
        
        return result


# solution two using no sliding window
# Complexity:
# O(N^3) time - N^2 for the outer loop and N for the inner loop (list() is O(N))
# O(N) space - for the result list
'''
If we do not ignore the space required for the output list, the algorithm needs more space which is used for the contiguos list.

For an array with distinct elements, finding all of its contiguous subarrays
is like finding the number of ways to choose two indices, i and j, in the array such that i <= j.

If there are a total of n elements in the array, here is how we can count all the contiguous subarrays:
- When i = 0, j can have any value from 0 to n-1, giving a total of n choices.
- When i = 1, j can have any value from 1 to n-1, giving a total of n-1 choices.
- Similarly, when i = 2, j can have n-2 choices.
- When i = n-1, j can only have only 1 choice.
Combining all the choices we get: [n * (n + 1)] / 2.
So, at most, we need space for O(N^2) output lists, making our space complexity O(N^3).
'''
class Solution:
    def findSubarrays(self, arr, target):
        result = []
        left = 0
        right = left + 1

        while left < len(arr):
            current = arr[left]
            currentSum = current
            contiguos = [current]

            while right < len(arr) and currentSum * arr[right] < target:
                result.append(list(contiguos))
                currentSum *= arr[right]
                contiguos.append(arr[right])
                right += 1

            # add the last element when the and condition is not satisfied
            # this is because we add previous elements when the condition is satisfied
            # So, if we have 2 * 5, we add 2.
            # In the next iteration we add 2 * 5 but we have 2 * 5 * 3, whihc fails the condition
            result.append(contiguos)
            left += 1
            right = left + 1

        return result
