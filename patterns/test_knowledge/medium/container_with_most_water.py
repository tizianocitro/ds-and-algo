# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/container-with-most-water-medium

'''Problem:
Given an array of non-negative integers, where each integer represents the height of a vertical line positioned at index i.
You need to find the two lines that, when combined with the x-axis, form a container that can hold the most water.
The goal is to find the maximum amount of water (area) that this container can hold.

Note: The water container's width is the distance between the two lines, and its height is determined by the shorter of the two lines.

Input: [1,3,2,4,5]
Output: 9
Explanation: The lines at index 1 and 4 form the container with the most water.
The width is 3 * (4-1), and the height is determined by the shorter line, which is 3. Thus, the area is 3 * 3 = 9.

Input: [5,2,4,2,6,3]
Output: 20
Explanation: The lines at index 0 and 4 form the container with the most water.
The width is 5 * (4-0), and the height is determined by the shorter line, which is 5. Thus, the area is 5 * 4 = 20.

Input: [2,3,4,5,18,17,6]
Output: 17
Explanation: The lines at index 4 and 5 form the container with the most water.
The width is 17 * (5-4), and the height is determined by the shorter line, which is 17. Thus, the area is 17 * 1 = 17.
'''

# solution one using two pointers
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def maxArea(self, height):
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

# solution two using min and max pointers
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def maxArea(self, height):
        # keep track of the max area, and the min and max pointers
        # - min_current points to the smaller of the two heights and is update to the be
        #   min_current = max_current everytime ww find a new max_current
        # - max_current points to the larger of the heights we find while traversing the array
        max_area = min_current = max_current = 0

        for i in range(1, len(height)):
            current = height[i]

            # compute the area between the min and max pointers and the current height
            a_min = min(current, height[min_current]) * (i - min_current)
            a_max = min(current, height[max_current]) * (i - max_current)
            max_area = max(max_area, a_min, a_max)

            # update min and max pointers accordint to what was stated above
            min_current = max_current if current > height[max_current] else min_current
            max_current = i if current > height[max_current] else max_current

        return max_area