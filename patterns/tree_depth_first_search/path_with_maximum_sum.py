# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639b65080dbaa5118a4b5fe4

'''Problem:
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
The path must contain at least one node.

Input: [1, 2, 3, 4, None, 5, 6]
Output: 16
Explanation: The path with the maximum sum is: [4, 2, 1, 3, 6]
'''

# solution one with class level variable
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
import math

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMaximumPathSum(self, root):
        self.global_maximum_sum = -math.inf
        self.dfsMaximumSum(root)
        return self.global_maximum_sum

    def dfsMaximumSum(self, root):
        if root is None:
            return 0

        left_sum = self.dfsMaximumSum(root.left)
        right_sum = self.dfsMaximumSum(root.right)

        # ignore paths with negative sums, since we need to find the maximum sum
        # we should ignore any path which has an overall negative sum
        left_sum = max(left_sum, 0)
        right_sum = max(right_sum, 0)

        # maximum path sum at the current node is equal to the sum from the left 
        # subtree + the sum from right subtree + val of current node
        local_maximum_size = left_sum + right_sum + root.val

        self.global_maximum_sum = max(self.global_maximum_sum, local_maximum_size)

        # maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return max(left_sum, right_sum) + root.val