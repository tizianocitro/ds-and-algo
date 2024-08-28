# !code: 257, !difficulty: easy, !from: https://leetcode.com/problems/binary-tree-paths/

'''Problem:
Given a binary tree, return all root-to-leaf paths.

Input: [1,2,3,null,5]
Output: ["1->2->5","1->3"]
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of nodes in the tree and logn is the max length of a path
# O(nlogn) space - where n is the number of nodes in the tree and logn is the max length of a path
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        all_paths = []
        self.dfsPaths(root, all_paths, [])
        return all_paths

    def dfsPaths(self, root, all_paths, current_path):
        if root is None:
            return

        # since lists in python are mutable objects, when current_path changes
        # in subsequent recursive calls, it also affects the values stored in
        # all_paths, thus we need to make a copy of the current_path
        current_path.append(root.val)

        if root.left is None and root.right is None:
            all_paths.append("->".join([str(n) for n in current_path]))
        else:
            self.dfsPaths(root.left, all_paths, current_path)
            self.dfsPaths(root.right, all_paths, current_path)

        del current_path[-1]
