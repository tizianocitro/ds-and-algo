# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6399d2d989924acc4bea0939

'''Problem:
Given a binary tree and a number S, find all paths from root-to-leaf such that the sum of all the node values of each path equals S.

Input: [12, 7, 1, 4, None, 10, 5], S = 23
Output: [[12, 7, 4], [12, 1, 10]]
'''

'''Similar Problems:
Problem: Given a binary tree, find the root-to-leaf path with the maximum sum.
Solution: We need to find the path with the maximum sum. As we traverse all paths, we can keep track of the path with the maximum sum.
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once (which will take O(n)), and for every leaf node,
# we might have to store its path (by making a copy of the current path) which will take O(logn) which is the height of the tree for both balanced and unbalanced trees.
# O(nlogn) space - if we ignore the space required for the allPaths list, the space complexity of the above algorithm will be O(n) in the worst case.
# This space will be used to store the recursion stack. The worst-case will happen when the given tree is a linked list (i.e., every node has only one child).
# Since, for binary trees, there exists only one path to reach any leaf node, we can easily say that total root-to-leaf paths in a binary tree can’t be more than the number of leaves.
# As we know that there can’t be more than (n + 1) / 2 leaves in a binary tree, therefore the maximum number of elements in allPaths will be O((n+1)/2) = O(n).
# Now, each of these paths can have many nodes in them. For a balanced binary tree, each leaf node will be at maximum depth.
# As we know that the depth (or height) of a balanced binary tree is O(logn) we can say that, at the most, each path can have logn nodes in it.
# This means that the total size of the allPaths list will be O(nlogn). If the tree is not balanced, we will still have the same worst-case space complexity.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPaths(self, root, required_sum):
        allPaths = []
        self.dfsPaths(root, required_sum, allPaths, [])
        return allPaths

    def dfsPaths(self, root, required_sum, allPaths, currentPath):
        if root is None:
            return
        
        val = root.val

        # add the current node to the path
        currentPath.append(val)

        # if the current node is a leaf and its value is equal to required_sum, save the current path
        if val == required_sum and root.left is None and root.right is None:
            # since lists in Python are mutable objects, when currentPath changes in subsequent recursive calls,
            # it also affects the values stored in allPaths, thus we need to make a copy of the currentPath
            # using list() to make a copy of the currentPath
            # this will take O(logn) time because in the worst case, the currentPath will have logn nodes
            allPaths.append(list(currentPath))
        else:
            self.dfsPaths(root.left, required_sum - val, allPaths, currentPath)
            self.dfsPaths(root.right, required_sum - val, allPaths, currentPath)

        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        del currentPath[-1]
