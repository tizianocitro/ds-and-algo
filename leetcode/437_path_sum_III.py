# !code: 437, !difficult: medium, !from: https://leetcode.com/problems/path-sum-iii/

'''Problem:
Given the root of a binary tree and an integer target_sum, return the number of paths where the sum of the values along the path equals target_sum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Constraints:
- The number of nodes in the tree is in the range [0, 1000]
- -109 <= node.val <= 109
- -1000 <= target_sum <= 1000

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], target_sum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], target_sum = 22
Output: 3
'''

# solution one using dfs and prefix sum
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - for the prefix_sum dictionary
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> int:
        # initialize prefix_sum dictionary with base case (0 sum occurs once)
        prefix_sum = {0: 1}

        return self.dfs(root, 0, target_sum, prefix_sum)

    def dfs(self, node, curr_sum, target_sum, prefix_sum):
        if not node:
            return 0

        # update the current cumulative sum with the current node value
        curr_sum += node.val

        # check if there exists a path that sums to target_sum ending at this node
        path_count = prefix_sum.get(curr_sum - target_sum, 0)

        # update the prefix_sum map with the current cumulative sum
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        # explore the left subtree and right subtree
        path_count += self.dfs(node.left, curr_sum, target_sum, prefix_sum)
        path_count += self.dfs(node.right, curr_sum, target_sum, prefix_sum)

        # backtrack: after processing this node and its children, remove the current sum
        # from prefix_sum to avoid affecting other branches
        prefix_sum[curr_sum] -= 1

        return path_count
