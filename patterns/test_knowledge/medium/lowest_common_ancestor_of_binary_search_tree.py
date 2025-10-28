# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/lowest-common-ancestor-of-a-binary-search-tree-medium

'''Problem:
Given a binary search tree (BST) and two of its nodes, find the node that is the lowest common ancestor (LCA) of the two given nodes.
The LCA of two nodes is the node that lies in between the two nodes in terms of value and is the furthest from the root.
In other words, it's the deepest node where the two nodes diverge in the tree.
Remember, in a BST, nodes have unique values.

Constraints:
- The number of nodes in the tree is in the range [2, 105]
- All Node.val are unique
- p != q
- p and q will exist in the BST

Input:
    BST: [6,2,8,0,4,7,9,null,null,3,5]
    Node 1: 2
    Node 2: 8
Output: 6
Explanation: The nodes 2 and 8 are on the left and right children of node 6. Hence, node 6 is their LCA.

Input:
    BST: [6,2,8,0,4,7,9,null,null,3,5]
    Node 1: 0
    Node 2: 3
Output: 2
Explanation: The nodes 0 and 3 are on the left and right children of node 2, which is the closest ancestor to these nodes.

Input:
    BST: [6,2,8,0,4,7,9,null,null,3,5]
    Node 1: 4
    Node 2: 5
Output: 4
Explanation: Node 5 is the right child of node 4. Hence, the LCA is node 4 itself.
'''

'''Notes:
See also the problem on Leetcode: leetcode/235_lowest_common_ancestor_of_a_binary_search_tree.py
'''

# solution one
# Complexity:
# O(h) time - where h is the height of the tree which is h = log(n) for balanced trees and h = n for skewed trees
# O(h) space - where h is the height of the tree which is h = log(n) for balanced trees and h = n for skewed trees
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        # if the current node is p or q, return the current node
        if root.val == p or root.val == q:
            return root.val

        # if both nodes are less than the current node, then the LCA
        # is in the left subtree, so no need to check the right subtree
        if p < root.val and q < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # if both nodes are greater than the current node, then the LCA
        # is in the right subtree, so no need to check the left subtree
        elif p > root.val and q > root.val:
            return self.lowestCommonAncestor(root.right, p, q)      

        # if one node is less than the current node and the other
        # is greater, then the LCA is the current node
        return root.val