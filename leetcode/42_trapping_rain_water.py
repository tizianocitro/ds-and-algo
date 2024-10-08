# !code: 42, !difficulty: hard, !from: https://leetcode.com/problems/trapping-rain-water/

'''Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Constraints:
- n == height.length
- 1 <= n <= 2 * 104
- 0 <= height[i] <= 105

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
'''

# solution one using two pointers
# Complexity:
# O(n) time - where n is the number of elements in the height array
# O(1) space
class Solution:
    def trap(self, height) -> int:
        # no need to check the length of the height array because
        # it is guaranteed to be at least 1 by the constraints
        left, right = 0, len(height) - 1

        # this two pointers will keep track of the maximum height
        # to the left and right of the element that we will use to
        # calculate the trapped rain at each step as they will also
        # indicate the limiting factor to how much rain we can trap
        left_max_height, right_max_height = height[left], height[right]

        trapped_rain = 0
        while left < right:
            # if the left max is less than the right max, we move the left pointer
            # because it means that the left side is the limiting factor to how
            # much rain we can trap, otherwise we move the right pointer
            if left_max_height < right_max_height:
                left += 1

                # keep track of the next max left height
                # if you do this update before updating the trapped rain
                # you can avoid the min(0, left_max - height[left])
                left_max_height = max(left_max_height, height[left])
                trapped_rain += left_max_height - height[left]
            else:
                right -= 1

                # keep track of the next max right height
                # if you do this update before updating the trapped rain
                # you can avoid the min(0, right_max - height[right])
                right_max_height = max(right_max_height, height[right])
                trapped_rain += right_max_height - height[right]

        return trapped_rain

# solution two using max left and max right arrays
# Complexity:
# O(n) time - where n is the number of elements in the height array
# O(n) space - for the max left and max right arrays
class Solution:
    def trap(self, height) -> int:
        # no need to check the length of the height array because
        # it is guaranteed to be at least 1 by the constraints
        n = len(height)

        # this will store the maximum height to the left of the current element
        max_left = [0] * n 
        # this will store the maximum height to the right of the current element
        max_right = [0] * n

        # calculate the maximum height to the left of each element
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        # calculate the maximum height to the right of each element
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        # calculate the trapped rain as the minimum of the maximum height to the left
        # and right of the current element minus the height of the current element
        # but then we take the maximum of 0 and the result because we don't want to
        # have negative trapped rain because it doesn't make sense 
        trapped_rain = 0
        for i in range(n):
            min_height = min(max_left[i], max_right[i])
            trapped_rain += max(0, min_height - height[i])

        return trapped_rain