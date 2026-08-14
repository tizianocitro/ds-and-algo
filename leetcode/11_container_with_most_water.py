# !code: 11, !difficulty: medium, !from: https://leetcode.com/problems/container-with-most-water/

'''Problem:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 104

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1
'''

# solution one using two pointers
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def maxArea(self, height) -> int:
        max_area = 0

        left, right = 0, len(height) - 1
        while left <= right:
            # compute the area between the two pointers and update the max_area
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            # move the pointer that points to the smaller height
            # because this offers the possibility of finding a larger area
            # by moving the pointer to a larger height
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# solution two using two pointers but less clean than solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def maxArea(self, height) -> int:
        max_area = 0

        left, right = 0, len(height) - 1
        while left <= right:
            # compute the area between the two pointers
            area = min(height[left], height[right]) * (right - left)

            # update the max_area if the current area is larger
            if area > max_area:
                max_area = area
            # move the pointer that points to the smaller height
            # because this offers the possibility of finding a larger area
            # by moving the pointer to a larger height
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
