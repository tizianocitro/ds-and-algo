# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/validate-binary-search-tree-medium

'''Problem:
Determine if a given binary tree is a binary search tree (BST). In a BST, for each node:
- All nodes to its left have values less than the node's value.
- All nodes to its right have values greater than the node's value.

Input: [5,3,7]
Output: true
Explanation: The left child of the root (3) is less than the root, and the right child of the root (7) is greater than the root. Hence, it's a BST.

Input: [5,7,3]
Output: false
Explanation: The left child of the root (7) is greater than the root, making it invalid.

Input: [10,5,15,null,null,12,20]
Output: true
Explanation: Each subtree of the binary tree is a valid binary search tree. So, a whole binary tree is a valid binary search tree.
'''

# solution one
# Complexity:
# O(v) time - where v is the number of nodes in the tree
# O(v) space - for the recursive call stack
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        return self.isValidSubBST(root, [-float('inf'), float('inf')])

    def isValidSubBST(self, node, possible_values_range):
        # if the node is None, then it is a valid BST
        # because an empty tree is a valid BST
        if not node:
            return True

        # check if the node value is within the possible values range
        min_val, max_val = possible_values_range
        if min_val < node.val < max_val:
            # if it is we check that the left and right subtrees are valid BSTs
            # so we update the possible values range for the left and right subtrees
            # for the left subtree, the max value is the node value and the min value is the current min value
            # for the right subtree, the min value is the node value and the max value is the current max value
            return self.isValidSubBST(node.left, [min_val, node.val]) and \
                self.isValidSubBST(node.right, [node.val, max_val])

        # if the node value is not within the possible values range, then it is not a valid BST
        return False
