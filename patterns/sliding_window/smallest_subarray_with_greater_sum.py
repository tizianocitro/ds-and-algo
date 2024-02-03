# !difficulty: easy

'''Problem:
Given an array of positive integers and a number S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
Return 0 if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], s = 7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to 7 is [5, 2].
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# The outer for loop runs for all n elements, and the inner while loop processes each element only once;
# therefore, the time complexity of the algorithm will be O(n + n), which is asymptotically equivalent to O(n).
# O(1) space
class Solution:
    def findMinSubArray(self, s, arr):
        minLenght = float("inf")
        sum, start = 0, 0

        for end in range(len(arr)):
            sum += arr[end]
            while sum >= s:
                minLenght = min(minLenght, end - start + 1)
                sum -= arr[start]
                start += 1

        if minLenght == float("inf"):
            return 0
        return minLenght  
