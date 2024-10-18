# !code: 1650, !difficulty: medium, !from: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

'''Problem:
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node parent;
    }
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that
has both p and q as descendants (where we allow a node to be a descendant of itself)."

Constraints:
- The number of nodes in the tree is in the range [2, 105]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q exist in the tree

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

Input: root = [1,2], p = 1, q = 2
Output: 1
'''

# solution one using depth
# Complexity:
# O(n) time - where n is the number of nodes in the tree if the tree is a skewed tree
# it would be O(h) space where h is the height of the tree
# O(1) space
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        # not actually needed, but it allows us to skip the depth count
        # in the case we are given the same node for p and q
        if p == q:
            return p

        # find the depth of p and q
        p_depth = self.getDepth(p)
        q_depth = self.getDepth(q)

		# make the lower node reach the same height as the higher node
        # one of the two loops will not be executed
        while p_depth > q_depth:
            p = p.parent
            p_depth -= 1

        while q_depth > p_depth:
            q = q.parent
            q_depth -= 1

		# now that they are at the same depth, move them up the
        # tree in parallel until they meet at the LCA
        while p != q:
            p = p.parent
            q = q.parent

        # either p or q is the LCA
        return p

    def getDepth(self, p: Node) -> int:
        depth = 0
        while p:
            p = p.parent
            depth += 1
        return depth

# solution two using sets
# Complexity:
# O(n) time - where n is the number of nodes in the tree if the tree is a skewed tree
# it would be O(h) space where h is the height of the tree
# O(n) space - where n is the number of nodes in the tree if the tree is a skewed tree
# it would be O(h) space where h is the height of the tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        # paths from p and q to root
        p_path, q_path = set([p]), set([q])

        # while p or q is not None, meaning there are still parents to visit
        # in the paths from either p or q to the root
        while p or q:
            p_parent = p.parent if p else None
            q_parent = q.parent if q else None

            # if p_parent is in q_path, then p_parent is the LCA
            if p_parent and p_parent in q_path:
                return p_parent
            # otherwise, add p_parent to p_path
            elif p_parent:
                p_path.add(p_parent)

            # do the same for q_parent as above
            if q_parent and q_parent in p_path:
                return q_parent
            elif q_parent:
                q_path.add(q_parent)

            # move p and q up to their parents
            p = p_parent
            q = q_parent

        # this will never be reached because p and q are guaranteed to exist in the tree
        return None
