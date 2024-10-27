# !code: 230, !difficulty: medium, !from: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

'''Problem:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Constraints:
- The number of nodes in the tree is n
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Follow-Up Question:
If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

# solution one using recursive inorder traversal (dfs)
# with optimized space and time complexity
# Complexity:
# O(max(h, k)) time - where h is the height of the tree and k is the number of elements in the inorder array
# O(max(h, k)) space - where h is the height of the tree and k is the number of elements in the inorder array
# because if the tree is skewed, the height of the tree will be equal to the number of nodes in the tree
# so the space complexity will be O(n), otherwise, it will be O(k)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = []
        self.dfs(root, inorder, k)
        # the kth smallest element is the kth element in the inorder traversal
        # k - 1 because the array is 0-indexed
        return inorder[k - 1]

    # inorder traversal ensures that the nodes are visited in ascending order
    def dfs(self, node, inorder, k):
        if not node:
            return

        # first visit left node
        if node.left:
            self.dfs(node.left, inorder, k)

        # then visit the current node
        inorder.append(node.val)

        # when the inorder array has k elements, we can stop the traversal
        # because in position k - 1, we have the kth smallest element
        if len(inorder) == k:
            return

        # then visit right node
        if node.right:
            self.dfs(node.right, inorder, k)

# solution two using recursive inorder traversal (dfs)
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - for the inorder array
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = []
        self.dfs(root, inorder)
        # the kth smallest element is the kth element in the inorder traversal
        # k - 1 because the array is 0-indexed
        return inorder[k - 1]

    # inorder traversal ensures that the nodes are visited in ascending order
    def dfs(self, node, inorder):
        if not node:
            return

        # first visit left node
        if node.left:
            self.dfs(node.left, inorder)

        # then visit the current node
        inorder.append(node.val)

        # then visit right node
        if node.right:
            self.dfs(node.right, inorder)

# solution three using iterative inorder traversal (dfs)
# Complexity:
# O(h) time - where h is the height of the tree, but for skewed trees, it will be O(n)
# O(h) space - where h is the height of the tree, but for skewed trees, it will be O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            # visit left nodes first until there are no more left nodes
            while root:
                stack.append(root)
                root = root.left

            # pop the last left node visited
            root = stack.pop()
            k -= 1
            # if k is 0, then we have found the kth smallest element
            if not k:
                return root.val

            # visit the right node
            root = root.right