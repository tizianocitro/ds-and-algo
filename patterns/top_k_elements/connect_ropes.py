# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1ceee19e6a3ce13ceddd0

'''Problem:
Given N ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
The cost of connecting two ropes is equal to the sum of their lengths.

Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

Input: [3, 4, 5, 6]
Output: 36
Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)

Input: [1, 3, 11, 5, 2]
Output: 42
Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of ropes
# O(n) space - to store the ropes in the heap
from heapq import *

class Solution:
    def minimumCostToConnectRopes(self, ropeLengths):
        # hapify the ropes to get the smallest rope at the top,
        # so that we can connect the smallest ropes first
        min_heap = ropeLengths
        heapify(min_heap)

        # keep track of the total cost while connecting ropes
        cost = 0

        # keep connecting the smallest ropes until we are left with one rope,
        # meaning all the ropes are connected and we have our final cost
        while len(min_heap) > 1:
            # get the two smallest ropes and connect them
            rope1 = heappop(min_heap)
            rope2 = heappop(min_heap)
            new_rope = rope1 + rope2

            # put the new rope back in the heap
            # and add the cost to the total cost
            heappush(min_heap, new_rope)
            cost += new_rope

        return cost
