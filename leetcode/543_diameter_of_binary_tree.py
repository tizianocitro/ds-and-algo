# !code: 543, !difficulty: easy, !from: https://leetcode.com/problems/diameter-of-binary-tree/

'''Problem:
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Input: root = [1,2]
Output: 1
'''

# solution one using dfs
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree for the recursion stack
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.dfsDiameter(root)

        # minus 1 because we are counting edges not nodes
        return self.diameter - 1 

    def dfsDiameter(self, root):
        if not root:
            return 0

        # recursively get the longest path of left and right subtree
        left_longest = self.dfsDiameter(root.left)
        right_longest = self.dfsDiameter(root.right)

        # update the diameter at each node
        diameter = left_longest + right_longest + 1
        self.diameter = max(self.diameter, diameter)

        # return the longest path of the current node
        # deep to its subtrees to the upper level
        return max(left_longest, right_longest) + 1