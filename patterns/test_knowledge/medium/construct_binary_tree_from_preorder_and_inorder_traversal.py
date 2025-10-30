# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/construct-binary-tree-from-preorder-and-inorder-traversal-medium

'''Problem:
Given the preorder and inorder traversal sequences of a binary tree, your task is to reconstruct this binary tree.
Assume that the tree does not contain duplicate values.

Input:
    Preorder: [1,2,4,5,3,6,7]
    Inorder: [4,2,5,1,6,3,7]
Output:
    Tree Representation: [1,2,3,4,5,6,7]

Explanation: The first value in preorder (1) is the root. In the inorder list, everything left of value 1 is the left subtree and everything on the right is the right subtree.
Following this pattern recursively helps in reconstructing the binary tree. All null value represents the leaf node.

Input:
    Preorder: [8,5,9,7,1,12,2,4,11,3]
    Inorder: [9,5,1,7,2,12,8,4,3,11]
Output:
    Tree Representation: [8,5,4,9,7,11,1,12,2,null,3]

Explanation: Start with 8 (from preorder) as the root. Splitting at 8 in inorder, we find the left and right subtrees. Following this pattern recursively, we can construct the tree.

Input:
    Preorder: [3,5,6,2,7,4,1,9,8]
    Inorder: [6,5,7,2,4,3,9,1,8]
Output:
    Tree Representation: [3,5,1,6,2,9,8,null,null,7,4]
Explanation: Following the same approach, using 3 as root from preorder, we split the inorder sequence into left and right subtrees and continue recursively.
'''

# solution one
# Complexity:
# O(n) time - we are visiting each of the n nodes once, and the look-up for the inorder index is constant time (due to hash map)
# O(n) space - the space is majorly used for the hash map and the recursive stack
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = self.right = None

class Solution:
    def __init__(self):
        self.pre_index = 0
        self.inorder_index_map = {}

    def buildTree(self, preorder, inorder):
        # create a dictionary to store the indices of values in the inorder list
        self.inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        return self.constructTree(preorder, 0, len(inorder) - 1)

    def constructTree(self, preorder, in_start, in_end):
        # base case: if the start index is greater than the end index, return None
        # this happens when we have reached a leaf node
        if in_start > in_end:
            return None

        # get the value at the current preorder index as the root value
        root_val = preorder[self.pre_index]
        self.pre_index += 1
        root = TreeNode(root_val)

        # if the start index is equal to the end index, return the root node
        if in_start == in_end:
            return root

        # find the index of the root value in the inorder list
        root_in_index = self.inorder_index_map[root_val]

        # recursively construct the left and right subtrees
        root.left = self.constructTree(preorder, in_start, root_in_index - 1)
        root.right = self.constructTree(preorder, root_in_index + 1, in_end)

        return root

def printTree(root):
    if not root:
        return

    # using array to simulate a queue
    queue = [root]
    while queue:
        level_size = len(queue)
        is_last_level = True

        for _ in range(level_size):
            current = queue.pop(0)
            if current:
                print(current.val, end=' ')
                queue.append(current.left)
                queue.append(current.right)
                if current.left or current.right:
                    is_last_level = False
            else:
                print('null', end=' ')

        if is_last_level:
            break