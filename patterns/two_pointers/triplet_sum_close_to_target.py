# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638f7323ae53511bdc364dab

''' Problem:
Given an array of unsorted numbers and a target number,
find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet.
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Input: [-1, 0, 2, 3], target=3 
Output: 2 // The triplet [-1, 0, 3] has the sum '2' which is closest to the target.
There are two triplets with distance '1' from the target: [-1, 0, 3] & [-1, 2, 3].
Between these two triplets, the correct answer will be [-1, 0, 3] as it has a sum '2',
which is less than the sum of the other triplet which is '4'.
This is because of the following requirement: 'If there are more than one such triplet, return the sum of the triplet with the smallest sum.'
'''

# solution one
# Complexity:
# O(n^2) time - where n is the length of the input array
# O(n) space - where n is the length of the input array (for sorting)
class Solution:
    def searchTriplet(self, arr, target_sum):
        arr.sort()
        minDist, minSum = float('inf'), float('inf')

        for i in range(len(arr)):
            current = arr[i]
            if i > 0 and current == arr[ i - 1]:
                continue

            left, right = i + 1, len(arr) - 1
            while left < right:
                sum = arr[left] + arr[right] + current
                dist = abs(sum - target_sum)
                if dist < minDist or (dist == minDist and sum < minSum):
                    minDist = dist
                    minSum = sum
                    
                    if sum < target_sum:
                        left += 1
                    else:
                        right -= 1

        return minSum

# solution two which skips the last two elements
# Complexity:
# O(n^2) time - where n is the length of the input array
# O(n) space - where n is the length of the input array (for sorting)
class Solution:
    def searchTriplet(self, arr, target_sum):
        arr.sort()
        minDist, minSum = float('inf'), float('inf')

        # We skip the last 2 numbers because we are looking for triplets
        # and thus don't need to consider the last two positions in this loop
        for i in range(len(arr) - 2):
            current = arr[i]
            if i > 0 and current == arr[ i - 1]:
                continue

            left, right = i + 1, len(arr) - 1
            while left < right:
                sum = arr[left] + arr[right] + current
                dist = abs(sum - target_sum)
                if dist < minDist or (dist == minDist and sum < minSum):
                    minDist = dist
                    minSum = sum
                    
                    if sum < target_sum:
                        left += 1
                    else:
                        right -= 1

        return minSum
