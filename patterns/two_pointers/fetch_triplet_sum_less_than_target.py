# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638fa5205844e928cbf004bf

''' Problem:
Given an array arr of unsorted numbers and a target sum,
count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return all such triplets.

Input: [-1, 4, 2, 1, 3], target = 5 
Output: [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]
'''

# solution one
# Complexity:
# O(n^3) time - where n is the length of the input array
# The searchPair() will take O(N^2), the main while loop will run in O(N), but the nested for loop can also take O(N),
# this will happen when the target sum is bigger than every triplet in the array.
# O(n) space - where n is the length of the input array (for sorting)
class Solution:
    def searchTriplets(self, arr, target):
        triplets = []
        arr.sort()
        for i in range(len(arr) - 2):
            # avoid duplicates while iterating this array
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            count += self.countPairs(arr, triplets, target, arr[i], i + 1)
        return count
    
    def countPairs(self, arr, triplets, target, current, left):
        count = 0
        right = len(arr) - 1
        while left < right:
            sum = current + arr[left] + arr[right]
            if sum < target:
                # since arr[right] >= arr[left], we can replace arr[right] by any 
                # number between left and right to get a sum less than the target sum
                for i in range(right, left, -1):
                    triplets.append([current, arr[left], arr[i]])
                left += 1
            else:
                right -=1
        return count