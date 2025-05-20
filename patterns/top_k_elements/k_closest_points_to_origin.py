# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1cd9e19e6a3ce13cedcbc

'''Problem:
Given an array of points in a 2D plane, find k closest points to the origin.

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
'''

# solution one
# Complexity:
# O(nlogk) time - where n is the length of the input array and k is the input k
# O(k) space - to store the heap
from heapq import *
import math

class Solution:
    def findClosestPoints(self, points, k):
        max_heap = []

        # we use the distance from the origin as the key for the max-heap
        for i in range(k):
            point = points[i]
            distance_from_origin = self.calc_distance_from_origin(point)
            heappush(max_heap, (-distance_from_origin, point))

        for i in range(k, len(points)):
            point = points[i]
            distance_from_origin = self.calc_distance_from_origin(point)

            # if the distance from origin of the current point is less than
            # the distance of the top point of the max-heap, we switch them
            if distance_from_origin < -max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-distance_from_origin, point))

        return [heappop(max_heap)[1] for _ in range(len(max_heap))]

    # The Euclidean distance of a point p = [x,y] from the origin
    # can be calculated through the following formula: sqrt(x^2 + y^2)
    def calc_distance_from_origin(self, p):
        # p[0] is x, p[1] is y
        return math.sqrt((p[0]**2) + (p[1]**2))
